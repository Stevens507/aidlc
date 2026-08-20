# AI-DLC v2 — cómo funciona por dentro

Estudio de [`../fuentes/repo-oficial/v2/`](../fuentes/repo-oficial/v2/) (2.6.18) y del whitepaper *AI-DLC Workflows 2.0 Specification*.

Ver también: [01 — fuentes](01-fuentes.md) · [03 — qué falta](03-que-falta.md) · [04 — v1 vs v2](04-v1-vs-v2.md)

---

## 0. La distinción que hay que sostener

> **AI-DLC es una metodología** — un enfoque estructurado y con compuertas, definido por AWS. **Este repositorio es su implementación nativa multi-harness.** La metodología es el *qué*; cada distribución por harness es el *cómo* para un runtime.

Se puede adoptar la metodología sin adoptar el repo, y criticar el repo sin tocar la metodología.

---

## 1. La arquitectura de tres planos

El modelo mental que explica casi todo lo demás. El repo lo toma prestado, explícitamente, de la arquitectura de routers modernos.

| Plano | En redes | En AI-DLC | Cadencia |
|---|---|---|---|
| **Control** | BGP, OSPF, cómputo de rutas | Definiciones de etapa, reglas, sensores — *el esquema de lo que debe correr* | Al arrancar el workflow |
| **Datos** | Reenvío de paquetes | Ejecuciones de etapa, Bolts, invocaciones de agente — *las corridas reales* | Continuo |
| **Gestión** | SNMP, dashboards, CLI | `/aidlc --doctor`, el log de auditoría, consultas | Cadencia humana |

**La frontera de compilación es la pieza central.** Al arrancar el workflow, `aidlc-graph.ts compile` lee el frontmatter de las 33 etapas, recorre `memory/` y `sensors/`, resuelve cada import y emite `stage-graph.json` con las respuestas ya horneadas en cada nodo. Durante todo el workflow el runtime **lee campos pre-resueltos**; no vuelve a caminar la cadena de herencia.

De ahí sale la propiedad más contraintuitiva del sistema:

> **Un aprendizaje capturado a mitad de workflow no cambia las reglas del workflow en curso.** Escribe en disco, pero la vista compilada en vuelo no se toca. Aplica en el siguiente compile.

Justificación: BGP no recomputa rutas a mitad de vuelo de un paquete. El pago es predictibilidad — las compuertas ya aprobadas dieron fe de un conjunto estable de reglas.

Un segundo grafo, `runtime-graph.json`, es el plano de datos: se recompila con un recorrido event-sourced completo del log de auditoría en cada evento de transición.

**Recuperación como propiedad emergente.** Cinco fuentes reconstruyen el estado tras compactación o reinicio, en este orden: artefactos → `memory.md` por etapa → shards de auditoría → documentos de estado → `runtime-graph.json`. El mismo orden en que un humano retoma trabajo ajeno. Lo que **no** se puede reconstruir es el ritmo conversacional de la sesión anterior; el repo lo declara propiedad fundamental de las sesiones LLM, no defecto corregible.

---

## 2. El bucle: motor determinista ↔ conductor

- **El motor** (`aidlc-orchestrate.ts`, cuatro subcomandos: `next`, `continue`, `report`, `park`) es código TypeScript determinista. Posee **toda** decisión entre etapas: scope, ruteo, resolución de saltos, guardas de resume, estado de compuerta, terminación.
- **El conductor** (`SKILL.md`, lo que invoca `/aidlc`) es un **bucle de reenvío delgado**. No es el plano de control.

```
Loop:
  1. directive = aidlc-orchestrate.ts next $ARGUMENTS
  2. actuar según directive.kind
  3. aidlc-orchestrate.ts report --stage <slug> --result <outcome>
  4. repetir hasta directive.kind == done
```

Cada `next` devuelve **exactamente una** directiva tipada en JSON y **no muta nada**. Ocho tipos se emiten hoy: `load-steering`, `run-stage`, `invoke-swarm`, `ask`, `print`, `error`, `done`, `parked`.

> El motor posee el ruteo; el conductor posee la *calidad de ejecución* dentro del movimiento que el motor nombra.

Detalles del borde:

