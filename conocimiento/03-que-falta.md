# AI-DLC v2 — ¿está hecho? ¿qué habría que cambiar?

Estado real de [`../aidlc-v2/`](../aidlc-v2/) (2.6.54) frente a lo que necesitaría una organización en entorno regulado.

Ver también: [01 — fuentes](01-fuentes.md) · [02 — cómo funciona](02-como-funciona.md) · [04 — v1 vs v2](04-v1-vs-v2.md)

---

## Respuesta corta

**El motor está hecho. El método específico de una organización no, y el repo está diseñado para que no lo esté.**

Entrega un *runtime* de metodología: máquina de estados, 33 etapas, 14 agentes, compuertas, auditoría, sensores, bucle de aprendizaje, siete harnesses. Eso no hay que construirlo.

Lo que deja deliberadamente vacío es **el contenido del método**: qué secciones debe tener un documento de requisitos, qué prácticas afirma el equipo, qué regulación aplica, qué comando de check define «hecho». Esos huecos son la superficie de extensión.

Y hay una lista corta de cosas **rotas o sin construir**, con issues abiertos.

---

## 1. Lo que ya está hecho

| Capacidad | Estado |
|---|---|
| Motor de orquestación determinista | Completo, 4 subcomandos, directiva tipada única por paso |
| Máquina de estados workflow / fase / etapa | Completa, 6 estados, transiciones propiedad del motor |
| 33 etapas × 5 fases, 14 agentes, 11 scopes | Completo |
| Compuertas + escotilla tras 3 revisiones | Completo |
| Auditoría de 85 eventos, audit-first, shards por clon | Completo, con tests |
| Reviewers adversariales con presupuesto y congelación | Completo (Goal 4 = Shipped) |
| Bucle de aprendizaje con admisión sin override | Completo |
| Cadena de reglas de 5 capas | 4 de 5; la de etapa está reservada sin construir |
| Composer adaptativo con puntuación de entropía | Completo (Goal 3 = Shipped) |
| Spaces / intents / multi-repo / org-KB | Completo (Goal 7 = Shipped) |
| Mecanismo de plugins | Shipped, con piezas diferidas (§3) |
| 7 harnesses desde un core | Completo; paridad desigual (§4) |
| Ensemble de tres roles | Completo (Goal 1 = Shipped) |
| Windows nativo, sin WSL | Soportado |

---

## 2. Lo que deja vacío a propósito — aquí está el trabajo

### 2.1 Las plantillas de artefacto — la ranura más importante, y está vacía

`core/memory/templates/` contiene **solo un `.gitkeep`**. El nivel de framework (`tools/data/templates/`) también. Cero plantillas, en ambos niveles.

El `.gitkeep` explica la ranura:

> Un equipo deja `<artifact>.md` aquí con la forma de H2 que quiere, y **ambos lectores la usan** — el agente rellena el esqueleto, y el sensor `required-sections` verifica contra el mismo archivo. **El framework no envía plantillas por defecto** — la resolución cae al piso de ≥2 H2.

Consecuencias:

- **Sin plantillas, `required-sections` verifica que el documento tenga dos H2.** No es control de calidad documental.
- **Con plantillas, es conformidad de forma real**, y la forma producida y la verificada **no pueden divergir**.

Para entorno regulado esta es *la* palanca. Si un requisito dice que todo documento de requisitos lleva clasificación de datos, matriz de trazabilidad y firma de aprobación, se escribe una vez como `requirements.md` en `memory/templates/`.

**Nadie ha escrito esas plantillas. Ni AWS.**

### 2.2 `team.md` y `project.md` — encabezados con ejemplos comentados

Suman 110 líneas y **ni una de contenido activo** — solo encabezados (`## Way of Working`, `## Walking Skeleton`, `## Testing Posture`, `## Deployment`, `## Code Style`, `## Forbidden`, `## Mandated`, `## Corrections`) con ejemplos en comentarios HTML.

**Lo que sí está lleno es `org.md`** — 116 líneas de opinión del framework: trunk-based development, squash-merge de Bolts, ladder prompt, posturas de testing por scope con piso de 80% de cobertura para `mvp`/`enterprise`/`feature`/`infra`/`classic`, deploy-on-merge a staging con aprobación manual a producción.

> **Esa es la postura de AWS.** Contradecirla desde `team.md` no está permitido — la compuerta de admisión rechaza contradicciones con `org.md` y **no hay override**. Solo revisar, saltar o escalar. Cada default que no encaje es una decisión explícita.

### 2.3 El conocimiento de compliance es genérico

`aidlc-compliance-agent` trae **115 líneas**: PCI-DSS, HIPAA, SOC 2, GDPR, nivel panorámico y orientado a AWS. Material de arranque, no la regulación concreta de nadie. Va en `aidlc/knowledge/aidlc-compliance-agent/` (nivel de space, propiedad del equipo, nunca sobreescrito).

### 2.4 El comando de check y la spec protegida

> Un check que siempre pasa, o una spec vacía, le entrega al swarm un sello de goma.

