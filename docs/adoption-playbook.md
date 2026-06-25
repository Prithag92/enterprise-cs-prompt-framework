# Enterprise CS Prompt Framework — Adoption Playbook
**For:** CS team leads rolling out LLM-assisted workflows  
**Time investment:** 2–3 weeks for full team adoption  
**Prerequisites:** Team has access to Claude or GPT-4. Nothing else required.

---

## What this playbook covers

How to introduce this framework to a customer success team — including the parts 
most adoption guides skip: handling resistance, managing the first bad output, 
and building the habits that make AI usage sustainable rather than a month-long 
experiment that quietly dies.

---

## Why most CS AI rollouts fail

They skip straight to tool access.

A CSM gets access to ChatGPT, uses it twice, gets one output that needs heavy 
editing, concludes "it's faster to just write it myself," and never uses it again.

The failure is not the tool. The failure is the absence of:
1. A structured prompt (they started from blank)
2. An evaluation step (they sent the first output without reviewing)
3. A feedback loop (nobody captured what went wrong to improve it)

This playbook builds all three before anyone touches a live client communication.

---

## Week 1 — Foundation (do not skip this)

### Day 1–2: Context before tools
Before showing anyone a prompt, run a 30-minute session on:

**Why LLMs fail in enterprise CS specifically:**
- They don't know your clients
- They don't know your product
- They produce confident wrong answers when context is thin
- They are consistent in structure, inconsistent in judgment

This session exists to reset expectations. Teams that understand why LLMs fail 
use them more effectively than teams who are told they're transformative.

**Talking points:**
"The model is not trying to help your client. It is trying to produce text that 
looks like a good response. Your job is to make sure it has enough real information 
that 'looks like a good response' and 'is a good response' are the same thing."

### Day 3–4: The rubric before the prompt
Introduce the evaluation rubric (`/evaluation/output-rubric.md`) before showing 
anyone a prompt template.

Have each team member run the rubric against three real emails they wrote last 
week — without any AI involvement. The goal is not to score the emails. The goal 
is to internalise the five dimensions of a good CS response so the rubric feels 
like articulating things they already know, not memorising new criteria.

### Day 5: First prompt — support response only
Introduce the support response prompt (`/prompts/support/support-response-v3.md`) 
with a real but low-stakes scenario.

**Exercise:** Each team member picks one inbound support email from the past month 
and runs it through the prompt. They then apply the rubric and note what they had 
to change.

**Debrief questions:**
- What did the model get right without being told?
- What did it get wrong because the context was thin?
- What would you change in the context injection?

Do not move to other prompt categories until the team is consistently producing 
rubric-passing outputs from the support prompt.

---

## Week 2 — Expansion and habits

### Introduce escalation and status prompts
Once the support prompt is comfortable, introduce escalation summarisation and 
status update prompts — in that order.

Status updates are the highest-stakes prompt category. Do not introduce them 
until the team has built evaluation habits. A CSM who skips the rubric on a 
low-stakes support response will skip it on a high-stakes status update too.

### Build the iteration habit
Introduce the iteration log (`/docs/iteration-log-template.md`).

The rule: if you change more than two sentences of a prompt output before sending, 
log what you changed and why. It takes 90 seconds. It is the entire mechanism 
by which the framework improves.

**Common resistance:** "I don't have time to log things."  
**Response:** "If you edited the output, the prompt didn't work correctly. 
Logging it takes less time than editing it will take the next person who runs 
the same prompt on the same scenario."

### Peer review session
Weekly 20-minute session where two team members share one prompt output each — 
the raw LLM draft and the final version they sent — and discuss what changed 
and why.

This is more valuable than any documentation. CS knowledge about what works 
for which clients lives in people's heads. This session externalises it.

---

## Week 3 — Knowledge retrieval and full workflow

### Introduce knowledge retrieval prompt
The knowledge retrieval prompt requires good internal documentation to work. 
Before rollout, identify the 10 questions clients ask most frequently and ensure 
there is a clear, accurate, written answer to each one that can be injected.

If that documentation doesn't exist: write it first. The prompt cannot compensate 
for absent knowledge.

### Full workflow dry run
Simulate a complete client incident: inbound support email → escalation summary → 
status update → follow-up knowledge question. Run the full sequence using prompts, 
evaluate each output, log what needed changing.

---

## Handling the first bad output in production

This will happen. A prompt output will get sent to a client with an error — 
a wrong date, an imprecise product description, a tone miss.

**What not to do:** Remove access to the tools or pause the rollout.

**What to do:**
1. Handle the client situation normally — own the error, correct it, move on
2. Identify which rubric check would have caught the error
3. Update the relevant prompt with a constraint that prevents the same error
4. Log it

The goal is a framework that improves from failures, not one that is paused by them. 
One production error that generates a prompt improvement is better than six months 
of caution that delays adoption.

---

## Measuring success

Track these weekly from week 2 onwards:

| Metric | How to measure | Target |
|---|---|---|
| Average drafting time per response | Self-reported, spot check | 50% reduction vs. baseline |
| Rubric pass rate on first draft | Log rubric outcomes | >80% after week 3 |
| Outputs requiring >2 sentence edits | Iteration log | Declining week-on-week |
| Team adoption rate | Who is using prompts vs. not | 100% by end of week 3 |

Do not measure client satisfaction as a primary AI adoption metric. Client satisfaction 
reflects many variables. Operational metrics tell you whether the framework is working.

---

## When to not use a prompt

- When you know exactly what you want to say and it will take 5 minutes to write
- When the client relationship requires something highly personal that templates 
  will flatten
- When the situation is genuinely novel and you have no good context to inject
- When you are under 2 minutes to a deadline — drafting from blank is faster 
  than prompt setup in an emergency

The framework is a tool, not a mandate. Judgment about when to use it is part 
of using it well.