- El conductor pasa `$ARGUMENTS` verbatim al primer `next`. **No pre-parsea.**
- Si una directiva parece malformada, debe decirlo y **detenerse** — nunca improvisar el ruteo en prosa.
- El motor nunca llama a `AskUserQuestion`; delega el turno humano al conductor.

**Y el conductor tiene instrucciones explícitas de callarse.** *«Un experto trabajando junto a alguien no narra sus pulsaciones.»* El estado de reposo entre llamadas es cero prosa. Solo hablan el campo `narration` de una directiva (redactado por la herramienta que conoce los hechos) y las líneas `SAY:` del protocolo.

---

## 3. La etapa: los tres compartimentos en concreto

Ejemplo real (`inception/requirements-analysis.md`):

```yaml
slug: requirements-analysis
phase: inception
lead_agent: aidlc-product-agent
mode: inline
# ---------- C1: el QUÉ ----------
produces: [requirements, requirements-analysis-questions]
consumes:
  - {artifact: intent-statement, required: false}
  - {artifact: business-overview, required: false, conditional_on: brownfield}
requires_stage: [approval-handoff, reverse-engineering]
# ---------- C2: CÓMO SABEMOS QUE ESTÁ BIEN ----------
summary_confirmation: required
reviewer: aidlc-product-lead-agent
reviewer_max_iterations: 2
review_class: advisory
sensors: [required-sections, upstream-coverage]
```

Y el cuerpo lleva secciones `## Sensors` y `## Learn` explícitas — C3 vive ahí, con el diario de cuatro encabezados: **Interpretations / Deviations / Tradeoffs / Open questions**.

> Los archivos de etapa son **artefactos inmutables del framework**. El ritual de aprendizaje escribe en el harness, nunca en el archivo de etapa. Esa disciplina permite actualizar el framework sin perder personalizaciones.

**Secuencia canónica:** `preguntas → artefacto → reviewer (si se declara) → learnings → compuerta`.

---

## 4. Compartimento 2 — la verificación, en tres capas

### Capa A — Sensores (determinista)

Seis sensores. Disparan desde un hook `PostToolUse` en cada Write/Edit, filtrados por un glob `matches`:

| Sensor | Dispara en | Verifica |
|---|---|---|
| `claim-sources` | salidas de Intent Capture | toda afirmación lleva etiqueta de fuente que resuelve al registro confirmado |
| `required-sections` | markdown del record dir | presencia de los H2 requeridos |
| `upstream-coverage` | markdown del record dir | los entregables referencian cada artefacto upstream declarado |
| `traceability` | `traceability.json` | IDs upstream declarados y cubiertos, targets downstream existentes |
| `linter` | `.ts` / `.js` | envuelve el linter del proyecto (ESLint por defecto) |
| `type-check` | `.ts` / `.tsx` | envuelve el type-checker (tsc por defecto) |

> **Los seis son `default_severity: advisory`.** El schema acepta hoy exactamente un valor; `blocking` está *reservado*. Un sensor que falla produce una fila `SENSOR_FAILED` y un archivo de detalle — **no bloquea la compuerta**.

Las reglas pueden declarar `pairing: <sensor-id>` o `pairing: feedforward-only` — declaración explícita de que el framework *no puede* verificar esa regla deterministamente. Obligar a declarar lo no verificable es de las mejores ideas del diseño.

### Capa B — Reviewers (inferencial, con salvaguardas)

Dos agentes solo-lectura: `aidlc-product-lead-agent` (requisitos, historias, UX) y `aidlc-architecture-reviewer-agent` (diseño técnico, código). Disparan solo si la etapa declara `reviewer:`.

Se despacha como **sub-agente separado** y recibe la definición, el Q&A y los artefactos — **nunca el `memory.md` ni el plan del constructor**. Escribe una sección `## Review` con un veredicto: **READY** o **NOT-READY**.

Dos clases, resueltas por el motor con regla low-wins (clase de la etapa, `review_cap` del scope, override `--review`):

- **`advisory`** — una pasada, ambos veredictos terminales. Hallazgos citados verbatim en la compuerta.
- **`adversarial`** — el reviewer *intenta refutar*. READY es el veredicto al que **falla en llegar**, no el default. NOT-READY → el constructor re-corre, hasta `reviewer_max_iterations` (2).

