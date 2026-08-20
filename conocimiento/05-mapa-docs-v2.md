# Mapa de la documentación de v2

Índice de los **95 archivos / 24.718 líneas** de documentación que trae [`../aidlc-v2/`](../aidlc-v2/). Ninguno de estos archivos es mío: son de AWS, y están intactos en el clon.

Ver también: [01 fuentes](01-fuentes.md) - [02 como funciona](02-como-funciona.md) - [03 que falta](03-que-falta.md) - [04 v1 vs v2](04-v1-vs-v2.md)

---

## Las tres guías, una por lector

| Guía | Eres… | Cambias… |
|---|---|---|
| **User Guide** (`docs/guide/`) | quien construye software *con* AI-DLC | nada del framework - corres `/aidlc`, respondes en compuertas, revisas artefactos |
| **Harness Engineer Guide** (`docs/harness-engineering/`) | quien re-forma *cómo se comporta* para su equipo | los **datos**: etapas, agentes, scopes, reglas, sensores, conocimiento |
| **Developer Reference** (`docs/reference/`) | quien cambia AI-DLC *mismo* | el **código** que lee esos datos |

> La línea entre las dos últimas es **dato versus código**. La línea entre la primera y el resto es **usar versus dar forma**.

### Por dónde entrar

- **Entender el método sin implementarlo** -> `assets/AI-DLC-Workflows-2.0-Specification.pdf` (6 pp.) y luego `docs/guide/00-introduction.md`.
- **Adaptarlo a un equipo** -> `docs/harness-engineering/00-overview.md`, y de ahí a plantillas, reglas y sensores.
- **Entender por qué funciona así** -> `docs/reference/02-plane-architecture.md` primero, luego `01-architecture.md` y `03-orchestrator.md`.
- **Qué hay pendiente** -> `docs/roadmap.md`.

---

## Raíz de la documentación

`docs` - 2 archivos, 268 líneas

| Líneas | Archivo | Qué cubre |
|---:|---|---|
| 39 | [`README.md`](../aidlc-v2/docs/README.md) | AI-DLC Documentation |
| 229 | [`roadmap.md`](../aidlc-v2/docs/roadmap.md) | AI-DLC Workflows 2.0 - Roadmap |

## **User Guide** — construir *con* AI-DLC

`docs/guide` - 20 archivos, 6170 líneas

| Líneas | Archivo | Qué cubre |
|---:|---|---|
| 81 | [`00-introduction.md`](../aidlc-v2/docs/guide/00-introduction.md) | Introduction |
| 414 | [`01-getting-started.md`](../aidlc-v2/docs/guide/01-getting-started.md) | Getting Started |
| 293 | [`02-your-first-workflow.md`](../aidlc-v2/docs/guide/02-your-first-workflow.md) | Your First Workflow |
| 318 | [`03-spaces-and-intents.md`](../aidlc-v2/docs/guide/03-spaces-and-intents.md) | Spaces and Intents |
| 431 | [`04-phases-and-stages.md`](../aidlc-v2/docs/guide/04-phases-and-stages.md) | Phases and Stages |
| 435 | [`05-scopes-and-depth.md`](../aidlc-v2/docs/guide/05-scopes-and-depth.md) | Scopes, Depth, and Test Strategy |
| 319 | [`06-agents.md`](../aidlc-v2/docs/guide/06-agents.md) | Agents |
| 214 | [`07-interaction-modes.md`](../aidlc-v2/docs/guide/07-interaction-modes.md) | Interaction Modes |
| 397 | [`08-knowledge.md`](../aidlc-v2/docs/guide/08-knowledge.md) | Knowledge |
| 187 | [`09-rules-and-the-learning-loop.md`](../aidlc-v2/docs/guide/09-rules-and-the-learning-loop.md) | Rules and the Learning Loop |
| 181 | [`10-state-and-audit.md`](../aidlc-v2/docs/guide/10-state-and-audit.md) | State Tracking and Audit Trail |
| 176 | [`11-session-management.md`](../aidlc-v2/docs/guide/11-session-management.md) | Session Management |
| 932 | [`12-cli-commands.md`](../aidlc-v2/docs/guide/12-cli-commands.md) | CLI Commands |
| 236 | [`13-customization.md`](../aidlc-v2/docs/guide/13-customization.md) | Customization |
| 289 | [`14-artifacts-reference.md`](../aidlc-v2/docs/guide/14-artifacts-reference.md) | Artifacts Reference |
| 276 | [`15-troubleshooting.md`](../aidlc-v2/docs/guide/15-troubleshooting.md) | Troubleshooting |
| 393 | [`16-worked-examples.md`](../aidlc-v2/docs/guide/16-worked-examples.md) | Worked Examples |
| 170 | [`17-skills.md`](../aidlc-v2/docs/guide/17-skills.md) | Skills and Runner Commands |
| 70 | [`glossary.md`](../aidlc-v2/docs/guide/glossary.md) | Glossary |
| 358 | [`workshop-mode.md`](../aidlc-v2/docs/guide/workshop-mode.md) | Workshop Mode |

