# AI-Driven Development Lifecycle for Financial Services | AWS for Industries

# AI-Driven Development Lifecycle for Financial Services

by Silvia Prieto, Jean-Francois Landreau, and Richard Caven on 26 MAY 2026 in [Financial Services](https://aws.amazon.com/blogs/industries/category/industries/financial-services/ "View all posts in Financial Services"), [Industries](https://aws.amazon.com/blogs/industries/category/industries/ "View all posts in Industries"), [Kiro](https://aws.amazon.com/blogs/industries/category/artificial-intelligence/kiro/ "View all posts in Kiro") [Permalink](https://aws.amazon.com/blogs/industries/ai-driven-development-lifecycle-for-financial-services/) Share

  * [](https://www.facebook.com/sharer/sharer.php?u=https://aws.amazon.com/blogs/industries/ai-driven-development-lifecycle-for-financial-services/)
  * [](https://twitter.com/intent/tweet/?text=AI-Driven%20Development%20Lifecycle%20for%20Financial%20Services&via=awscloud&url=https://aws.amazon.com/blogs/industries/ai-driven-development-lifecycle-for-financial-services/)
  * [](https://www.linkedin.com/shareArticle?mini=true&title=AI-Driven%20Development%20Lifecycle%20for%20Financial%20Services&source=Amazon%20Web%20Services&url=https://aws.amazon.com/blogs/industries/ai-driven-development-lifecycle-for-financial-services/)
  * [](mailto:?subject=AI-Driven%20Development%20Lifecycle%20for%20Financial%20Services&body=AI-Driven%20Development%20Lifecycle%20for%20Financial%20Services%0A%0Ahttps://aws.amazon.com/blogs/industries/ai-driven-development-lifecycle-for-financial-services/)
  * 


This blog explains what the AI- Driven Development Lifecycle is and why it can help you drive faster application development using AI in a well governed and controlled way. We’ll explore the three stages of AI-DLC, examine how it transforms team structures, and provide a practical three-phase approach for getting started. But let’s start with Amazon CEO Andy Jassy’s 2025 Letter to Shareholders where he shared a story that should give every technology executive something to consider:

## A Signal Too Big to Ignore

> _“Six engineers rebuilt the entire Amazon Bedrock inference engine in 76 days using Kiro, Amazon’s agentic coding service. The original estimate was 40 engineers and a full year. This new engine, called Mantle, became the backbone of Amazon Bedrock’s rapid scaling. That compression ratio, from 40 person-years to 6 people in 76 days, is not an incremental improvement. It is a category shift in how software gets built.”_

This is not a proof-of-concept. It is production infrastructure powering one of the world’s largest AI services. Some of the processes, tools and ways of working used in this project are parts of what we refer to today as AI-Driven Development Lifecycle, or AI-DLC, which is what we will cover in this blog.

For financial services business and technology leaders like you, the implications are significant. If a team of six can achieve the output of forty in building mission-critical infrastructure, what does that mean for the next technology-led modernization program? The core banking transformation? The next payments system?

AI-DLC represents a structured, governance-rich methodology that directly addresses the operational risk concerns inherent in your organization adopting AI at scale. It embeds the controls and oversight that risk professionals require helping your organization to adopt it with confidence.

## The Problem With the Status Quo

Financial services technology leaders face a familiar tension. Customers expect real-time payments, personalized services, and omnichannel experiences. Meanwhile, regulatory requirements, legacy complexity, and the cost of large development organizations create drag on innovation that hiring alone cannot fully offset.

Traditional Agile still relies on human developers to write, review, test, and deploy every line of code. Even the most disciplined Scrum teams are constrained by cognitive throughput. The result: deployment cycles measured in weeks, backlogs that consistently grow faster than teams can address them, and a structural velocity ceiling that competitive pressure keeps pushing against.

Two flawed responses have emerged. The first is fully autonomous AI-managed development, letting AI run the process without adequate oversight. This is generally unreliable, unexplainable, and incompatible with regulated industries. The second is AI-assisted development: using AI as an autocomplete tool. This is more easily governed, but captures only a fraction of AI’s true potential.

AI-DLC charts a deliberate middle path. It uses AI’s full potential while preserving the human oversight that regulated industries require. AI orchestrates the development process; humans retain oversight, decision-making authority, and accountability.

## What Is AI-DLC? The Three Stages

At its core, AI-DLC is a methodology where AI agents orchestrate the whole process, generating plans, code, tests, and infrastructure configurations at each stage of the development lifecycle, but humans verify and approve before execution proceeds. The developer’s role shifts from writing code to managing and validating AI-generated outputs. The distinction sounds subtle; the operational impact is not.

### Stage 1: Inception (Mob Elaboration)

Cross-functional teams such as developers, product managers, business analysts, QA engineers collaborate in mob programming format to build context on the existing code base. With the help of tools like [Amazon Kiro](https://kiro.dev/), they elaborate design, create user stories, and plan small, consumable units of work.

The key insight: AI thrives on specificity. The richer the inputs, the higher the quality of generated outputs. AI agents accelerate this phase too, generating requirement drafts and surfacing follow-up questions at each step.

### Stage 2: Construction (Mob Construction)

With context established, AI agents take the lead, generating code and tests aligned to the elaborated user stories, including security and resilience tests and Infrastructure-as-Code (IaC). Human developers review, validate, and refine. The cadence shifts from “write code, then review” to “review AI-generated code continuously.” Documentation is generated on the fly and updated automatically with every change.

### Stage 3: Operation

AI-DLC does not stop at deployment. Production deployment can be automated through AI-generated IaC deployed through CI/CD pipelines. AI agents, such as [Amazon DevOps Agent](https://aws.amazon.com/devops-agent/), can augment incident management by investigating root causes autonomously. Continuous monitoring feeds back into the coding agent’s context, informing future inception cycles and creating a virtuous benefit cycle.

## The Organizational Shift: From Scrum Teams to AI Pods

The most significant change AI-DLC introduces is to team size and ways of working. The comparison is stark:

Dimension | Traditional SDLC | AI-DLC  
---|---|---  
Team size | Scrum teams of ~7 developers | AI Pods of 2–3 developers working in Mob format  
Cadence | Sprint planning, 2-week cycles | Work done in days; smaller batches, faster deployments  
Code review | After completion | Continuous, high-volume (Large Language Model + human)  
Testing | Low-fidelity mocks | High-fidelity with realistic simulators, security and penetration testing  
CI/CD | Slow build infrastructure | Fast pipelines with automated quality gates  
  
The results from early adoption are compelling. One European financial services institution shifted from one product owner with 12 developers delivering 15 features per sprint, to one product owner with just 3 developers delivering 35 features per sprint, a reduction of 9 external contractor FTEs delivering direct financial benefit to the business.

One important operational note: co-location, or virtual teams working the same hours, is particularly important during the Inception phase, where synchronous collaboration between humans and AI agents drives context quality, and context quality drives everything else.

## Infrastructure Must Keep Pace

Cloud migration addressed the foundational layer: scalability, resilience, cost flexibility. But the infrastructure conversation has moved on. The question is no longer where workloads run, but whether the platform underneath can support what the institution wants to do next.

Three infrastructure imperatives stand above the rest:

  1. **Redesign CI/CD pipelines for velocity.** In many institutions, every code change (regardless of size or risk) passes through the same committee-driven approval process. This approach becomes a bottleneck when AI-augmented teams can produce well-tested increments continuously. The answer is risk-based change categorisation: only material changes require human sign-off; routine changes flow through automated validation. Small, frequent, easily reversible releases are inherently less risky than large, batched ones. The pipeline must enforce this discipline.
  2. **Evolve security infrastructure.** The emergence of models like Anthropic Claude Mythos that has been built to autonomously discover and chain issues at a scale and speed that manual pen testing cannot match, signals a step change. The implication for banks is unambiguous: only a human-plus-FM defense can match the scale and speed of human-plus-FM-enabled actors. Security infrastructure can no longer be periodic and reactive. Continuous security scanning, automated penetration testing, and AI-generated validated fixes must become the baseline. [AWS Security Agent](https://aws.amazon.com/security-agent/) provides out of the box these functionalities.
  3. **Prioritize integration architecture.** Fragmented integration across APIs, event buses, data pipelines, identity layers, remains the single biggest drag on time to value. The infrastructure must provide the foundation that enables every other part of an organization’s digital transformation to deliver.



## Why Regulators Can Embrace AI-DLC

Speed and resource efficiency are the headline benefits of AI-DLC adoption. For regulated financial institutions, however, it is the governance and risk management architecture that determines whether those benefits are realizable at scale. AI-DLC places human-in-the-loop governance at the heart of its design.

The methodology provides end-to-end traceability from business intent to production code which is a critical requirement for audit and regulatory review. When a test fails the code can be traced to a requirement. The requirement can be traced to a user story:[![Requirement Traceability Flow User Story to Test Coverage traceability diagram](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2026/05/22/Requirement-Traceability-Flow-User-Story-to-Test-Coverage.png)](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2026/05/22/Requirement-Traceability-Flow-User-Story-to-Test-Coverage.png)

_Figure 1: Requirement Traceability Flow – User Story to Test Coverage_

Equally significant is the concept of embedded governance through steering files. These are structured configuration documents that guide the coding agent to produce code in line with enterprise requirements such as security policies, architecture standards, approved dependency lists, regulatory guidelines such as the EU AI Act, and responsible AI principles. Organizations do not add governance after the fact; they can include it into the agent’s operating parameters from the outset.

[![Organizational Standards and Guidelines for Secure Architecture](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2026/05/22/Organizational-Standards-and-Guidelines-for-Secure-Architecture.png)](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2026/05/22/Organizational-Standards-and-Guidelines-for-Secure-Architecture.png)

_Figure 2: Organizational Standards and Guidelines for Secure Architecture_

### Quality and Testing as First-Class Controls

AI-DLC emphasizes comprehensive testing, helping AI to validate its own work and self-correct when tests fail, including deviations from steering files. Developers and risk teams can see this loop at work by reviewing logged traces. The methodology advocates for left-shifted QA: catching issues as early as possible, before they compound. For financial institutions, this means that the increased volume of AI-generated code changes is matched by a proportionate increase in automated quality controls.

### Measurable Outcomes: The Business Case

AI-DLC introduces a suite of KPIs designed to work in opposition thereby preventing gaming of traditional performance statistics. These include: mean time to deployment, mean time to recovery, percentage of failed deployments, number of events by severity, technical debt levels, and customer net promoter score. These metrics provide risk and audit functions with quantifiable, ongoing assurance.

Amazon’s Cost-to-Serve-Software (CTS-SW) framework provides a practical lens for sizing the financial opportunity:

> _“Consider a CIO or CTO at a bank with 1,000 developers, each with an annual cost of $130K including tooling, totaling $130M in developer expenses. A 15% CTS-SW improvement achieves $20M in cost avoidance from a $2M solution investment — a 10x return. For every dollar invested, $10 are generated in return.”_

## Getting Started: A Three-Phase Approach

Institutions that have seen the evidence and want to act have a clear set of actions to follow. The approach is deliberate, sequenced, and designed to build organizational capability alongside technical implementation.

  1. **Phase 1 — Executive Alignment:** Confirm your C-suite understands how AI-DLC differs from traditional Agile and the organizational changes it demands. Tie adoption to measurable business outcomes. Without executive sponsorship, transformation stalls at the pilot stage.
  2. **Phase 2 — Technical Enablement:** Equip architects and engineering leads with deep knowledge of agentic coding tools such as [Amazon Kiro](https://kiro.dev/) or Anthropic’s Claude Code. Focus on best practices, change management, and developer experience measurement to build internal expertise and identify champion teams.
  3. **Phase 3 — Hands-On Pilots:** Run immersive pilot programs where teams bring their own code bases and build real solutions over two-to-three day sprints. Use these pilots to generate proof points and build the organizational momentum for broader rollout.



You can scale through two models: a decentralized approach with wide access with self-service training and community support; or a centralized approach that controls access and replicates in deliberate waves. Both are viable. Both share one non-negotiable prerequisite: mature DevSecOps practices must already be in place. AI-DLC amplifies existing capabilities. It does not compensate for foundational gaps.

## Conclusion

Adopting AI-DLC is not about handing control to AI. It is about embedding AI into a disciplined, governed development lifecycle; one where humans validate every critical decision, controls are automated and measurable, and you can demonstrate to regulators, auditors, and customers that your AI-developed solutions are trustworthy.

The business benefits are significant and proven: Amazon’s own experience demonstrates a compression from one year to 76 days, and a team of six rather than forty. But these benefits are only realizable if you invest in the supporting infrastructure such as fast CI/CD pipelines, high-fidelity testing environments, automated security and compliance gates, clear accountability structures, and ongoing measurement.

The AI-DLC methodology provides the framework for accelerated progress such that you can commit to the organizational and process changes required to operate within it safely. Contact your AWS account team to learn more.

## Further Reading

  * [AWS Blog: AI-Driven Development Life Cycle (Methodology Introduction)](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) — The original blog post announcing and explaining the AI-DLC methodology
  * [AWS Blog: Open-Sourcing Adaptive Workflows for AI-DLC](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/) — Explains how AI-DLC addresses rigid workflows, inflexible depth, and over-automation, and introduces the open-source implementation
  * [AWS Blog: Building with AI-DLC using Amazon Q Developer](https://aws.amazon.com/blogs/devops/building-with-ai-dlc-using-amazon-q-developer/) — A practical walkthrough of the AI-DLC workflow in action using Amazon Q Developer
  * [AI-DLC Method Definition Paper (Whitepaper)](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) — The full methodology whitepaper describing the principles, phases, and workflow patterns in depth



![Silvia Prieto](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/05/08/Silvia-Prieto.jpg)

### Silvia Prieto

Silvia is the Head of generative AI and ML for Global Financial Services companies in EMEA, Asia-Pacific and Japan. In her current job, she is responsible for shaping and delivering AI Go-To-Market strategies and thought leadership. Silvia plays a crucial role in assisting organizations in understanding the nuances of these innovative technologies and their applications, as well as providing guidance on large-scale implementation.

![Jean-Francois Landreau](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2026/05/22/Jean-Francois-Landreau.png)

### Jean-Francois Landreau

Jean-Francois Landreau is a Senior Solutions Architect for Global Financial Services, guiding his customers on resilience, containers and how to accelerate their Software Development Life Cycle among other things. He brings to these conversations his experience on Agile, DevOps and Platform Engineering collected over the years. He has led various platform implementations in different capacities since 2007 at Thomson Reuters and then at Allianz. He is a strong believer that you can't take enlightened enterprise decisions if you are too far away from the machine room.

![Richard Caven](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2026/05/22/Richard-Caven.jpg)

### Richard Caven

Richard Caven is a Worldwide Banking Specialist at AWS. He is responsible for the development and execution of strategic initiatives to help customers migrate to the cloud and drive their digital transformation journey. Richard joined AWS in 2018 from Barclays where he was a Managing Director and COO for the Global Treasury function.
