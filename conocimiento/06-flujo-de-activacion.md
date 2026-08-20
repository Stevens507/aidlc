# El flujo de activación — qué enciende qué

Trazado sobre el código de [`../fuentes/repo-oficial/v2/`](../fuentes/repo-oficial/v2/) (2.6.18), no sobre la documentación. Donde el código y los docs discrepan, mando el código y lo señalo.

Diagrama: [`diagramas/aidlc-v2-maquinaria.drawio`](diagramas/aidlc-v2-maquinaria.drawio) — 4 páginas.

Si buscas **el método** y no la máquina, está en [07](07-como-se-trabaja.md). Si buscas **un caso concreto de principio a fin**, en `diagramas/aidlc-v2-un-caso.drawio`.

Ver también: [01 fuentes](01-fuentes.md) · [02 cómo funciona](02-como-funciona.md) · [03 qué falta](03-que-falta.md) · [04 v1 vs v2](04-v1-vs-v2.md) · [05 mapa docs](05-mapa-docs-v2.md)

---

## En una frase

> **El motor decide qué hacer. El conductor decide cómo hacerlo bien. Una directiva por paso, y calcularla no muta nada.**

Todo lo demás son detalles de esa frase.

---

## 1. El bucle

```
Bucle:
  1. directiva = aidlc-orchestrate.ts next $ARGUMENTS
  2. actuar según directiva.kind
  3. aidlc-orchestrate.ts report --stage <slug> --result <resultado>
  4. repetir mientras directiva.kind != done
```

Tres propiedades que lo sostienen:

- **`next` no muta nada.** Lee `aidlc-state.md` y `stage-graph.json`, y devuelve **exactamente una** directiva tipada en JSON. Calcular el siguiente paso y ejecutarlo son operaciones separadas.
- **El conductor pasa `$ARGUMENTS` verbatim.** No pre-parsea. El motor resuelve las banderas, el scope, los saltos.
- **Si una directiva parece malformada, el conductor debe detenerse**, no improvisar el ruteo en prosa.

**Ocho tipos de directiva** se emiten hoy: `load-steering`, `run-stage`, `invoke-swarm`, `ask`, `print`, `error`, `done`, `parked`. Otros dos están declarados en el esquema y **nunca se emiten** (`dispatch-subagent`, `present-gate`).

---

## 2. Qué se activa dentro de una etapa

El orden importa, y los pasos 1 a 6 ocurren **antes** de que el LLM escriba una sola línea.

| # | Qué pasa | Quién |
|---|---|---|
| 1 | **`load-steering`** — el motor lee del disco `org.md`, `team.md`, `project.md` y la regla de fase, y entrega el **texto** | motor |
| 2 | **`run-stage`** — llega una directiva con **24 campos ya resueltos** | motor |
| 3 | **Persona + conocimiento** — bloqueante: leer cada archivo de `inline_context_paths` antes de nada más | conductor |
| 4 | **El archivo de etapa** — `stage_file` | conductor |
| 5 | **Artefactos de entrada** — `consumes`, solo los que existen en disco | conductor |
| 6 | **Protocolos condicionales** — `protocol_modules`: solo los que aplican | conductor |
| 7 | Cuerpo de la etapa: preguntas → artefactos, con diario `memory.md` | conductor |
| 8 | Reviewer, si la etapa lo declara — sub-agente separado, no ve el plan del constructor | conductor |
| 9 | Ritual de aprendizajes — una herramienta aflora el diario verbatim | herramienta |
| 10 | Compuerta de aprobación | humano |
| 11 | El motor verifica artefactos, marca `[x]`, emite auditoría, rutea | motor |

### Los 24 campos de `run-stage`

Esto es lo que hace el flujo auditable: **el conductor nunca re-deriva una ruta.**

```
stage · phase · lead_agent · support_agents · mode · single
inline_context_paths · context_warnings · gate · memory_path
consumes · produces · rules_in_context · sensors_applicable · stage_file
reviewer · reviewer_max_iterations · review_class · protocol_modules
swarm_settled · conductor_persona · next_stage · wave · narration
```

Del comentario en `aidlc-directive.ts`: *«Carrying paths makes persona loading observable and enforceable in traces.»* El nombre de un agente **no** es contexto cargado; la ruta leída sí.

---

## 3. Los 17 guardias

No los invoca el LLM. Los registra `settings.json` y los ejecuta el harness — por eso no se pueden saltar.

| Evento | Guardias |
|---|---|
| **PreToolUse** | `deliver-stage-rules` (Task/Agent) · `state-transition-guard` · `reviewer-scope` · `review-freeze` · `plan-approval-guard` (Task) · `fold-usage` |
| **PostToolUse** | `write-audit-log` (Write/Edit) · `run-sensors` (Write/Edit) · `sync-workflow-state` (TaskUpdate) · `record-human-turn` (AskUserQuestion) · `rebuild-stage-graph` (Bash) · `fold-usage` |
| **UserPromptSubmit** | `record-human-turn` |
| **SessionStart / SessionEnd** | `session-start` · `session-end` |
| **PreCompact** | `validate-state` |
| **SubagentStop** | `log-subagent` |
| **Stop** | `continue-workflow` |

**Cada guardia existe porque un LLM se salta el paso que vigila.** `plan-approval-guard` porque un agente empieza a generar sin esperar. `state-transition-guard` porque escribe el estado por su cuenta. `continue-workflow` porque abandona el bucle a medio turno.

