# Tried running the newly GA'd AI-DLC Workflows v2.5.5 with Kiro CLI | DevelopersIO

> **Fuente:** DevelopersIO (Classmethod)
> **URL:** https://dev.classmethod.jp/en/articles/aidlc-workflows-v2-ga-kiro-cli/
> **Descargado:** 2026-08-19

---

## Introduction

We published a preview article for AI-DLC Workflows v2.0.0 in June 2026. About five weeks later, v2.0 reached GA.

<https://dev.classmethod.jp/articles/aidlc-workflows-v2-install-kiro-claude-codex/>

The current version v2.5.5 is the latest release, incorporating minor updates since GA.

<https://github.com/awslabs/aidlc-workflows#-announcing-20-ga>

<https://x.com/masaosaan/status/2079946093039886800>

In this article, we use `dist/kiro/` from v2.5.5 to launch a workflow with Kiro CLI and verify operation up to the question generation and answer mode presentation in the intent-capture stage.

## Verification Details

### Verification Environment

| Item | Value |
| --- | --- |
| Kiro CLI | 2.13.1 |
| AI-DLC Workflows | v2.5.5 |
| Conductor Model | claude-opus-4.6 |
| Sub-agent Model | claude-sonnet-4.6 |
| bun | Kiro CLI built-in version (used by adding to PATH) |
| Launch Method | Using pre-built dist/kiro/ |

The AI-DLC defaults are claude-opus-4.8 for the conductor and claude-sonnet-4.5 for the sub-agent. In the author's environment, the `defaultModel` in `cli.json` and each agent definition were modified to evaluate with the opus-4.6 / sonnet-4.6 combination.

Since `dist/` is committed as pre-built, it can be placed simply by cloning and copying.

```
git clone -b v2 https://github.com/awslabs/aidlc-workflows.git /tmp/aidlc-v2
cp -r /tmp/aidlc-v2/dist/kiro/.kiro <project>/.kiro
cp -r /tmp/aidlc-v2/dist/kiro/aidlc <project>/aidlc
cp /tmp/aidlc-v2/dist/kiro/AGENTS.md <project>/AGENTS.md
```

### Major Changes from v2.0.0 → v2.5.5

The structural changes from v2.0.0 to v2.5.5 are as follows.

| Item | v2.0.0 | v2.5.5 |
| --- | --- | --- |
| Number of Stages | 32 | 32 |
| Number of Agents | 13 | 14 (+composer) |
| Number of Harnesses | 4 | 5 (+opencode) |
| Audit events | 67 | 74 |
| Number of Scopes | 9 | 9 |
| Stage modes | 2 (inline, subagent) | 4 (+pipeline, +mob) |

Key new features are listed below.

* **Adaptive Workflows (v2.2.0)** The composer agent can now infer scope from natural language input and dynamically generate EXECUTE/SKIP grids
* **Plugin Mechanism (v2.3.0)** A mechanism for defining extended stages and contributions in the `plugins/` directory was added
* **opencode Harness (v2.4.6)** Support for opencode.ai was added as the fifth harness
* **3-Role Ensemble (v2.5.0)** Collaborator separation via `pipeline`/`mob` modes and contribution files were introduced

Summary of Changes by Major Version

| Version | Date | Overview |
| --- | --- | --- |
| 2.1.0 | 06-24 | Full workspace overhaul: `aidlc-docs/` → `aidlc/spaces/default/intents/`. Per-intent layout, spaces/intents/multi-repo |
| 2.2.0 | 07-04 | Adaptive Workflows: composer agent (14th). Automatic scope selection via NL keyword inference, dynamic EXECUTE/SKIP grid generation |
| 2.3.0 | 07-07 | Plugin mechanism: extended stage and contribution definitions via `plugins/` |
| 2.5.0 | 07-17 | 3-role ensemble: `pipeline`/`mob` modes. Collaborator separation, contribution files |

### Running doctor

After placement, running `/aidlc --doctor` resulted in `39 passed, 0 failed`.