Las salvaguardas contra las patologías del LLM-as-judge:

1. **Presupuesto duro de turnos** (`maxTurns: 60`), nativo donde el harness tiene la palanca.
2. **Borrado antes de cada despacho.** Se elimina cualquier `## Review` previa, para que un READY anterior no se lea como cubriendo trabajo nuevo. Con esa regla, «no hay sección» significa «revisión incompleta» uniformemente.
3. **Un veredicto solo cuenta si parsea.** Sección faltante o duplicada = intento INCOMPLETO. Se reintenta una vez sin consumir iteración; un segundo intento incompleto registra `NOT-READY` con el hallazgo *«review did not complete within its turn budget»*. **Un corte silencioso se vuelve hallazgo visible, nunca veredicto ausente ni deadlock.**
4. **Presupuesto aplicado por el motor.** `aidlc-log.ts review` rechaza una `--iteration` que exceda el presupuesto.
5. **Congelación tras recibo terminal.** Cualquier escritura posterior a un artefacto de `produces[]` invalida el recibo y el motor **rechaza la compuerta**.
6. **El reviewer nunca bloquea.** El humano tiene la última palabra.

### Capa C — Verificación de frontera de fase

```
Intent → Scope → Requirements → Designs → Units → Code → Tests → Deployment
```

| Frontera | Se verifica |
|---|---|
| Ideation → Inception | intent capturado, alcance definido, viabilidad confirmada |
| Inception → Construction | requisitos trazados a diseños, units definidas, plan aprobado |
| Construction → Operation | units construidas y probadas, CI configurado, infra diseñada |

Si falla, se presentan los problemas y **no se avanza**.

---

## 5. Las compuertas

Toda etapa salvo las 3 de Initialization requiere aprobación explícita. Default: **Approve** / **Request Changes**.

**Regla de no-comportamiento-emergente:** Construction y Operation deben usar *siempre* el formato de 2 opciones. Solo Ideation e Inception pueden añadir una tercera, y únicamente para readmitir una etapa saltada.

**Escotilla de escape:** tras 3 «Request Changes» sobre la misma etapa, la 4ª compuerta añade «Accept as-is». Tras el 2º ciclo se avisa. Reconoce que el bucle de revisión puede volverse trampa y le pone salida visible.

**Verificación mecánica:** `approve` rechaza una etapa cuyos artefactos declarados en `produces` no existen en disco.

Seis estados: `[ ]` no iniciada · `[-]` en progreso · `[?]` esperando aprobación · `[R]` revisando · `[x]` completada · `[S]` saltada.

**Las transiciones son propiedad del motor.** El conductor reporta y nunca escribe checkboxes ni emite eventos por prosa. Hay tests que lo guardan.

### El flujo tri-modal de preguntas

**Guide me** (interactivo, lotes de máx. 4×4) · **I'll edit the file** · **Chat**. En los tres el archivo es el registro autoritativo, con **confirmación consolidada** y recibo que liga el turno humano al digest del archivo.

Y una sección entera de **prevención de exceso de confianza**:

> Por defecto preguntar, no asumir. Nunca proceder con ambigüedad. Banderas rojas: respuestas de una palabra a preguntas abiertas; «lo que tú creas»; señales contradictorias; esquivar la pregunta. Cuando el usuario defiere: *«Quiero asegurarme de que el diseño refleje TUS prioridades.»*

Detección de contradicciones cruzadas: desajuste de alcance, de riesgo, conflictos tecnológicos, timeline vs alcance. **No proceder hasta resolver.**

---

## 6. Compartimento 3 — el bucle de aprendizaje

> **El único trabajo que hace el modelo en este bucle es escribir observaciones en `memory.md`.** Todo lo posterior — contar, aflorar, rutear, escribir — lo hace herramienta determinista o la elección explícita del humano.