No lo aporta el framework. Es infraestructura del proyecto, y es la condición de entrada a la autonomía en Construction.

### 2.5 El conocimiento de dominio del equipo

`aidlc/knowledge/` se crea **vacío**. Sin estructura obligatoria. DocumentKB llegó en 2.6.15 — rebanada S1 de una feature en construcción (#714, #731).

---

## 3. Lo roto o sin construir

Del propio `docs/roadmap.md` (estado 2026-08-10) y de los docs de referencia. Con seguimiento público, lo cual habla bien del proyecto.

### Bloqueantes para entorno regulado

| Hueco | Estado | Por qué importa |
|---|---|---|
| **Severidad `blocking` de sensores** | Reservada; abierta en **#431** | Los 6 son advisory. **Nada bloquea una compuerta por fallar una verificación determinista.** |
| **Provenance a nivel de commit** | *«Open design question»* | *«La cadena de auditoría actual no provee un lookup inverso durable desde un commit de origen arbitrario a su intent y workflow.»* Si una auditoría pregunta «¿de qué requisito salió esta línea?», no hay respuesta mecánica. |
| **Trazabilidad per-stage enforcement** | PR **#401** abierto, necesita rebase | Goal 6 = **Parcial**. Existe el grafo, la cobertura upstream y la provenance de claims; falta el enforcement. |
| **Propagación de resultados obsoletos** | PR **#716** en vuelo | Si una etapa upstream se re-corre, los downstream no se marcan stale automáticamente. |
| **Enriquecimiento progresivo in-place** | North Star sin construir | Las etapas downstream generan artefactos nuevos en vez de enriquecer los upstream. |
| **Ciclos cross-stage gobernados** | Goal 5 = **Parcial** | *«Los bucles de feedback cross-stage disparados por etapa siguen sin construir.»* PR #616 es un caso estrecho. |
| **Reglas por etapa** | Reservadas, sin construir | La 5ª capa de la cadena no existe. |

### Operacionales

| Hueco | Estado | Impacto |
|---|---|---|
| **Sin contrato de upgrade** | **#636**; PR #535 cerró sin merge | El único consejo es *«re-copy your `dist/<harness>/`»*. **Las ediciones al árbol del harness se pierden.** Sobrevive `aidlc/` porque es un directorio neutral separado — ese diseño es lo que salva. |
| **Releases desalineados** | **#635** | GitHub sigue marcando `v1.0.1` como Latest. *«Los números de versión describen el árbol committeado; no son GitHub Releases.»* Se clona una rama, no se descarga un artefacto. |
| **Dependencia dura de bun** | **#399** | 17 hooks y 41 herramientas en bun. En Windows hay que asegurarlo en el PATH de shells **no interactivas**. |
| **Packaging / instalación / rollback** | **#722**, pilar estratégico | Sin instalador, sin npm, sin rollback. Hoy es `cp -R`. |
| **Benchmarks de resultado** | **#684** propuesto, **#223** rastreado, **no es stream activo** | No existe medición repetible de **si AI-DLC mejora resultados**. Ni de AWS. *Ojo: sí existe instrumentación de proceso — ver la corrección abajo.* |

### Del mecanismo de plugins

- **`required_sections` de un plugin mergea y valida pero no llega al nodo compilado** — *«nada falla una etapa por una sección declarada faltante todavía»*. El único camino a conformidad de forma sigue siendo las plantillas.
- **El subárbol `memory/` no se proyecta** — un plugin **no puede aportar reglas ni política de fase**.
- **`when:` se parsea pero ningún consumidor lo evalúa.**
- **`aidlc.contributes` no se lee** — el packager descubre por convención de directorios.
- Sin discovery remoto, sin marketplace, sin trust (**#723**).
- **Kiro no tiene compuerta de confianza en instalación.** *«Trata un drop de plugin en Kiro como `git clone && run`.»*

---

## 4. Kiro específicamente

Todo lo sustantivo es **idéntico** — son las mismas herramientas desde `.kiro/tools/`. Lo que cambia:

| Área | Claude Code | Kiro CLI / IDE |
|---|---|---|
| Compuertas y preguntas | widget `AskUserQuestion` | **Opciones numeradas en prosa**. El archivo de preguntas sigue siendo la fuente de verdad |
| Statusline | etapa + modelo + % contexto | **No disponible** |
| Swarm | `Task` paralelo, Workflow opcional | **`AIDLC_USE_SWARM=1` se anuncia como no-op** |
| Eventos de sesión | `SESSION_STARTED/RESUMED/ENDED`, `SESSION_COMPACTED` | **Solo `SESSION_STARTED`** |
| Stop hook (enforcement del bucle) | interactivo + headless | **Solo sesiones interactivas** en CLI |
| MCP | 5 servidores | CLI: los mismos 5 **deshabilitados**. IDE: **ninguno** |
| Kiro IDE — grants de tools | por agente, con alcance | frontmatter **sin alcance, más ancho que el sandbox del JSON de CLI** |

Dos tocan la traza:

1. **La traza de sesión es incompleta.** Sin `SESSION_ENDED` ni `SESSION_COMPACTED`, el registro de 85 eventos tiene menos eventos en la práctica.
2. **El enforcement del bucle se debilita en no interactivo.**

PRs abiertos de paridad: **#653** y **#555**.

> El README advierte además que en Kiro funciona mejor con **Claude Opus 4.8** (plan de pago), y que *«con modelos más débiles el conductor puede saltarse pasos opcionales de etapa o apurar las compuertas»*.

---

## 5. El costo de personalizar

**Sin fork** (vive en `aidlc/`, sobrevive a un re-copy):
reglas en `memory/team.md` y `project.md` · plantillas en `memory/templates/` · conocimiento en `aidlc/knowledge/` · documentos en DocumentKB · scopes compuestos · `settings.local.json`.

**Con fork** (autorar en `core/` y correr `bun scripts/package.ts`):
añadir o editar una **etapa** · añadir un **agente** · definir un **scope** a mano · autorar un **sensor** · cambiar el `tier_cap`.

Nada requiere TypeScript — todo es Markdown con frontmatter. Pero **sí requiere ser dueño del árbol `core/` y re-empacar**, y `dist/` está drift-guarded. Con 187 releases en cuatro meses, mantener un fork rebasado tiene costo creciente.

**El mecanismo de plugins existe para evitar ese fork en lo aditivo** — pero hoy no puede aportar reglas ni hacer cumplir secciones requeridas.

> **Empezar por lo que no requiere fork.** Plantillas, reglas, conocimiento y un check de proyecto real cubren la mayor parte de lo que necesita un entorno regulado, sin deuda de mantenimiento.

---

## 6. Lo que no cubre en absoluto

| Falta | El repo tiene | Lo que haría falta |
|---|---|---|
| **Documento de metodología para una organización** | documentación de implementación (~18.600 líneas) + whitepaper de 6 páginas | Un documento para quien no va a leer 18.600 líneas |
| **Caso de adopción** | ninguno | Por qué esta organización, en este contexto |
| **Criterio de proporcionalidad** | 11 scopes y un composer | El criterio humano de cuándo usar cuál, y cuándo nada |
| **Mapeo regulatorio concreto** | 115 líneas genéricas | El marco propio, mapeado a etapas, artefactos y compuertas |
| **Rollout y madurez** | `workshop-mode.md` (receta manual) | Cómo lo adopta un equipo, en qué orden, con qué señales |
| **Evidencia de resultados** | nada; benchmarks propuestos (#684) | Lo medible honestamente en el propio contexto |
| **La hoja de hidratación de C2** | el mecanismo, vacío | Qué reglas ya son ejecutables deterministas y cuáles arrancan como criterio humano — el Principio 7 hecho plan |

Ese último es el más valioso. El whitepaper es honesto: la hidratación de C2 es incremental y toma tiempo, alineamiento y refinamiento iterativo. **Nadie ha publicado cómo se hace en una organización real.**

---

## 7. Lectura de conjunto

**No hay que hacer el AI-DLC. Está hecho, y bien hecho.** Lo que hay que hacer es lo que el framework, por diseño, no puede hacer por nadie:

1. **Escribir las plantillas de artefacto.** Mayor retorno por unidad de esfuerzo, sin fork.
2. **Decidir qué hacer con los defaults de `org.md`.** La compuerta de admisión no admite override.
3. **Aportar el marco regulatorio real.**
4. **Tener un comando de check y una spec protegida que valgan algo.**
5. **Escribir la ruta de hidratación de C2.**
6. **Documentar el método para humanos.**

Y declarar los tres huecos que no se cierran desde afuera: **sensores sin severidad bloqueante (#431)**, **sin provenance a nivel de commit**, y **sin contrato de upgrade (#636)**. Los tres con issue abierto; ninguno con fecha.

---

## Corrección — la medición no está tan vacía como dije

Al leer `core/skills/` aparecieron tres skills que había pasado por alto. **Cambian el matiz sobre medición:**

| Skill | Qué da |
|---|---|
| `aidlc-session-cost` | Duración, compuertas superadas, escrituras al diario, disparos de sensores, aprendizajes capturados — todo desde el grafo de runtime |
| `aidlc-replay` | El rastro de auditoría convertido en narrativa legible: qué se decidió, en qué orden, por qué |
| `aidlc-outcomes-pack` | Documento único de traspaso al cerrar el workflow |

Así que la distinción correcta es:

- **Instrumentación de proceso** — *sí existe*. Qué consumió este workflow, qué se decidió, qué queda. Es auditable y determinista.
- **Benchmark de resultado** — *no existe*. Nadie, tampoco AWS, puede mostrar con datos que el método mejora la entrega frente a no usarlo.

Lo primero sirve para gobernar una corrida. Lo segundo es lo que haría falta para justificar la adopción con números, y **eso sigue siendo aporte disponible**.