Full doctor Output

```
AI-DLC Health Check
─────────────────────────────────────
✓  bun installed (required for CLI tools and hooks)
✓  aidlc-audit-logger.ts present
✓  aidlc-sync-statusline.ts present
✓  aidlc-validate-state.ts present
✓  aidlc-log-subagent.ts present
✓  aidlc-session-start.ts present
✓  aidlc-session-end.ts present
✓  aidlc-statusline.ts present
✓  aidlc-kiro-adapter.ts present
✓  agents/aidlc.json present (hook + permission wiring)
✓  settings/cli.json present (workspace default-agent activation)
✓  AWS_AIDLC_DEFAULT_SCOPE (unset — no project default)
✓  Enabled plugins: all enabled (no selection); enabled stage counts: aidlc=29, bootstrap=3
✓  Plugin selection flags: harness.json agrees with stage-graph.json
✓  Enabled stage compile coverage: every enabled stage file is in the full graph
✓  workspace shell ready (.kiro/ + aidlc/spaces/default/memory/)
✓  Agent filename/name consistency: all agent files match declared names
✓  Scope filename/name consistency: all scope files match declared names
✓  Submodules: no .gitmodules at workspace root
✓  Hooks last fired: ...
✓  Hook drops: none recorded
✓  Audit locks: none leaked
✓  State Version: 7
✓  Orphan worktrees: 0 observed
✓  Stale branches: 0 (0 bolt-* observed)
✓  Orphan state files: 0 observed
✓  Orphan audit: 0 observed
✓  Practices staleness: never affirmed (informational)
✓  MERGE_DISPATCH: 0 orphan INVOKED (0 bracketed)
✓  Cycle detection: 0 cycles
✓  Orphan stage files: 32 graph entries all have files
✓  Uncompiled stage files: 0 stage files missing from the compiled graph
✓  Scope validation: 9 scopes valid (27 advisories)
✓  Schema validation: 32/32 stages validated
✓  Graph references: 122 artifacts + edges resolved
✓  Keyword overlap: no conflicts
✓  Rule drift: no team/project rule overlaps org policy
✓  Paired sensor coverage: no sensor-bound rules (0 feedforward-only)
✓  Intent registry: all rows ⇄ record dirs reconciled
─────────────────────────────────────
39 passed, 0 failed
```

### Launching the Workflow

We launched the workflow using a calculator app as the subject.

```
/aidlc "シンプルな電卓Webアプリを作りたい"
```

The AI-DLC workflow engine presented scope options.

```
How would you like to proceed?

- compose  — Compose a tailored workflow (adaptive)
- mvp      — Skip operations, ship the core
- feature  — New feature, practical depth
- poc      — Proof of concept (8/32 stages)
- (other scopes available)
```

To verify the entry point with a minimal configuration, we selected `poc` (8/32 stages). intent-birth was executed and the workflow record was created.

```
intent-birth --scope poc --arguments "シンプルな電卓Webアプリを作りたい" --label "simple-calc"
Record created: aidlc/spaces/default/intents/260722-simple-calc/
```

The intent-capture stage then began, and the question file was generated.

```
Generated: intent-capture-questions.md (3 questions, PoC scope minimal depth)

Q1: Calculator purpose (for learning or practical use)
Q2: Supported operations (basic arithmetic only or scientific calculator)
Q3: Target users (developer themselves or end users)

Select answer mode:
- Guide me (interactive Q&A)
- I'll edit the file (direct edit)
- Chat (freeform conversation)
```

Verification was stopped at this point. We confirmed that the intent-capture stage operates correctly up to question generation and answer mode presentation.

## Summary

AI-DLC Workflows v2.5.5 worked immediately on Kiro CLI with just a copy from dist/. The v2 architecture, Harness Engineering design philosophy, and usage are explained in detail in the article below, so we recommend reading it before evaluation.

<https://zenn.dev/aws_japan/articles/aidlc-workflows-v2-harness-engineering>
