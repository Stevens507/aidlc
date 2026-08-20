# Fuentes oficiales de AWS sobre AI-DLC

Todo el material de este directorio fue descargado de fuentes oficiales de AWS el 14 de agosto de 2026. Es la base documental para redactar el documento de metodología del área.

## Fuentes canónicas (la metodología)

| Fuente | Fecha | Dónde está | Original |
|---|---|---|---|
| **Method Definition Paper** — Raja SP. El white paper que define el método: mental model, fases, rituales, artefactos, los diez principios. 8 páginas. | jul 2025 | `paper/aidlc-method-definition-paper.pdf` (+ texto extraído en `-texto.md`) | [amplifyapp.com](https://prod.d13rzhkk8cj2z0.amplifyapp.com/) (sirve el PDF en `/aidlc.pdf`) |
| **Blog de lanzamiento** — "AI-Driven Development Life Cycle: Reimagining Software Engineering", Raja SP, AWS DevOps Blog. Presenta el método: por qué, mental model, Inception/Construction/Operations, Mob Elaboration/Construction, Bolts. | 31 jul 2025 | `blogs/2025-07-31_ai-driven-development-life-cycle.md` | [aws.amazon.com](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) |
| **Blog práctico** — "Building with AI-DLC using Amazon Q Developer", Will Matos, Raj Jain, Siddhesh Jog y Raja SP. El método aplicado paso a paso con Project Rules; publicado en la semana de re:Invent 2025. | 29 nov 2025 | `blogs/2025-11-29_building-with-ai-dlc-using-amazon-q-developer.md` | [aws.amazon.com](https://aws.amazon.com/blogs/devops/building-with-ai-dlc-using-amazon-q-developer/) |
| **Adaptación a servicios financieros** — "AI-Driven Development Lifecycle for Financial Services", AWS for Industries. El método en entornos regulados: controles, cumplimiento, evidencia. Relevante para nuestros clientes de banca y sector público. | 26 may 2026 | `blogs/2026-05-26_ai-driven-development-lifecycle-for-financial-services.md` | [aws.amazon.com](https://aws.amazon.com/blogs/industries/ai-driven-development-lifecycle-for-financial-services/) |
| **Blog del código abierto** — "Open-Sourcing Adaptive Workflows for AI-DLC", Will Matos, Raj Jain, Siddhesh Jog y Raja SP. El anuncio de la apertura del código. | 29 nov 2025 | `blogs/2025-11-29_open-sourcing-adaptive-workflows.md` | [aws.amazon.com](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/) |
| **Especificación AI-DLC Workflows 2.0** — el whitepaper técnico de la implementación 2.0 (GA). 6 páginas. | 2026 | `especificacion/AI-DLC-Workflows-2.0-Specification.pdf` (+ `-texto.md`) | [github.com/awslabs/aidlc-workflows (v2)](https://github.com/awslabs/aidlc-workflows/blob/v2/assets/AI-DLC-Workflows-2.0-Specification.pdf) |

AWS presentó el método en re:Invent en diciembre de 2025 (sesión DVT214, "Introducing AI-Driven Development Lifecycle").

## Repositorio oficial: `awslabs/aidlc-workflows` (licencia MIT-0)

Snapshot del 14 ago 2026, sin historial git.

- `repo-oficial/main/` — rama `main`: las **reglas AI-DLC v1** (`aidlc-rules/` 1.0.1): reglas core y detalladas por fase (inception, construction, operations), extensiones (security, resiliency, testing) e instrucciones de instalación para Kiro, Amazon Q Developer, Cursor, Cline, Claude Code, Copilot y Codex.
- `repo-oficial/v2/` — rama `v2`: la **implementación 2.0 GA** (versión 2.6.2): 5 fases y 33 etapas (Initialization, Ideation, Inception, Construction, Operation), roster de 14 agentes, 9 scopes adaptativos, núcleo neutral en `core/` con superficies por herramienta en `harness/`. La documentación de uso está en `v2/docs/guide/`.
- Excluido del snapshot v2 por peso: `dist/` (artefactos compilados), `tests/` y `uv.lock`. Si hacen falta: `git clone -b v2 https://github.com/awslabs/aidlc-workflows`.

**Sobre las 3 fases del paper y las 5 de la implementación:** ya está estudiado y no son dos metodologías. Las 5 son las 3 del paper con Inception partida en dos (`ideation` + `inception`) y una fase 0 de fontanería delante. El detalle, con la trampa que esconde la palabra «Inception», en [`../conocimiento/LEEME.md`](../conocimiento/LEEME.md).

**Ojo con la versión del snapshot:** el `repo-oficial/v2/` de aquí es la **2.6.2**. El estudio de `../conocimiento/` se hizo contra la **2.6.18**, que añade dos scopes (`aidlc-classic` y `aidlc-express`, 9 → 11). Todo lo demás coincide.

## Casos publicados en blogs regionales oficiales de AWS

Experiencias reales de adopción; útiles como evidencia de resultados y patrones de adopción, no como definición del método. En su idioma original.

| Archivo | Caso |
|---|---|
| `blogs-regionales/jp_joint-ai-dlc-unicorn-gym-202601.md` | Japón: Unicorn Gym conjunto de AI-DLC (ene 2026) |
| `blogs-regionales/jp_ai-dlc-unicorn-gym-hitachi-ics-202601.md` | Japón: Hitachi ICS, primer AI-DLC del grupo Hitachi: 3 meses-persona en 2 días |
| `blogs-regionales/jp_joint-ai-dlc-unicorn-gym-202606.md` | Japón: Unicorn Gym de 9 empresas (jun 2026) |
| `blogs-regionales/jp_joint-ai-dlc-unicorn-gym-isv-202607.md` | Japón: Unicorn Gym de 8 ISV SaaS (jul 2026) |
| `blogs-regionales/jp_astemo-ai-dlc.md` | Japón: Astemo, adopción a escala de toda la plantilla |
| `blogs-regionales/ko_aws-aidlc-woongjinthinkbig-tech-blog.md` | Corea: Woongjin ThinkBig, agente de curaduría de libros construido con AI-DLC |
| `blogs-regionales/ko_aidlc-armiq-subagent-customskills.md` | Corea: Armiq, AI-DLC extendido con subagentes y custom skills en proyecto de equipo |
| `blogs-regionales/cn_apache-seatunnel-aidlc-practice.md` | China: práctica de AI-DLC en Apache SeaTunnel |
| `blogs-regionales/cn_ai-engineering-platform-aidlc-migration.md` | China: migración de ingeniería de datos de plataforma a AI-DLC |

## Lecturas de terceros

No definen el método; sirven para contrastar cómo lo cuenta alguien de fuera y para ver corridas reales de la 2.0.

| Archivo | Qué aporta |
|---|---|
| `terceros/01_exploreagentic_ai-dlc-explained.md` | Lectura conceptual, útil para contrastar narrativa |
| `terceros/02_eleks_ai-dlc-explained.md` | Lectura de consultora, nivel conceptual |
| `terceros/03_developersio_instalacion-v2-preview.md` | Instalación de la 2.0 preview verificada en tres harnesses. Señala los dos escollos reales: `bun` en el PATH y los ajustes de usuario de Codex CLI |
| `terceros/04_developersio_ejecucion-v2-ga-kiro.md` | Corrida real de la 2.5.5 GA con Kiro CLI, hasta intent-capture |

## Notas de procedencia

- Los `.md` de blogs se convirtieron del HTML original; las imágenes siguen apuntando a las URL de CloudFront de AWS.
- `blogs/imagenes/` guarda un **espejo local parcial** de esas imágenes (17 archivos, descargados el 19 ago 2026), por si AWS rota el CDN. Es parcial: no cubre todas las que citan los blogs. Los `.md` siguen apuntando al original.
- Los `-texto.md` junto a cada PDF son extracciones de texto plano para buscar y citar; ante cualquier duda, manda el PDF.