1. **Diario** — `memory.md` por etapa, cuatro encabezados, timestamps ISO.
2. **Aflorar** — `aidlc-learnings.ts surface` emite candidatos **verbatim**. Sin parafraseo ni filtrado.
3. **Confirmar** — siempre se pregunta *«Anything to add for next time?»* aunque no haya candidatos; nunca se infiere «nada». La única clasificación pedida al humano es el encabezado, que determina el destino.
4. **Chequeo de admisión** — se compara contra `org.md`. Si contradice: **revisar / saltar / escalar**. **No hay override.**
5. **Persistir** — práctica en `memory/project.md` (default) o `team.md` (promoción de un clic). Emite `RULE_LEARNED` o `SENSOR_PROPOSED`.

Gobierno:

- **No hay camino de escritura a scope org.**
- **Default al scope más estrecho** (project), para que la sorpresa de un proyecto no se vuelva regla de la organización.
- **Las «Open questions» no promueven.**
- Si el aprendizaje es un *binding de sensor*, la instalación es de dos escrituras atómicas.

### Cadena de cinco capas

```
org → team → project → phase → stage
```

**Estrictamente aditiva.** Nada se descarta ni sobreescribe en runtime. El scope se deriva del *nombre de archivo*. Los conflictos se atrapan **al escribir**, no en runtime. Los keywords `enforcement:` y `overrides:` fueron **eliminados del schema**.

---

## 7. Construction — la apuesta real de v2

### Tres dueños

| Preocupación | Dueño | Dónde vive |
|---|---|---|
| **Postura** de autonomía (default) | ingeniero de harness | regla en `memory/{team,project}.md` |
| Qué Units **pueden** paralelizarse | ingeniero de harness | `units-generation` y su DAG |
| El **chequeo de convergencia** | ingeniero de harness | comando de build/test del proyecto + spec protegida |
| El **otorgamiento** de autonomía | **el humano** | ladder prompt en runtime |
| El **driver** del swarm | el operador | `AIDLC_USE_SWARM` |
| El **veredicto**, merge-back y auditoría | una herramienta | `aidlc-swarm.ts` |

*El determinismo pertenece a una herramienta, el conocimiento a un agente, el juicio a un humano.*

### El flujo

Construction corre **Bolt por Bolt**, guiado por `bolt-plan.md` y el DAG.

1. El **primer Bolt es el walking skeleton**. Su compuerta se presenta **siempre**.
2. Tras aprobarla, el **ladder prompt** dispara una vez: continuar autónomamente o comprobar cada Bolt. Persiste como `Construction Autonomy Mode`, emite `AUTONOMY_MODE_SET`.
3. Los Bolts elegibles forman un **batch**: N llamadas `Task` **en un solo mensaje**, una compuerta a nivel de batch.

**Halt-and-ask sin importar el modo de autonomía.** Fallo parcial de un batch: esperar a todas las Tasks, **preservar los artefactos de los exitosos**, y presentar retry / skip / abort acotado al fallido.

### Los dos frenos

**Freno 1 — Plan Approval es parada dura en todo modo.** Fingerprint SHA-256 sobre plan + instrucciones de test. Cualquier cambio posterior lo invalida y reabre la aprobación. *«No comiences la generación, no despaches al agente desarrollador, y no infieras aprobación de una continuación del bucle de reenvío.»* Durante Bolts se suprime la compuerta *de completitud*, **nunca** la de Plan Approval.

**Freno 2 — el swarm no cree a sus workers.**

> Un trabajador puede afirmar que su Unit convergió. **El framework nunca toma esa afirmación por buena.** La señal autoritativa es el **comando de check del proyecto**: exit `0` = convergido.

Con anti-tampering: el árbitro compara la spec designada contra su baseline en git forkeado, **para que nadie debilite el test que define «hecho»**.

> **Un check que siempre pasa, o una spec vacía, le entrega al swarm un sello de goma.**

### Dónde existe la paralelización

Solo en los scopes donde corre `units-generation`: `enterprise`, `feature`, `mvp`, `classic`, `workshop`. Los incrementales (`bugfix`, `refactor`, `security-patch`) y `poc`/`infra`/`express` corren Construction de una sola pasada.

> La autonomía en Construction es propiedad de los scopes greenfield multi-Unit, no de todos.

---

## 8. Adaptación: scopes, profundidad, composer

Tres perillas ortogonales: **scope** (qué etapas), **depth** (cuánto detalle), **test strategy** (cuántos tests).

