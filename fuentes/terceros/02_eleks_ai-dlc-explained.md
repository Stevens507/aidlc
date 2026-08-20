# AI-DLC Explained: How AWS Labs Brings Structure to AI Coding

> **Fuente:** ELEKS
> **URL:** https://eleks.com/blog/aws-ai-dlc-explained/
> **Descargado:** 2026-08-19

---

Article

# AI-DLC Explained: How AWS Labs Brings Structure to AI Coding

Related services

* [Agentic AI](https://eleks.com/services/ai-development-services/agentic-ai-development/)
* [AI development](https://eleks.com/services/ai-development-services/)
* [Software development](https://eleks.com/services/custom-application-development/)

Listen to the article
22 min

AI coding assistants are changing how quickly software gets built. They help generate features, fix bugs, and shorten timelines. However, this speed can also create challenges for governance. If AI writes the code, how can we ensure quality? How do we check for compliance? This is where the AWS Labs’ AI-DLC framework becomes important. Let's take a closer look.

Key takeaways

* AWS AI-DLC framework consists of three phases workflow (inception, construction, operations) with required human approvals at each stage to stop AI from acting on its own.
* The framework puts documentation first, so if all code is deleted, the complete record of what was built and why remains intact for compliance and audit purposes.
* AWS AI-DLC focuses on reproducibility and governance, which means it is better for regulated settings with clear requirements, rather than for rapid prototyping or exploring new ideas.

## Understanding the AWS AI-DLC

AWS AI-DLC (AI-driven development lifecycle) is a formal, structured workflow framework that guides [AI coding assistants](/services/ai-development-services/agentic-ai-development/) through a formal software development process. This framework enforces mandatory workflows using "steering files" (rules) that dictate how the AI must operate.

The structure of this workflow consists of three phases:

1. It starts with **inception**. That's where all your requirements are analysed, and workflow planning gets done.
2. Only then can it move into **construction**, which is the development, the functional design, the code generation, and testing.
3. There is a third phase, **operations**, where it’s deployed.

The framework requires users to provide **approval** at key points before moving to the next phase. You cannot go from inception to construction, or from planning to code generation, without someone signing off. This step-by-step process helps prevent the AI from making changes on its own or acting in unexpected ways.

AWS AI-DLC puts **documentation first**. All files go into `aidlc-docs/` subfolders based on their phase, while the application code stays in the main workspace and never in the documentation folders. This setup means that even if the code is deleted, the record of what was done is still there.

## Breaking down AWS AI-DLC’s rule set

Now let's talk about the rules themselves. The repository shows them broken down by phase **`inception/`** (includes 7 rule files like workspace detection, requirements analysis, user stories, application design, etc.), **`construction/`** (includes 6 rule files such as functional design, code generation, NFR requirements, infrastructure design, build/test), and **`common/`** (shared validation rules like content validation, ASCII/Mermaid diagram standards).

**Critical mandatory rules:**

* **Content validation:** all files must pass validation according to `common/content-validation.md` before they are created.
* **Rule details logging:** load the relevant rule detail files from `.kiro/aws-aidlc-rule-details/` before starting each phase.
* **Comprehensive audit logging:** log every user interaction, approval, and decision in `audit.md`, including all raw input and timestamps.
* **Checkpoint approvals:** users must explicitly approve before advancing between major stages.
* **Plan-level checkboxes:** mark each work step with [x] as soon as it is completed.
* **No emergent behaviour:** during construction phases, use only standardised 2-option completion messages.

## The AWS AI-DLC process: requirements analysis to code generation

AWS AI-DLC framework takes what could be messy AI input and turns it into a clear, repeatable workflow. The logging stands out. Every step, from requirements analysis to workflow planning and code generation, gets tracked in detail. Each decision is recorded in an `audit.md` file, making traceability a key feature.

### Requirements analysis

Requirements analysis is a structured nine-step execution process flow:

1. Load context: retrieve reverse-engineering docs for brownfield projects.
2. Analyse request: evaluate clarity, type, scope, and complexity.
3. Determine depth: choose minimal, standard, or comprehensive analysis level.
4. Assess provided materials: review existing requirements and intent statements.
5. Completeness analysis: systematically evaluate six requirement categories.
6. Generate questions: create a verification document; ask until ambiguities resolve.
7. Build requirements doc: synthesise findings with user answers.
8. Update tracking: mark Inception Phase progress complete.
9. Present results: deliver a structured completion message with the approval workflow.

Once the requirements are set, the next step is planning how the code will come together. This is where workflow planning kicks in. Instead of jumping straight into coding, the AI lays out a clear, step-by-step plan for [building the software](/services/custom-application-development/).

### Code generation process

**Part 1 - Planning:** Create a detailed, step-by-step code generation plan with explicit activities and story traceability.

**Part 2 - Generation:** Execute the approved plan sequentially, generating code, tests, and artifacts while updating progress checkboxes.

Critical rules:
:   * Application code in workspace root only; documentation in `aidlc-docs/` only
    * Brownfield projects modify existing files in-place rather than creating duplicates
    * "Do not deviate from the step sequence"
    * Never add hardcoded logic beyond specifications

## How AWS AI-DLC differs from standard AI development

| **Aspect** | **AWS AI-DLC** | **Traditional AI coding assistants** | **AI-native SDLC** |
| --- | --- | --- | --- |
| **Structure** | Rigid 3-phase workflow with gates | Ad-hoc, user-directed, based on knowledge and best practices | Fully autonomous loops |
| **Documentation** | Mandatory, comprehensive | Optional, minimal | Auto-generated, variable quality |
| **Approval process** | Explicit checkpoints required | Continuous iteration | Autonomous execution |
| **Governance** | Built-in audit trails | No formal tracking | Limited oversight |
| **Planning** | Upfront, formal design phase | Just-in-time, as needed | Autonomous planning |
| **Platform** | Amazon Q, Kiro only (though the specs-driven development approach can be used with other tools) | Platform-agnostic | Platform-agnostic |
| **Control model** | Human-gated progression | Human-in-the-loop | AI-driven |

AWS AI-DLC works best when your requirements are predictable, several stakeholders need to see how [AI](/services/ai-development-services/) makes decisions, you’re dealing with old code that needs to be understood, your team is onboarding and needs consistent AI behaviour, or when auditability is more important than how fast you develop.

On the other hand, traditional practices are better if you need to prototype quickly and your requirements change often, you’re working alone without managing stakeholders, you’re exploring solutions that aren’t clear yet, you have tight deadlines and need to ship fast instead of documenting everything, or you need flexibility because AI-DLC ties you to Amazon Q or Kiro.

### Detailed comparison of AWS AI-DLC vs alternative AI development approaches

1. vs ad-hoc AI assistance

#### AWS AI-DLC vs ad-hoc AI assistance (ChatGPT, Claude, GitHub Copilot)

Typical practice: Developers ask questions, get code snippets, iterate freely without formal structure.

AI-DLC difference:

* Enforces phases: You can't jump to coding without completing requirements analysis
* Mandatory documentation: Every decision is logged to `audit.md`, not just chat history
* Quality gates: User approval required before phase transitions
* Prescriptive workflow: Rules dictate what questions to ask and when

Trade-off: AWS AI-DLC sacrifices speed and flexibility for reproducibility and governance.

*It's important to note that Claude's code has a planning mode.*

2. vs AI pair programming

#### AWS AI-DLC vs AI pair programming (Cursor, Windsurf, Codeium)

Typical practice: AI provides inline suggestions, autocomplete, and refactoring within the IDE. The developer maintains full control.

AI-DLC difference:

* Process-driven, not code-driven: Focuses on requirements → design → code sequence
* Separate documentation phase: Creates extensive markdown artifacts before touching code
* Multi-file orchestration: Generates complete plans spanning multiple modules
* Checkpoint friction: Can't quickly iterate; must follow approval workflows

Trade-off: AWS AI-DLC emphasises planning over coding velocity; better for complex projects, worse for exploratory work.

3. vs autonomous AI agents

#### AWS AI-DLC vs. autonomous AI agents (GPT-Engineer, AutoGPT, Devin)

Typical practice: Give AI a high-level goal; it autonomously plans, codes, tests, and iterates until done.

AI-DLC difference:

* Human-gated progression: AI stops at checkpoints for approval vs. running autonomously
* Structured documentation: Formal requirements.md and design docs vs. internal agent logs
* No deviation: Strict adherence to approved plan vs. adaptive replanning
* Conservative scope: Works incrementally per unit vs. attempting end-to-end solutions

Trade-off: AWS AI-DLC prevents runaway AI behaviour but requires more human oversight.

Learn how AI coding agents function, what they can do, and why human oversight is still important for quality and security in our article: [AI Coding Agents: Boosting Productivity in Modern Software Development](/blog/ai-coding-agents/)

4. vs. TDD with AI assistance

#### AWS AI-DLC vs. TDD with AI assistance (specs-driven development)

Typical practice: Developer writes tests first, then asks AI to implement code that passes tests.

AI-DLC difference:

* Documentation-first, not test-first: Requirements and design docs precede test creation
* NFR phase: Dedicated stage for non-functional requirements (performance, security)
* Formal test plans: Build & Test stage generates comprehensive test strategies
* Less flexible: Can't easily refactor tests mid-development; must update formal plans

Trade-off: AWS AI-DLC ensures test coverage aligns with formal requirements but reduces TDD's iterative benefits.

5. vs. lightweight AI workflows

#### AWS AI-DLC vs. lightweight AI workflows (Aider, Smol Developer)

Typical practice: Minimalist CLI tools that use AI for specific tasks (code edits, generation) without enforcing structure.

AI-DLC difference:

* Heavy process overhead: 20+ rule files vs. simple command-line prompts
* Folder structure requirements: Must create `aidlc-docs/` hierarchy
* Platform lock-in: Requires Amazon Q or Kiro vs. any LLM API
* Activation ceremony: Must use "Using AI-DLC, ..." trigger phrase

Trade-off: AWS AI-DLC is enterprise-grade governance; lightweight tools are hacker-friendly productivity boosters.

## AWS AI-DLC limitations to consider

* **IDE tool lock-in:** Rules designed specifically for Amazon Q and Kiro CLI - may not work with other AI coding assistants.
* **Documentation overhead:** Every phase generates multiple markdown files (requirements.md, audit.md, plans, designs, etc.).
* **Approval friction:** Mandatory checkpoints between phases require explicit user confirmation.
* **Learning curve:** 20+ rule files to understand; requires knowing when to invoke "Using AI-DLC, ..." trigger phrase.
* **Activation:** Users initiate projects by stating intent using "Using AI-DLC, ..." in chat. The workflow then presents structured multiple-choice questions, generates plans for user review, and produces artifacts in an `aidlc-docs/` directory after each approved stage.
* **Implementation:** AI-DLC activates through platform-specific steering mechanisms: Amazon Q Rules files in `.amazonq/rules/` or Kiro Steering Files in `.kiro/steering/`, copied from the `aidlc-rules` repository.

## Conclusions

This is a framework that forces mandatory quality gates, treats documentation as a first-class, mandatory deliverable, and gives you built-in traceable audit trails for every single decision.

The AWS AI-DLC proves that formalising these AI coding processes is less about making coding easier and is entirely about making AI coding governable. We can automate the generation of features, sure, but we can't automate the human trust that's needed to actually deploy them. And that raises a really critical question that everyone needs to consider as development just keeps accelerating.

If we accept the premise that AI needs these strict human-gated limitations to avoid emergent behaviour and maintain compliance, what is the ultimate trade-off that society is making? We're weighing the incredible speed of autonomous iteration against the safety and accountability of human-gated progression. That tension, that's probably the defining characteristic of the next decade of software development.

Want to implement governance frameworks for AI-driven development in your company?

Application development

We’ll help you bring your most complex software vision to life with our leading full-cycle custom application development service. So you can focus on delivering an incredible user experience that sets you apart from the competition.

## FAQs

What is the AWS AI DLC?

AWS AI-DLC is a framework that helps [AI coding](/research/ai-code-review/) assistants follow a clear, step-by-step process for building software. It uses sets of rules to make sure the AI works the way you want, every time.

What is the AI DLC approach?

The AI-DLC approach brings AI into every part of the software development process, working alongside your team from planning to launch. With humans guiding strategy and making key decisions, AI helps speed things up and keeps projects on track.

What are the stages of the AI project cycle?

First, you define the problem and set your goal. Next, you gather the data you need, then explore and prepare it for action. After that, it's time to build and train your [AI model](/expert-opinion/data-vs-models-ai-experts-take/). Once it's ready, you test how well it works. The final step is putting your model to work in the real world, and then keeping an eye on it to make sure it keeps getting better.

What is AI-assisted software development?

AI-assisted software development brings tools like [LLMs](/blog/how-llms-think/) and [machine learning](/services/data-science-services/machine-learning-services/) to every stage of software development. These tools help with everything from writing code and testing to debugging and documentation. With its help, developers can spend less time on repetitive tasks and more time solving big-picture problems.

Published:

**January 20, 2026**

Updated:

**January 21, 2026**

## Related Insights

[Retrieval-Augmented Generation (RAG) Explained: Why Most Systems Fail and the 20 Components That Fix Them

View article](https://eleks.com/research/retrieval-augmented-generation-rag-explained-components/ "Retrieval-Augmented Generation (RAG) Explained: Why Most Systems Fail and the 20 Components That Fix Them")

Listen to the article
13 min

AI-DLC Explained: How AWS Labs Brings Structure to AI CodingAI-DLC Explained: How AWS Labs Brings Structure to AI Coding

AI-DLC Explained: How AWS Labs Brings Structure to AI Coding

Your browser does not support the audio element. 

0:00 0:00

Speed

1x

Voice is AI-generated.  
Inconsistencies may occur.

Contact Us

What our customers say

The breadth of knowledge and understanding that ELEKS has within its walls allows us to leverage that expertise to make superior deliverables for our customers. When you work with ELEKS, you are working with the top 1% of the aptitude and engineering excellence of the whole country.

Right from the start, we really liked ELEKS’ commitment and engagement. They came to us with their best people to try to understand our context, our business idea, and developed the first prototype with us. They were very professional and very customer oriented. I think, without ELEKS it probably would not have been possible to have such a successful product in such a short period of time.

ELEKS has been involved in the development of a number of our consumer-facing websites and mobile applications that allow our customers to easily track their shipments, get the information they need as well as stay in touch with us. We’ve appreciated the level of ELEKS’ expertise, responsiveness and attention to details.