## User Guide · por harness

`docs/guide/harnesses` - 7 archivos, 1087 líneas

| Líneas | Archivo | Qué cubre |
|---:|---|---|
| 33 | [`README.md`](../aidlc-v2/docs/guide/harnesses/README.md) | Running on other harnesses |
| 171 | [`codex-cli.md`](../aidlc-v2/docs/guide/harnesses/codex-cli.md) | AI-DLC on Codex CLI |
| 194 | [`copilot.md`](../aidlc-v2/docs/guide/harnesses/copilot.md) | AI-DLC on GitHub Copilot (CLI + VS Code) |
| 198 | [`cursor.md`](../aidlc-v2/docs/guide/harnesses/cursor.md) | AI-DLC on Cursor |
| 150 | [`kiro-cli.md`](../aidlc-v2/docs/guide/harnesses/kiro-cli.md) | Running AI-DLC on Kiro CLI |
| 220 | [`kiro-ide.md`](../aidlc-v2/docs/guide/harnesses/kiro-ide.md) | Running AI-DLC on Kiro IDE |
| 121 | [`opencode.md`](../aidlc-v2/docs/guide/harnesses/opencode.md) | AI-DLC on opencode |

## User Guide · fichas de agente

`docs/guide/agents` - 12 archivos, 466 líneas

| Líneas | Archivo | Qué cubre |
|---:|---|---|
| 31 | [`README.md`](../aidlc-v2/docs/guide/agents/README.md) | Agent Deep Dives |
| 46 | [`architect-agent.md`](../aidlc-v2/docs/guide/agents/architect-agent.md) | Architect Agent |
| 39 | [`aws-platform-agent.md`](../aidlc-v2/docs/guide/agents/aws-platform-agent.md) | AWS Platform Agent |
| 36 | [`compliance-agent.md`](../aidlc-v2/docs/guide/agents/compliance-agent.md) | Compliance Agent |
| 38 | [`delivery-agent.md`](../aidlc-v2/docs/guide/agents/delivery-agent.md) | Delivery Agent |
| 37 | [`design-agent.md`](../aidlc-v2/docs/guide/agents/design-agent.md) | Design Agent |
| 44 | [`developer-agent.md`](../aidlc-v2/docs/guide/agents/developer-agent.md) | Developer Agent |
| 38 | [`devsecops-agent.md`](../aidlc-v2/docs/guide/agents/devsecops-agent.md) | DevSecOps Agent |
| 40 | [`operations-agent.md`](../aidlc-v2/docs/guide/agents/operations-agent.md) | Operations Agent |
| 36 | [`pipeline-deploy-agent.md`](../aidlc-v2/docs/guide/agents/pipeline-deploy-agent.md) | Pipeline & Deploy Agent |
| 41 | [`product-agent.md`](../aidlc-v2/docs/guide/agents/product-agent.md) | Product Agent |
| 40 | [`quality-agent.md`](../aidlc-v2/docs/guide/agents/quality-agent.md) | Quality Agent |

## **Harness Engineer Guide** — re-formar el comportamiento (datos, sin código)

`docs/harness-engineering` - 11 archivos, 2522 líneas

