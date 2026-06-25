# Quick Reference — Which Prompt to Use

## Scenario → Prompt mapping

| Situation | Prompt to use | Time to set up |
|---|---|---|
| Client reports a bug or issue | `support/support-response-v3.md` | ~3 min |
| Issue needs internal escalation | `escalation/escalation-summary-v2.md` | ~2 min |
| Incident ongoing, need to update client proactively | `status/status-update-v2.md` | ~3 min |
| Client asks a product / process question | `knowledge/knowledge-retrieval-v2.md` | ~4 min |

## Before every prompt run
- Fill **all** `{{VARIABLES}}` — write "unknown" not blank for missing fields
- Have the **evaluation rubric** open: `evaluation/output-rubric.md`

## After every prompt run
- Run the **5-point rubric** — 60 seconds — before any further action
- If you edited more than 2 sentences: **log it** in `docs/iteration-log-template.md`

## Hard stops — do not use a prompt if:
- You have under 2 minutes — write it yourself
- The situation is genuinely novel with no comparable past context
- The client relationship requires something deeply personal
- You have no knowledge to inject for a knowledge retrieval question

## Models
Both **Claude (Anthropic)** and **ChatGPT / GPT-4** work with all prompts.  
Claude: slightly better on tone-sensitive escalations  
GPT-4: slightly more concise on technical summaries  
Either: requires the same rubric pass before sending
