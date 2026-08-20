# AI-DLC Explained: AWS's AI-Driven Development Lifecycle

> **Fuente:** exploreagentic.ai
> **URL:** https://www.exploreagentic.ai/insights/ai-dlc/
> **Descargado:** 2026-08-19

---

AI-DLC — the AI-Driven Development Lifecycle — is AWS's methodology for building software with AI agents doing most of the production work: three phases (Inception, Construction, Operations) run in "bolts," work cycles measured in hours or days instead of two-week sprints, with the team validating every AI-proposed plan before an agent executes it. AWS published it on its DevOps blog in July 2025, open-sourced the workflow rules that November, and presented it at re:Invent 2025 claiming 10-15x productivity gains. The methodology is real. The numbers are AWS's, not yours. And the governance guidance — who signs off on AI-planned work, what evaluation bar agent-written code must clear before production — is where the documentation goes quiet.

Most of what has been written about AI-DLC so far is evangelism. Your SDLC is obsolete, the sprint is dead, adapt or fall behind. Some of that is even true. But your current SDLC quietly embeds a set of controls — peer review, audit trails, release gates — and a lifecycle where the plan, the code, and the tests are machine-generated in the same afternoon dissolves those controls faster than it replaces them. This is the operator's read: what the methodology is, what it looks like with real agents, and the two holes to fill before any of it touches a regulated workload.

## What AI-DLC Is — and What It Thinks Expired

The methodology came out of AWS's developer transformation work; Raja SP published the founding post on the AWS DevOps blog on July 31, 2025. The argument underneath is sharper than the branding suggests. Scrum's rituals — the two-week sprint, the groomed backlog, the standup — are batching mechanisms: human attention is expensive and coordination is slow, so you accumulate work into batches big enough to justify planning them.

Remove that constraint and the batch size stops making sense. When an agent can draft a domain model, an architecture, and a test suite in less time than a sprint-planning meeting takes, a two-week cycle is pure queueing delay. AI-DLC shrinks the cycle to fit the new bottleneck: how fast humans can validate what the AI proposes.

The vocabulary maps over cleanly:

| Traditional SDLC | AI-DLC | What actually changed |
| --- | --- | --- |
| Sprint (2 weeks) | Bolt (hours to days) | The batch shrinks to one validated decision cycle |
| Epic | Unit of work | Scoped so a team finishes it in a handful of bolts |
| Backlog grooming | Mob Elaboration | AI drafts requirements; the whole team interrogates them live |
| Solo author + review queue | Mob Construction | AI drafts design and code; the team validates in real time |

### AWS's numbers, clearly labeled

At re:Invent 2025 (session DVT214) AWS presenters cited 10-15x productivity gains from AI-DLC engagements and described Wipro compressing roughly three months of planned work into about 20 hours — five days of four-hour mob sessions. The same talk carried its own counterweight: measured velocity gains from unstructured AI-assistant adoption sit closer to 10-15 percent. The gap between 15 percent and 15x is, in AWS's telling, the methodology.

Those figures come from AWS and its partners, on engagements AWS helped run. Treat them like any vendor benchmark: directionally interesting, unverified in your context, produced by teams with every incentive to pick amenable projects. Nobody has published the failure cases yet.

## The Independent Numbers, for Contrast