| Líneas | Archivo | Qué cubre |
|---:|---|---|
| 198 | [`00-overview.md`](../aidlc-v2/docs/harness-engineering/00-overview.md) | Harness Engineer Guide |
| 104 | [`01-anatomy-of-a-stage.md`](../aidlc-v2/docs/harness-engineering/01-anatomy-of-a-stage.md) | Anatomy of a Stage |
| 312 | [`02-adding-a-stage.md`](../aidlc-v2/docs/harness-engineering/02-adding-a-stage.md) | Adding a Stage |
| 222 | [`03-adding-an-agent.md`](../aidlc-v2/docs/harness-engineering/03-adding-an-agent.md) | Adding an Agent |
| 154 | [`04-scopes.md`](../aidlc-v2/docs/harness-engineering/04-scopes.md) | Scopes |
| 192 | [`05-rules-and-the-loop.md`](../aidlc-v2/docs/harness-engineering/05-rules-and-the-loop.md) | Rules and the Learning Loop |
| 223 | [`06-sensors.md`](../aidlc-v2/docs/harness-engineering/06-sensors.md) | Sensors |
| 211 | [`07-team-knowledge.md`](../aidlc-v2/docs/harness-engineering/07-team-knowledge.md) | Team Knowledge |
| 295 | [`08-construction-and-swarm.md`](../aidlc-v2/docs/harness-engineering/08-construction-and-swarm.md) | Construction and the Swarm |
| 181 | [`09-porting-to-a-new-harness.md`](../aidlc-v2/docs/harness-engineering/09-porting-to-a-new-harness.md) | Porting AI-DLC to a New Harness |
| 430 | [`10-authoring-a-plugin.md`](../aidlc-v2/docs/harness-engineering/10-authoring-a-plugin.md) | Authoring a Plugin |

## **Developer Reference** — cambiar AI-DLC *mismo* (código)

`docs/reference` - 21 archivos, 8922 líneas

| Líneas | Archivo | Qué cubre |
|---:|---|---|
| 62 | [`00-overview.md`](../aidlc-v2/docs/reference/00-overview.md) | Developer Reference Overview |
| 545 | [`01-architecture.md`](../aidlc-v2/docs/reference/01-architecture.md) | Architecture |
| 351 | [`02-plane-architecture.md`](../aidlc-v2/docs/reference/02-plane-architecture.md) | Plane Architecture |
| 850 | [`03-orchestrator.md`](../aidlc-v2/docs/reference/03-orchestrator.md) | Orchestrator |
| 1134 | [`04-stage-protocol.md`](../aidlc-v2/docs/reference/04-stage-protocol.md) | Stage Protocol Reference |
| 194 | [`05-agent-system.md`](../aidlc-v2/docs/reference/05-agent-system.md) | Agent System |
| 771 | [`06-hooks-and-tools.md`](../aidlc-v2/docs/reference/06-hooks-and-tools.md) | Hooks and Tools |
| 407 | [`07-sensor-system.md`](../aidlc-v2/docs/reference/07-sensor-system.md) | Sensor System |
| 111 | [`08-rule-system.md`](../aidlc-v2/docs/reference/08-rule-system.md) | Rule System |
| 379 | [`09-testing.md`](../aidlc-v2/docs/reference/09-testing.md) | Testing |
| 224 | [`10-knowledge-system.md`](../aidlc-v2/docs/reference/10-knowledge-system.md) | Knowledge System |
| 279 | [`11-contributing.md`](../aidlc-v2/docs/reference/11-contributing.md) | Contributing |
| 521 | [`12-state-machine.md`](../aidlc-v2/docs/reference/12-state-machine.md) | State Machine |
| 497 | [`13-runtime-graph.md`](../aidlc-v2/docs/reference/13-runtime-graph.md) | Runtime Graph |
| 392 | [`14-claude-features.md`](../aidlc-v2/docs/reference/14-claude-features.md) | Harness Primitives Mapping |
| 552 | [`15-stage-definition.md`](../aidlc-v2/docs/reference/15-stage-definition.md) | Stage Definition |
| 273 | [`16-artifact-vocabulary.md`](../aidlc-v2/docs/reference/16-artifact-vocabulary.md) | Artifact Vocabulary |
| 153 | [`17-skill-system.md`](../aidlc-v2/docs/reference/17-skill-system.md) | The Orchestration Engine and Skill System |
| 425 | [`18-plugin-mechanism.md`](../aidlc-v2/docs/reference/18-plugin-mechanism.md) | The Plugin Mechanism |
| 667 | [`diagrams.md`](../aidlc-v2/docs/reference/diagrams.md) | AI-DLC Workflow Diagrams |
| 135 | [`kiro-ide-hook-payload.md`](../aidlc-v2/docs/reference/kiro-ide-hook-payload.md) | Kiro IDE hook payload — empirical reference |

## Developer Reference · etapas por fase

`docs/reference/04-stages` - 5 archivos, 3355 líneas