| Scope | EXECUTE / 33 | Depth | Test |
|---|---|---|---|
| `enterprise` | 33 | Comprehensive | Comprehensive |
| `feature` | 33 | Standard | Standard |
| `classic` (default implícito) | 26 | Standard | Standard |
| `workshop` | 26 | Standard | Minimal |
| `mvp` | 23 | Standard | Standard |
| `infra` | 13 | Standard | Standard |
| `security-patch` | 10 | Minimal | Minimal |
| `express` | 10 | Minimal | Minimal |
| `poc` | 8 | Minimal | Minimal |
| `refactor` | 8 | Minimal | Minimal |
| `bugfix` | 7 | Minimal | Minimal |

La línea de confirmación **siempre nombra los números exactos** — etapas, compuertas, fan-out per-unit — computados de la grilla, nunca estimados. *Sabes a qué estás consintiendo antes de que arranque el workflow.*

**Regla de desambiguación:** keyword de scope + descripción de más de 5 palabras = match incidental → dispara la oferta de composición.

### El composer

`aidlc-composer-agent` estima cinco componentes de **entropía de implementación** —ambigüedad de intención, incertidumbre estructural, entropía de verificación, riesgo, supuestos sin resolver— y propone la **grilla EXECUTE/SKIP mínima viable**.

Cada EXECUTE nombra el componente que reduce, cada SKIP nombra qué ya lo cubre, y **cortar la espina dorsal se trata como el fallo peligroso**. Nada se escribe antes de aprobación explícita.

**Higiene de keywords:** los scopes compuestos salen con `keywords: []`.

**Recompose en vuelo:** solo etapas pendientes por delante del cursor; las completadas están **congeladas**; validación `--strict` para que ninguna quede sin input requerido; la primera etapa EXECUTE de Construction **no puede voltearse**.

---

## 9. El workspace

```
aidlc/
├── active-space                      ← cursor (gitignored, por usuario)
└── spaces/default/
    ├── memory/                       EL MÉTODO — org/team/project.md, phases/, templates/
    ├── knowledge/                    conocimiento de dominio (libre)
    │   ├── documents/                  originales del equipo
    │   └── documentkb/                 catálogo derivado (tool-owned)
    ├── codekb/<repo>/                base de conocimiento por repo
    └── intents/
        ├── intents.json              registro: uuid, slug, scope, repos, status
        └── 260624-export-bug/        un record dir por intent
            ├── aidlc-state.md
            ├── audit/<host>-<clone>.md
            └── <phase>/<stage>/*.md
```

- El directorio del harness (`.claude/`, `.kiro/`, `.codex/`, `.aidlc/`) es la **única** parte que difiere por harness.
- **Los dos cursores son gitignored y por usuario** — dos compañeros pueden estar en intents distintos.
- **La auditoría se commitea como shards por clon** para que git nunca mergee appends concurrentes. No hay `merge=union`; es deliberado.

### Configuración de dos ejes

| | Framework | Equipo |
|---|---|---|
| **Cargado continuamente** | `skills/`, `agents/`, `knowledge/`, `memory/org.md`, `scopes/`, grafos | `memory/team.md`, `memory/project.md` |
| **Artefacto por workflow** | *(vacío por diseño)* | `aidlc-state.md`, `audit/`, artefactos, worktrees |

La celda vacía es la firma de la regla, no un hueco.

**Convención:** sobreescribir en `team.md` / `project.md`, no mutar los defaults. Nada lo hace cumplir; mantiene los overrides visibles en revisión y permite actualizar limpiamente.

**La excepción de promoción cruzada.** Practices Discovery (2.2) es la **única** etapa que escribe en ambas filas, condicionada a afirmación:

> Sin la compuerta de afirmación, el framework pondría palabras en boca del equipo — y peor, persistirían. Con la compuerta, el equipo siempre fue quien las escribió.

---

## 10. Auditoría y trazabilidad

**85 tipos de evento** en un registro canónico.

### Atomicidad audit-first

Los comandos que mutan estado emiten auditoría **antes** de mutar:

1. Si la emisión falla, la herramienta lanza **antes de tocar el estado**.
2. Si la escritura falla después, hay entrada de «intención» sin movimiento de estado. **La deriva es visible y diagnosticable.**

