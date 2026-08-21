# AI-DLC v2 — fuentes

Recopilado el 2026-08-19 leyendo clones de las dos ramas: `main` (1.0.1) y `v2` (commit `fbb1460c`, **2.6.18**).

> Las dos ramas están guardadas en este repositorio, en la misma versión que se estudió: [`../fuentes/repo-oficial/main/`](../fuentes/repo-oficial/main/) y [`../aidlc-v2/`](../aidlc-v2/).

El **texto completo** de estas fuentes está en [`../fuentes/`](../fuentes/FUENTES.md) — ~16.500 palabras.

Ver también: [02 — cómo funciona](02-como-funciona.md) · [03 — qué falta](03-que-falta.md) · [04 — v1 vs v2](04-v1-vs-v2.md) · [05 — mapa docs v2](05-mapa-docs-v2.md)

---

## 1. Oficiales AWS

| Fuente | Copia local | Fecha | Qué aporta |
|---|---|---|---|
| Blog: *AI-Driven Development Life Cycle: Reimagining Software Engineering* — [origen](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) | [`blog-01`](../fuentes/blogs/2025-07-31_ai-driven-development-life-cycle.md) | 2025-07-31 | La metodología original. Referencia canónica del **qué**. |
| Method Definition Paper — [origen](https://prod.d13rzhkk8cj2z0.amplifyapp.com/) | [`../fuentes/paper/`](../fuentes/paper/) — PDF y texto extraído | 2025-07 | Paper de definición del método (Raja SP). |
| Blog: *Open-Sourcing Adaptive Workflows for AI-DLC* — [origen](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/) | [`blog-02`](../fuentes/blogs/2025-11-29_open-sourcing-adaptive-workflows.md) | 2025-11-29 | Anuncio de **v1** open source. Autores: Will Matos, Raj Jain, Siddhesh Jog, Raja SP. |
| Blog: *Building with AI-DLC using Amazon Q Developer* — [origen](https://aws.amazon.com/blogs/devops/building-with-ai-dlc-using-amazon-q-developer/) | [`blog-03`](../fuentes/blogs/2025-11-29_building-with-ai-dlc-using-amazon-q-developer.md) | 2025-11-29 | Walkthrough práctico sobre Q Developer. |
| Blog: *AI-Driven Development Lifecycle for Financial Services* — [origen](https://aws.amazon.com/blogs/industries/ai-driven-development-lifecycle-for-financial-services/) | [`blog-04`](../fuentes/blogs/2026-05-26_ai-driven-development-lifecycle-for-financial-services.md) | 2026-05-26 | **El más útil para entorno regulado**: steering files que codifican política antes de generar, más trazabilidad requisito→test. |
| Sitio de documentación v2 — [origen](https://awslabs.github.io/aidlc-workflows/) | [`../aidlc-v2/docs/`](../aidlc-v2/docs/) · índice en [05](05-mapa-docs-v2.md) | vigente | Las tres guías. Mismo contenido que `aidlc-v2/docs/`. |
| Roadmap — [origen](https://awslabs.github.io/aidlc-workflows/roadmap.html) | [`../aidlc-v2/docs/roadmap.md`](../aidlc-v2/docs/roadmap.md) | 2026-08-10 | Qué salió, qué está en vuelo, qué está planeado. Fuente de §3 del doc 03. |
| **Whitepaper: AI-DLC Workflows 2.0 Specification** (PDF, 6 pp.) | [PDF](../aidlc-v2/assets/AI-DLC-Workflows-2.0-Specification.pdf) · [texto](../fuentes/especificacion/aidlc-workflows-2.0-specification-texto.md) | 2026 | **La fuente clave de v2.** Los 9 principios, la estructura y el orquestador. Resumido abajo. |
| Repo — [origen](https://github.com/awslabs/aidlc-workflows/tree/v2) | [`../aidlc-v2/`](../aidlc-v2/) | vigente | Implementación. Licencia MIT-0. |

> **Hallazgo:** *no existe blog post oficial de AWS dedicado a v2 / 2.0 GA.* El anuncio de GA vive en el README del repo y en el whitepaper PDF. Los blogs de AWS indexados siguen describiendo v1. Si un documento cita «el blog de AWS» para justificar v2, la cita correcta es el whitepaper, no un blog.

## 2. Terceros

| Fuente | Copia local | Qué aporta |
|---|---|---|
| DevelopersIO — instalación de v2 preview en Kiro CLI / Claude Code / Codex CLI | [`terceros-03`](../fuentes/terceros/03_developersio_instalacion-v2-preview.md) | Verificación en 3 harnesses. Señala los dos escollos reales: `bun` en el PATH y ajustes de usuario de Codex CLI. |
| DevelopersIO — ejecución de v2.5.5 ya GA con Kiro CLI | [`terceros-04`](../fuentes/terceros/04_developersio_ejecucion-v2-ga-kiro.md) | Corrida real hasta intent-capture; `--doctor` con 39 checks pasando. |
| ELEKS — *AI-DLC Explained* | [`terceros-02`](../fuentes/terceros/02_eleks_ai-dlc-explained.md) | Lectura de consultora, nivel conceptual. |
| exploreagentic.ai — *AI-DLC Explained* | [`terceros-01`](../fuentes/terceros/01_exploreagentic_ai-dlc-explained.md) | Idem, útil para contrastar narrativa. |

---

## 3. Línea de tiempo

| Versión | Fecha | Hito |
|---|---|---|
| v1 | 2025-11-29 | Open source como rules de Q Developer y steering files de Kiro. 3 fases. |
| 0.1.0 (v2 dev) | 2026-04-24 | Primer commit versionado de la rama v2. |
| **2.0.0** | **2026-06-18** | v2 en **preview**. Reviewer opcional por etapa + harness Kiro IDE. Roster 11 → 13 agentes. |
| 2.2.0 | 2026-07-04 | Adaptive Workflows: `aidlc-composer-agent` y `/aidlc compose`. |
| **2.3.0** | **2026-07-07** | Corte donde se declara **GA**. Mecanismo de plugins. |
| 2.5.5 | 2026-07-22 | La versión que reseña DevelopersIO tras GA. |
| 2.6.18 | 2026-08-19 | HEAD clonado. Scopes classic/express, módulos de protocolo condicionales. |
| **2.6.54** | **2026-08-21** | Snapshot actual del repositorio. 23 commits en dos días: casi todo correcciones. Dos de fondo: bucle acotado de vuelta de Build&Test a generación de código (2.6.20) y cursor de continuación atómico en el motor (2.6.51). **Ninguno mueve la estructura.** |

187 entradas de CHANGELOG en cuatro meses. **Conviene fijar una versión** en cualquier documento que dependa de esto — el propio README lo pide: *«pin a known-good version for anything you depend on»*.

---

## 4. El whitepaper 2.0 — los 9 principios

Punto de partida declarado: *v1 demostró el valor de correr el SDLC como secuencia de etapas con humano en el loop; **v2 conserva la metodología y reconstruye la capa de workflow para avanzar progresivamente hacia entrega autónoma**, reduciendo la intervención humana a medida que se amplía la verificación comprobable por máquina.*

Dos fuerzas motivaron el rediseño: los clientes pedían bloques componibles de grano más fino, y la plataforma de agentes maduró — Skills y runtimes multi-agente permiten expresar esa granularidad de forma nativa, no solo con steering rules.

1. **El juicio humano se puede destilar en máquinas.** Codificar patrones de decisión en constructos ejecutables. No se afirma que el humano desaparezca; se afirma el imperativo de bajar el esfuerzo humano en cada etapa.
2. **Todo intent nace ambiguo, y está bien.** La IA debe preguntar antes de asumir.
3. **IA como solver auto-corrector, con red de seguridad.** Requiere tres propiedades: post-condiciones verificables por un programa que la IA *no pueda modificar*, criterio de éxito tratable, iteración barata. **Todo self-correcting loop lleva condición de parada**; si no converge, escala al humano.
4. **Modelo de tres compartimentos** (Generate–Verify–Learn):
   - **C1 — el «qué»**: inputs, outputs y artefactos intermedios obligatorios, declarativos.
   - **C2 — el «cómo sabemos que está bien»**: post-condiciones. *Inferential* (reglas LLM) y *Computational* (ejecutables, para lo que exige determinismo).
   - **C3 — el «qué aprendimos»**: qué señales de runtime se vuelven candidatas a regla.
5. **Toda etapa del SDLC encaja en el constructo.**
6. **Descomposición por etapas antes que compresión de un solo tiro.** *«Nuestras definiciones de etapa prescriptivas resultaron demasiado opinadas, y ahí surgió la fricción de adopción»*. De ahí las **Skills** como unidad de composición.
7. **Autonomía en incrementos seguros, no big-bang.** Hidratar C2 incrementalmente.
8. **Extensibilidad como restricción de diseño**: aditivas, por reemplazo, y composición de etapas nuevas.
9. **Aprender de la práctica.** Cada corrección humana es candidata a regla, con aprobación antes de promoverse.

**Salvaguarda:** una etapa cuyo C2 contiene *solo* post-condiciones juzgadas por LLM **no se auto-detiene**. Solo al destilar verificaciones en ejecutables deterministas crece la proporción de etapas que pueden hacerlo.

**Estructura (§3):** librería de agentes-persona · librería de etapas · librería de conocimiento · orquestador · package manager.

**El orquestador (§4)** cumple cinco funciones: propiedad del objetivo, composición del workflow, routing/observabilidad/control, frontera de abstracción (cada etapa es caja negra), invariantes cross-stage. *«No sigue un pipeline rígido. Mantiene un plan, pero ese plan es mutable.»*

**Guidelines (§6):** routing determinista · especialización de agentes · trazabilidad de artefactos · aprobación humana en etapas no-bootstrap · estado propiedad de la herramienta · verificación consultiva · aprendizaje controlado · **sin delegación oculta**.
