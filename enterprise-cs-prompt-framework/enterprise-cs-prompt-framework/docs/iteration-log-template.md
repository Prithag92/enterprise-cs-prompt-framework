# Prompt Iteration Log Template

## How to use this

Copy the template below each time you make a meaningful change to a prompt — 
or each time you significantly edit an output (2+ sentences changed before sending).

This log is the mechanism by which the framework improves. An unlogged edit 
is a bug that will recur.

---

## Entry template

```
---
DATE: [YYYY-MM-DD]
PROMPT: [which prompt — e.g. support-response-v3, status-update-v2]
LOGGED BY: [your name]

SCENARIO:
[Brief description of the client situation this prompt was run for — 
no client names, just context type e.g. "P2 data ingestion issue, 
strained account, 48h into incident"]

WHAT HAPPENED:
[What did the raw output do wrong, or what did you have to change before sending?]

ROOT CAUSE:
[Why did the output fail or need editing?]
□ Thin context injection — didn't provide enough information
□ Wrong variable value — context field was inaccurate or missing
□ Prompt instruction gap — the prompt didn't cover this scenario
□ Model variability — prompt is fine, output was an outlier
□ Rubric catch — rubric correctly identified the issue before sending

CHANGE MADE:
[What did you change in the prompt, or what additional instruction/constraint 
did you add?]

EXPECTED OUTCOME:
[What should be different next time this scenario runs?]

VALIDATED:
□ Yes — tested on similar scenario, improvement confirmed
□ Not yet — change logged, validation pending
---
```

---

## Example entry

```
---
DATE: 2026-03-14
PROMPT: support-response-v3
LOGGED BY: Pritha Ghosh

SCENARIO:
Inbound query from asset manager re: delayed NAV data feed. 
Account is in renewal stage, previous escalation 6 weeks ago. 
Issue was within SLA but client was already sensitised.

WHAT HAPPENED:
Output included "we understand this may be frustrating" — generic empathy 
phrase that reads as formulaic to a sophisticated institutional client 
who has had a previous escalation. Removed before sending.

ROOT CAUSE:
□ Prompt instruction gap — the prompt didn't cover this scenario
The banned phrases list covers specific filler phrases but doesn't 
address the category of "generic empathy language in accounts with 
escalation history." The KNOWN_SENSITIVITIES field was filled but 
the prompt doesn't tell the model how to adjust for escalation history.

CHANGE MADE:
Added to constraints section: 
"If KNOWN_SENSITIVITIES includes previous escalation: omit all empathy 
language. Lead with action, not acknowledgement. Empathy reads as hollow 
to a client who has already escalated; demonstrated competence is more 
valuable."

EXPECTED OUTCOME:
Outputs for accounts with escalation history should lead with what is 
being done, not with how the team feels about the situation.

VALIDATED:
□ Not yet — change logged, validation pending
---
```

---

## Iteration log index

Track all entries below for searchability.

| Date | Prompt | Change type | Logged by |
|---|---|---|---|
| 2026-03-14 | support-response-v3 | Added escalation history instruction | PG |
| 2026-02-28 | escalation-summary-v2 | Added "not confirmed in thread" instruction | PG |
| 2026-02-10 | status-update-v2 | Added relationship temperature variable | PG |
| 2026-01-22 | knowledge-retrieval-v2 | Added [REQUIRES HUMAN CONFIRMATION] pattern | PG |
| 2026-01-08 | support-response-v2 | Added banned phrases list | PG |