Y el cierre: **la CLI de auditoría rechaza que nadie escriba a mano los eventos que portan autoridad** — `HUMAN_TURN`, `GATE_APPROVED`, `REVIEW_COMPLETED`, `AUTONOMY_MODE_SET` y los cuatro `UNIT_*`. Son exactamente los que las guardas del motor leen como evidencia de autorización.

> Un LLM no puede fabricar su propio permiso.

---

## 4. Dos correcciones a la documentación

Verificadas en el código, no en los docs.

### 4.1 El grafo no se compila en cada workflow

Los docs dicen *«compile once at workflow start»*. En la realidad instalada:

- **`stage-graph.json` viene ya compilado en el `dist/`** — 33 nodos, con `rules_in_context` y `sensors_applicable` ya resueltos por etapa.
- El compile local solo se dispara al **cambiar la selección de plugins** (`regenerateSelectionSurfaces`, `aidlc-utility.ts:906` y `:923`).
- `--check` es un guardia de deriva para CI, no un paso de runtime.

Es decir: **el plano de control lo compila AWS al empaquetar**, no tu máquina al arrancar.

### 4.2 Un aprendizaje sí puede aplicar en el mismo workflow

Dos capítulos de la documentación se contradicen:

- `docs/reference/08-rule-system.md`: *«Delivery repeats every stage, so a learning admitted mid-workflow reaches the next stage.»*
- `docs/guide/09-rules-and-the-learning-loop.md`: *«A learning captured at one gate does **not** change the rules for the rest of the current workflow.»*

**El código resuelve la contradicción** (`aidlc-steering.ts`). `readRuleBundle` hace `readFileSync` del archivo **en cada etapa**. Por tanto:

| Tipo de aprendizaje | Cuándo aplica |
|---|---|
| Línea añadida a un archivo que **ya está** en `rules_in_context` (p. ej. `project.md`) — **el caso común** | **La siguiente etapa del mismo workflow** |
| Archivo de regla nuevo, o binding de sensor nuevo | El siguiente workflow (requiere recompilar) |

La afirmación del User Guide es **demasiado fuerte**: cierta para cambios estructurales, falsa para el caso común. Lo que se congela al compilar es **la lista de archivos**, no su contenido.

---

## 5. ¿Está sobre-ingenierizado?

### Lo que se instala

| | |
|---|---|
| Archivos instalados | **262** |
| `.md` (datos que el motor lee) | **191** |
| `.ts` | **58** — **64.800 líneas** |
| `.json` (compilado) | 7 |
| Motor / periferia | 27.590 líneas (47%) / 30.586 (53%) |
| Hooks | 6.617 líneas |
| Documentación para explicarlo | **24.700 líneas** |

**Una línea de documentación por cada 2,6 de código.** Esa proporción no es normal.

### La evidencia de que sí

**Siete abstracciones declaradas en el esquema, todas con cero usos hoy:**

| Abstracción | Estado |
|---|---|
| `mode: agent-team` | quinto modo de ejecución; ninguna etapa lo usa |
| `dispatch-subagent`, `present-gate` | 2 de las 10 directivas, nunca se emiten |
| `kind: llm` en sensores | reservado para v0.11+ |
| `default_severity: blocking` | reservado (#431) — **por eso hoy ningún sensor bloquea nada** |
| Reglas por etapa | la quinta capa de la cadena, sin construir |
| Campo `bundle` | «deliberadamente sin usar» |
| Predicado `when:` | se parsea, ningún consumidor lo evalúa |

A eso se suman cuatro archivos de casi 10.000 líneas cada uno (`aidlc-lib` 9.991, `aidlc-utility` 6.108, `aidlc-orchestrate` 6.100, `aidlc-state` 4.162), y **187 releases en cuatro meses**.

### La evidencia de que no

Casi toda la complejidad **defensiva** está comprada con fallos nombrados:

- Los cinco guardias de `PreToolUse` existen porque un LLM se salta exactamente eso.
- La atomicidad audit-first **tiene un test que la prueba** — chmod de solo-lectura sobre la auditoría, y se afirma que el estado se queda en `[?]`.
- Que la CLI rechace los eventos que portan autoridad cierra el agujero de que un LLM se autorice a sí mismo.
- El borrado de la sección `## Review` antes de cada despacho evita que un READY viejo se lea como nuevo.
- Los 24 campos de la directiva existen para que el conductor **no derive rutas** — lo que hace la carga de contexto observable en la traza.

Ninguno de esos mecanismos es decorativo. Cada uno tapa un fallo concreto que ocurre.

### El veredicto

**No está sobre-ingenierizado en lo defensivo. Sí lo está en lo especulativo.**

La línea es nítida y cae en el mismo sitio en cada capa:

- Lo que **impide un fallo observado** está bien construido y bien probado.
- Lo que **anticipa un futuro** —los siete reservados, las dos directivas fantasma, el quinto modo de ejecución— es peso muerto que hay que leer, mantener y documentar sin que hoy haga nada.

Y hay un coste indirecto que importa más que el conteo de líneas: **la superficie a entender antes de poder operarlo bien.** 33 etapas, 14 agentes, 11 scopes, 7 protocolos, 17 hooks, 85 eventos, 24 campos en una directiva. Un equipo puede usar el framework sin saber nada de eso; pero para **adaptarlo** —que es lo que necesita un entorno regulado— hay que conocerlo.

> El framework es sólido. Su curva de entrada es su verdadero costo, y no aparece en ninguna métrica del repo.
