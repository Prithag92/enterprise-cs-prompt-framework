# Enterprise CS Prompt Framework
### LLM-Assisted Client Communication for Investment Management & FinTech SaaS

---

> **Built from production experience.**
> This framework emerged from real work: deploying Claude and ChatGPT across enterprise client success workflows in an investment data management SaaS environment. It reduced client-facing response time by ~50% across 5 enterprise accounts over a 12-month rollout.
>
> It is not a tutorial. It is not a collection of "awesome prompts." It is a structured, opinionated system for making LLMs reliable enough to trust inside regulated, client-facing enterprise operations.

---

## Why this exists

Most enterprise teams fail at AI adoption not because the models are bad — but because they deploy them wrong.

They give a CSM access to ChatGPT and say "use this to respond faster." What they get is inconsistent tone, hallucinated details, responses that don't match their brand, and one bad client interaction that kills trust in the tool for six months.

This framework solves that. It provides:

- **Structured prompt templates** across the four highest-friction CS workflows
- **Injection patterns** for domain-specific context (fund types, data terminology, SLA language)
- **Iteration logs** showing what changed between prompt versions and why
- **Evaluation rubrics** for scoring LLM output before it reaches a client
- **Adoption playbook** for rolling this out across a CS team without chaos

---

## Repo structure

```
enterprise-cs-prompt-framework/
│
├── prompts/
│   ├── support/          # Inbound issue response drafting
│   ├── escalation/       # Escalation summarisation for internal handoff
│   ├── status/           # Proactive status updates to clients
│   └── knowledge/        # FAQ and knowledge retrieval responses
│
├── evaluation/           # Scoring rubrics and output quality checklists
├── examples/             # Before/after: raw LLM output vs. framework output
├── docs/                 # Adoption playbook, onboarding guide, design decisions
└── scripts/              # Utilities: prompt testing, batch evaluation
```

---

## The four prompt categories

| Category | Use case | Friction before LLM | Outcome after framework |
|---|---|---|---|
| **Support response** | Drafting replies to inbound client issues | 30–45 min per response, inconsistent quality | ~10 min with structured prompt, consistent tone |
| **Escalation summary** | Summarising incident context for internal handoff | Manual writeup, often incomplete | Structured summary in 2 min from raw thread |
| **Status update** | Proactive client comms during incidents or delays | Delayed sends, variable messaging | Templated, reviewed, sent within SLA window |
| **Knowledge retrieval** | Answering client FAQs from product/process knowledge | Searching docs manually, varying accuracy | Grounded responses with explicit knowledge injection |

---

## Design principles

**1. Specificity over flexibility**
Generic prompts produce generic outputs. Every template here is opinionated about structure, tone, and length — because that's what makes output consistent enough to trust.

**2. Context injection is non-negotiable**
LLMs hallucinate when they lack domain context. Every prompt in this framework has a designated context block where the operator injects: client name, issue history, product area, SLA status, and relevant terminology. No prompt runs without it.

**3. Output structure before tone**
We found that fixing structure first (headers, length, format) produced more reliable improvements than tuning tone. Tone was the last variable we adjusted, not the first.

**4. Evaluation before deployment**
No LLM output goes to a client without passing a 5-point rubric check. The rubric lives in `/evaluation/`. It takes 60 seconds. It prevents the one bad response that kills six months of trust-building.

**5. Designed for non-technical users**
Every prompt is written so a CSM with no AI background can run it correctly. The complexity is in the design, not the operation.

---

## Quick start

1. Clone the repo
2. Read `/docs/adoption-playbook.md` before using any prompts
3. Start with `/prompts/support/support-response-v3.md` — the most battle-tested template
4. Run any output through `/evaluation/output-rubric.md` before sending
5. Log what you change and why in the iteration log format (see `/docs/iteration-log-template.md`)

---

## What this is not

- Not a plug-and-play tool. It requires a human in the loop at every step.
- Not model-agnostic by accident. Templates are tested on Claude (Anthropic) and GPT-4. Other models may need adjustment.
- Not a replacement for CS judgment. The framework handles drafting and structure. The CSM handles relationship, context, and final review.

---

## Author

**Pritha Ghosh** — AI Customer Success Leader, FinTech SaaS  
12+ years across software engineering, enterprise CS, and LLM workflow design  
Generative AI Certification — IIT Guwahati (In Progress, 2026)  
[linkedin.com/in/pritha-ghosh1](https://linkedin.com/in/pritha-ghosh1)

---

*If this framework is useful to you — or if you think something is wrong with it — open an issue or connect on LinkedIn. I'm more interested in the conversation than the stars.*