| Líneas | Archivo | Qué cubre |
|---:|---|---|
| 1131 | [`construction.md`](../aidlc-v2/docs/reference/04-stages/construction.md) | Construction Phase -- Stage Reference (3.1-3.7) |
| 400 | [`ideation.md`](../aidlc-v2/docs/reference/04-stages/ideation.md) | Ideation Phase -- Stage Reference (1.1-1.7) |
| 1354 | [`inception.md`](../aidlc-v2/docs/reference/04-stages/inception.md) | Inception Phase -- Stage Reference (2.1--2.9) |
| 171 | [`initialization.md`](../aidlc-v2/docs/reference/04-stages/initialization.md) | Initialization Phase Stages (0.1-0.3) |
| 299 | [`operation.md`](../aidlc-v2/docs/reference/04-stages/operation.md) | Operation Phase -- Stage Reference (4.1-4.7) |

## Developer Reference · agentes

`docs/reference/agents` - 12 archivos, 1173 líneas

| Líneas | Archivo | Qué cubre |
|---:|---|---|
| 274 | [`README.md`](../aidlc-v2/docs/reference/agents/README.md) | Agent Reference |
| 92 | [`architect-agent.md`](../aidlc-v2/docs/reference/agents/architect-agent.md) | aidlc-architect-agent -- Technical Reference |
| 80 | [`aws-platform-agent.md`](../aidlc-v2/docs/reference/agents/aws-platform-agent.md) | aidlc-aws-platform-agent -- Technical Reference |
| 82 | [`compliance-agent.md`](../aidlc-v2/docs/reference/agents/compliance-agent.md) | aidlc-compliance-agent -- Technical Reference |
| 78 | [`delivery-agent.md`](../aidlc-v2/docs/reference/agents/delivery-agent.md) | aidlc-delivery-agent -- Technical Reference |
| 79 | [`design-agent.md`](../aidlc-v2/docs/reference/agents/design-agent.md) | aidlc-design-agent -- Technical Reference |
| 82 | [`developer-agent.md`](../aidlc-v2/docs/reference/agents/developer-agent.md) | aidlc-developer-agent -- Technical Reference |
| 80 | [`devsecops-agent.md`](../aidlc-v2/docs/reference/agents/devsecops-agent.md) | aidlc-devsecops-agent -- Technical Reference |
| 80 | [`operations-agent.md`](../aidlc-v2/docs/reference/agents/operations-agent.md) | aidlc-operations-agent -- Technical Reference |
| 78 | [`pipeline-deploy-agent.md`](../aidlc-v2/docs/reference/agents/pipeline-deploy-agent.md) | aidlc-pipeline-deploy-agent -- Technical Reference |
| 88 | [`product-agent.md`](../aidlc-v2/docs/reference/agents/product-agent.md) | aidlc-product-agent -- Technical Reference |
| 80 | [`quality-agent.md`](../aidlc-v2/docs/reference/agents/quality-agent.md) | aidlc-quality-agent -- Technical Reference |

## Developer Reference · plugin de ejemplo

`docs/reference/examples/test-pro` - 1 archivos, 40 líneas

| Líneas | Archivo | Qué cubre |
|---:|---|---|
| 40 | [`README.md`](../aidlc-v2/docs/reference/examples/test-pro/README.md) | `test-pro` — concrete config/JSON examples |

## Developer Reference · investigación

`docs/reference/research` - 2 archivos, 828 líneas

| Líneas | Archivo | Qué cubre |
|---:|---|---|
| 520 | [`Codex Manifest Shape Report.md`](../aidlc-v2/docs/reference/research/Codex Manifest Shape Report.md) | Codex Manifest Shape: How Codex Manages Add-ins |
| 308 | [`Cross-Tool Plugin Comparison.md`](../aidlc-v2/docs/reference/research/Cross-Tool Plugin Comparison.md) | Cross-Tool Plugin Manifest Comparison |

## RFCs y planes de implementación

`docs/rfcs` - 2 archivos, 715 líneas

| Líneas | Archivo | Qué cubre |
|---:|---|---|
| 223 | [`IMPLEMENTATION-PLAN.md`](../aidlc-v2/docs/rfcs/IMPLEMENTATION-PLAN.md) | RFC 0001 Implementation Plan — Design-Stage Rework |
| 492 | [`reviewer-reliability-and-stage-decomposition.md`](../aidlc-v2/docs/rfcs/reviewer-reliability-and-stage-decomposition.md) | RFC: Reviewer Reliability & Stage-Execution Decomposition |

---

**Total mapeado: 25546 líneas.**