Hay un test que hace chmod de solo-lectura sobre el archivo de auditoría y afirma que el estado se queda en `[?]`, no en `[x]`.

Dos excepciones razonadas por escrito: **audit-of-intent** (worktrees, copias de auditoría, despacho de merge) y **audit-last** para el catálogo derivado de DocumentKB:

> **Una entrada faltante subestima lo que pasó; una entrada fantasma afirma algo falso.** Para un artefacto derivado que puede reconstruirse, subestimar es el fallo más seguro. El mismo razonamiento no se extiende a ningún archivo de estado autoritativo.

### Patrones prohibidos

La CLI rechaza mecánicamente los recibos que portan autoridad — `HUMAN_TURN`, `GATE_APPROVED`, `GATE_REJECTED`, `QUESTION_ANSWERED`, `REVIEW_REQUESTED`, `REVIEW_COMPLETED`, `SWARM_STARTED`, `AUTONOMY_MODE_SET` y los cuatro `UNIT_*`. **Son exactamente los eventos que las guardas del motor leen como evidencia de autorización. Un LLM no puede fabricar su propio permiso.**

Un test de deriva exige que cada evento documentado tenga su emisor en código, y viceversa.

---

## 11. Extensibilidad

| Guía | Eres… | Cambias… |
|---|---|---|
| **User Guide** | quien construye *con* AI-DLC | nada del framework |
| **Harness Engineer Guide** | quien re-forma *cómo se comporta* | los **datos**: etapas, agentes, scopes, reglas, sensores, conocimiento |
| **Developer Reference** | quien cambia AI-DLC *mismo* | el **código** |

**El mecanismo de plugins** puede **añadir** etapas, agentes, scopes, reglas y sensores, y **modificar aditivamente** etapas del core. Principios: estrictamente aditivo (nunca override), core inmutable, reversible cuando está apagado, el slug es la identidad.

La confianza es nativa del host. **AI-DLC no construye capa de confianza propia** — y es explícito sobre el hueco: Kiro no tiene tienda, así que el folder-drop **no tiene compuerta de confianza**. *«Trata un drop de plugin en Kiro como `git clone && run`.»*

---

## 12. Evaluación

### Lo sólido

1. **La separación motor/conductor.** Que el ruteo sea código determinista y el LLM solo ejecute dentro del movimiento nombrado es lo que hace todo lo demás auditable. Lo más portable a otras metodologías.
2. **Las salvaguardas del reviewer.** El borrado antes de despacho, el «un veredicto solo cuenta si parsea», el presupuesto aplicado por el motor y la congelación tras recibo terminal. La mayoría de frameworks no tienen ninguna de las cuatro.
3. **El bucle de aprendizaje con el LLM acotado a escribir el diario.** Sin override en el chequeo de admisión. Sin escritura a scope org.
4. **La atomicidad audit-first**, con excepciones razonadas y probadas.
5. **La honestidad estructural.** `pairing: feedforward-only`. La celda vacía. El aviso de Kiro.
6. **El consentimiento informado** en la confirmación de scope.

### Lo que no está donde el whitepaper sugiere

1. **Los seis sensores son advisory.** Hoy el único bloqueo duro real es el comando de check del proyecto en Construction.
2. **La autonomía está acotada** a Construction, y dentro de ella a los scopes multi-Unit greenfield.
3. **La calidad depende del modelo.** Con modelos más débiles el conductor puede saltarse pasos o apurar compuertas.
4. **Superficie muy grande.** 33 etapas, 14 agentes, 11 scopes, 17 hooks, 41 herramientas, 7 protocolos, 85 eventos, ~18.600 líneas de documentación.
5. **Velocidad de cambio.** 187 releases en cuatro meses.

### Lo trasladable, aunque no se adopte el repo

- **Directiva única por paso**, y que calcularla no mute nada.
- **Los tres compartimentos como plantilla de etapa.**
- **Declarar lo no verificable** (`pairing: feedforward-only`).
- **La compuerta de admisión sin override.**
- **La afirmación antes de la promoción.**
- **Números exactos antes de consentir.**
- **La escotilla tras tres revisiones**, con aviso previo.
- **«Una entrada faltante subestima lo que pasó; una entrada fantasma afirma algo falso.»**