AWS's 10-15x is a vendor figure from vendor-run engagements. The nearest thing to an independent baseline is DORA's annual survey, which in 2025 was devoted specifically to AI-assisted software development. Published 23 September 2025 and drawn from nearly 5,000 technology professionals [[7]](#references)[[8]](#references):

| Finding | Figure |
| --- | --- |
| Professionals using AI at work | 90%, up 14 points year over year |
| Median time spent working with AI | 2 hours per day |
| Report AI has increased their productivity | more than 80% |
| Report a positive effect on code quality | 59% |
| Trust AI-generated code "a great deal" or "a lot" | 24% (4% and 20%) |
| Trust it "a little" or "not at all" | 30% (23% and 7%) |
| Relationship to software delivery throughput | positive — a reversal of the previous year's finding |
| Relationship to software delivery stability | still negative |

Two rows belong in the governance conversation. The first is the trust split: the same population reporting productivity gains above 80% says, 30% against 24%, that it does not much trust what the tool produces. That is not a contradiction — it describes a workflow in which humans are the check — and it is the empirical case for the named approver and the independent evaluation bar below. Mob validation *is* that check, formalised and accelerated; the question governance has to answer is whether the check survives being run at bolt cadence.

The second is the last row. Adoption is now positively associated with delivery throughput, having flipped from the prior year, while its association with delivery *stability* remains negative. If you adopt AI-DLC and instrument only velocity, you are measuring the axis that has already turned in your favour and ignoring the one that has not. Which is why "track defect escape rate next to velocity" appears sixth in the adoption path below and is not the sixth most important item on it.

## The Three Phases, Honestly

### Inception, and what Mob Elaboration really costs

Business intent goes in; requirements, stories, and units of work come out. The AI drafts — asking clarifying questions, proposing requirement sets, decomposing work — and the team validates all of it in a synchronous session AWS calls Mob Elaboration: product, engineering, and QA in one room, reacting to AI-generated questions live.

Done well, this is the strongest idea in the methodology. An agent that interrogates a vague business intent surfaces the ambiguities that normally show up as week-six rework. But notice what it demands: your most senior people, together, synchronously, for hours. The lifecycle spends less on typing and more on senior attention. Nobody puts that in the keynote.

### Construction, and the plan-verify-generate loop

Construction turns the validated context from Inception into architecture, domain models, code, and tests — again AI-drafted, again validated live, in sessions AWS calls Mob Construction. The rhythm is a tight loop: the agent proposes a plan, humans verify, the agent generates, repeat. The agent never executes a plan nobody approved.

### Operations, the thin phase

The AI applies the accumulated context to infrastructure as code, deployment, and monitoring, with team oversight. It is the least developed phase in every AWS artifact we have read — a few paragraphs where Construction gets pages. Platform teams waiting for the methodology to tell them something new will wait a while.

Across all three phases the pattern is identical: AI produces, humans approve, approval is the bottleneck. Which is why governance is not a side conversation here — the approval workflow is the methodology.

## AI-DLC With Real Agents: Kiro, Claude Code, and the Open-Sourced Rules

For its first few months, this was a blog post and a conference deck. That changed on November 29, 2025, when AWS open-sourced the adaptive workflows at [github.com/awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows) under the MIT-0 license — 3,300 GitHub stars at last check.

### What the repo actually contains

Rules files. A central workflow definition plus conditional rules that select stages by project context, adjust depth per phase, and embed the human checkpoints. They install as steering or rules files for Kiro (IDE and CLI), Amazon Q Developer, Cursor, Cline, Claude Code, GitHub Copilot, and OpenAI Codex. AWS-authored, not AWS-locked — a genuinely good call.

### Kiro and the artifact trail

Kiro, AWS's spec-driven agentic IDE, is the natural home: it structurally refuses to generate code until specs exist — a requirements.md, a design.md, and a tasks.md per feature — which happens to be exactly the artifact trail the phases assume. If your team lives in Claude Code instead, the same rules drop in as steering files and the loop feels similar; the tool matters less than the discipline of validated artifacts between phases. For background on how these agents plan and call tools, start with our [agentic AI](/agentic-ai/) pillar; in practice they also need wired access to repos, tickets, and CI — [MCP](/mcp/) territory.

We ran the workflow rules with Claude Code on an internal service to feel out the ceremony. The elaboration pass was genuinely good — the agent asked two scoping questions we had not settled among ourselves. The surprise was the calendar. Mob validation with four people at bolt cadence ate a full afternoon for work a sprint would have spread across two weeks. Faster, yes. Cheaper in senior attention, no.

### Where AI-DLC sits in the build-vs-buy spectrum

AI-DLC is the methodology layer — how a team works with agents. Building the agents themselves is framework territory ([Strands Agents](/insights/strands-agents/) covers AWS's answer); buying packaged agent capacity for business teams starts with [Claude Cowork](/insights/claude-cowork-enterprise/). The methodology assumes the agents exist and answers how humans and agents split the work.

## Governance Hole #1: Who Reviews AI-Planned Work?

Your current SDLC embeds controls so thoroughly that you have stopped seeing them. The pull-request review is a separation-of-duties control. The architecture review board is a risk-acceptance control. The release gate and the change ticket are continuously produced evidence that changes were authorized by someone accountable. None of them was designed for a cadence where plan, code, and tests appear in one afternoon.

### What the AWS material actually says

The founding post says humans "verify and approve before execution proceeds," and that phrase does a lot of load-bearing work. Verify against what standard? Approve with what authority? Recorded where? An instruction to a team is not a control an auditor can test. The open-sourced workflows embed approval checkpoints and log every artifact and decision — useful plumbing — but a repo cannot tell you who is allowed to approve, and it does not try.

AWS knows the question exists. The May 2026 post for financial services is the closest thing to official governance guidance so far: steering files that encode security and regulatory policy before generation, plus end-to-end traceability from requirement to test. Closer. Still silent on the org-chart question — every control is described mechanically, none is assigned to a role.

### Three controls to write down before your first bolt

* **A named approver per unit of work.** A specific human whose sign-off on the AI-drafted plan is recorded — and who is not the person who prompted the plan into existence. Mob validation is a quality practice, not an accountability structure; "the room agreed" satisfies no auditor we have ever sat across from.
* **A review standard for AI-drafted plans.** What the approver actually checks: data classifications touched, blast radius, rollback path, deviations from the steering files. Without a checklist, bolt-speed approval decays into reflexive clicking within a week.
* **A decision log bound to artifact versions.** Which spec version, which steering-file version, who approved, when. The workflows give you the raw trail; your job is binding it to identities and a retention policy.

Our [AI governance](/ai-governance/) pillar covers how these review gates generalize — the named-approver pattern applies to any AI-planned change, not just software.

## Governance Hole #2: The Evaluation Bar for Agent-Written Code

The second hole is quieter, and worse.

### The self-grading problem

In Construction, the same agent that writes the code writes the tests. That is self-grading. A green suite authored by the code's author proves consistency, not correctness — an agent that misread a requirement writes tests that faithfully verify the misreading. At sprint cadence a reviewer might catch it. At bolt cadence, with AI generating both sides of the check, the error compounds silently until production finds it.

The DVT214 presenters were blunt about ownership: you cannot defend a check-in with "the AI did this"; the developer stands behind every line. Right sentiment. Not a mechanism. A norm is not an evaluation bar — it does not say what must pass, at what threshold, before agent-written code ships.

### What the bar looks like in practice

* **Acceptance tests with independent provenance.** Write them — or at minimum human-review and freeze them — during Inception, from the validated requirements, before Construction begins. The agent then implements against a bar it did not set.
* **Trajectory evaluation for the agents themselves.** Outcome checks miss the agent that reached a correct answer through a tool-call path that fails on the next input. Scoring the path, not just the endpoint, is its own discipline — covered in [agent evaluation and testing](/insights/ai-agent-evaluation-testing/).
* **A frozen regression set per release.** Re-run it on every steering-file or model change. Our [LLM evaluation guide](/insights/llm-evaluation-guide/) maps which eval type belongs at which gate.
* **Versioned steering files, because they are prompts.** A steering file is the encoded engineering standard for every future bolt; an untracked edit silently changes what your whole pipeline builds. Give it the same registry-and-labels discipline as [prompt versioning](/insights/prompt-versioning/).

## An AI-DLC Adoption Path That Survives an Audit

Flow diagram of a single AI-DLC bolt with governance gates added: a unit of work becomes an AI-drafted plan, passes Gate 1 where a named approver who is not the prompter signs the plan, proceeds to Mob Construction where the agent writes code and tests, passes Gate 2 an independent evaluation bar of frozen acceptance tests and trajectory evals, then merges and deploys, with both gates writing to a decision log bound to spec version, steering-file version, approver identity, and eval scores.

The teams we have watched get this right run AI-DLC inside existing change management, not instead of it. In order:

1. **Pilot on one internal, low-blast-radius service.** Not the payments path. You want a system where a bad bolt costs embarrassment rather than an incident report, while the team learns what validation fatigue feels like.
2. **Write the review-gate policy before the first bolt.** Named approver, review standard, decision log — the three controls above, one page, signed off by whoever owns your change process. Retrofitting governance onto a team already moving at bolt speed is twice the fight.
3. **Make human-validated acceptance tests an Inception exit criterion.** The phase is not done when requirements exist. It is done when the tests that will judge Construction exist and a human has approved them.
4. **Run every unit of work through your existing change process.** One change ticket per unit of work; the artifact trail the workflows generate becomes the ticket's evidence. Bolts compress development time — they do not exempt you from change control.
5. **Stand up agent evals before scaling from one team to five.** A pilot team can cover for a missing eval harness with raw attention. Five teams cannot, and by then agent-written code volume has outrun any human's ability to read it.
6. **Track defect escape rate next to velocity.** AWS's financial-services guidance suggests time to deployment, time to recovery, and failed-deployment rate as the KPI set; add escaped defects. If 10x velocity arrives with 3x escaped defects, you did not get faster. You moved QA into production.

## What to Steal, What Breaks

### Steal these even if you never run a bolt

The intent-first elaboration session — an agent interrogating requirements before any code exists — is the highest-leverage single practice here, and it works fine inside a plain two-week sprint. Units of work scoped to one validated decision are a better planning grain than epics no matter who writes the code. And steering files as executable engineering policy are simply good practice for any team using coding agents.

### What breaks if you adopt it uncritically

Review theater at machine speed: approval volume outruns human attention, and sign-off decays into a rubber stamp — worse than no gate, because it manufactures false audit evidence. A compliance posture calibrated for quarterly releases meets a daily-release reality it was never designed to certify. And your best engineers quietly burn out as full-time validators — the one job the agent cannot do.

AI-DLC gets the diagnosis right: the SDLC's rituals priced in a constraint that no longer exists. What it does not ship is the control layer that made those rituals defensible. AWS handed you the speed. The accountability is still yours to build — and it should be built first.

## Frequently Asked Questions

### What is AI-DLC?

AI-DLC (AI-Driven Development Lifecycle) is AWS's methodology for software development in which AI agents draft the plans, code, tests, and infrastructure while humans validate each step before execution. It runs in three phases — Inception, Construction, Operations — in bolts lasting hours or days rather than weeks. AWS published it in July 2025 and open-sourced the workflow rules (awslabs/aidlc-workflows) that November.

### How is AI-DLC different from the traditional SDLC?

The traditional SDLC batches work into sprints because human coordination is expensive; AI-DLC assumes the bottleneck has moved to validation speed. Sprints become bolts of hours to days, epics become units of work, and solo authorship plus asynchronous review becomes mob-style live validation of AI-drafted plans.

### What are bolts in AI-DLC?

A bolt is AI-DLC's replacement for the sprint: a work cycle measured in hours or days in which the team validates an AI-proposed plan, the agent executes it, and the results are reviewed. The shorter cycle reflects that an agent drafts architecture, code, and tests in minutes — the two-week batch built for human-paced work becomes queueing delay.

### Is AI-DLC tied to AWS tools like Kiro?

No. The open-sourced workflow rules ship with installations for Kiro, Amazon Q Developer, Cursor, Cline, Claude Code, GitHub Copilot, and OpenAI Codex, under the permissive MIT-0 license. Kiro is the natural fit because its spec files — requirements.md, design.md, tasks.md — match the artifact trail the methodology assumes, but nothing in it requires an AWS toolchain.

### What are Mob Elaboration and Mob Construction?

They are AI-DLC's two collaborative rituals. In Mob Elaboration (Inception), the whole team — product, engineering, QA — synchronously validates the requirements and units of work the AI drafts from business intent. In Mob Construction, the team validates AI-proposed architecture, code, and tests in real time. Both exist so AI output is never accepted blind.

### Does AI-DLC include governance and compliance controls?

Partially. The open-sourced workflows embed human approval checkpoints and log artifacts and decisions, and AWS's financial-services guidance adds policy-encoding steering files plus requirement-to-test traceability. What none of the material defines is who holds approval authority or what evaluation threshold agent-written code must clear — you have to supply named approvers, a review standard, and an independent eval bar yourself.

## References

1. AWS DevOps Blog — "AI-Driven Development Life Cycle: Reimagining Software Engineering" (July 2025). <https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/>
2. AWS DevOps Blog — "Open-Sourcing Adaptive Workflows for AI-Driven Development Life Cycle (AI-DLC)" (November 2025). <https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/>
3. awslabs/aidlc-workflows — the open-sourced AI-DLC workflow rules, MIT-0 license. <https://github.com/awslabs/aidlc-workflows>
4. AWS Industries Blog — "AI-Driven Development Lifecycle for Financial Services" (May 2026). <https://aws.amazon.com/blogs/industries/ai-driven-development-lifecycle-for-financial-services/>
5. AWS re:Invent 2025 — "Introducing AI driven development lifecycle (AI-DLC)," session DVT214. <https://www.youtube.com/watch?v=1HNUH6j5t4A>
6. Kiro documentation — Specs: requirements, design, and task artifacts. <https://kiro.dev/docs/specs/>
7. Establishes the 2025 DORA survey's publication date and sample (nearly 5,000 technology professionals), 90% AI adoption, more than 80% reporting productivity gains, 30% reporting little or no trust in AI-generated code, and the positive relationship with delivery throughput alongside the continuing negative relationship with delivery stability — Google Cloud (September 2025): <https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report>
8. Source of the 14-point year-over-year adoption increase, the two-hour median daily time working with AI, the full trust breakdown (4% / 20% / 23% / 7%), and the 59% reporting improved code quality — Google, summarising the 2025 DORA report (2025): <https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/>
