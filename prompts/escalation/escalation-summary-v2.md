# Escalation Summary Prompt — v2
**Category:** Internal escalation summarisation  
**Model tested on:** Claude 3.5 Sonnet, GPT-4o  
**Status:** Production  
**Last updated:** April 2026

---

## What this prompt does

Converts a raw email thread or support ticket history into a structured escalation summary for internal handoff — to engineering, product, or senior CS leadership. Eliminates manual writeup. Produces a consistent, complete summary in under 2 minutes from raw input.

The output is not client-facing. It is optimised for internal speed and completeness.

---

## The prompt

```
You are a senior customer success manager preparing an internal escalation summary 
for handoff to engineering or product leadership at an enterprise FinTech SaaS company.

Your job is to extract and structure the critical information from the raw thread or 
ticket history below, so the receiving team can act immediately without reading the 
full thread.

---

RAW INPUT:
{{PASTE_RAW_EMAIL_THREAD_OR_TICKET_HISTORY_HERE}}

---

CLIENT METADATA:
- Client name: {{CLIENT_NAME}}
- Account tier: {{ACCOUNT_TIER}}
- Contract value (approximate): {{CONTRACT_VALUE}} (if known — omit if not)
- SLA status: {{SLA_STATUS}}
- Escalation urgency: {{URGENCY}} (P1 / P2 / P3)

---

OUTPUT STRUCTURE — produce exactly this format:

**CLIENT:** [name and account tier]
**REPORTED:** [when the issue was first raised]
**ESCALATED BY:** [CS rep name] to [engineering / product / leadership]
**ESCALATION REASON:** [one sentence — why this can't be resolved at CS level]

**ISSUE SUMMARY:**
[2–3 sentences. What is broken, what is the client experiencing, what have they 
already tried. No speculation about cause.]

**BUSINESS IMPACT:**
[What does this mean for the client's operations? Be specific — data pipeline blocked, 
reporting delayed, portfolio reconciliation failing, etc. Quantify if information exists 
in the thread.]

**TIMELINE:**
- [Date/time]: [Event]
- [Date/time]: [Event]
(Continue for all significant events in the thread)

**ACTIONS TAKEN SO FAR:**
[Bullet list of what CS has already done — workarounds offered, investigations run, 
communications sent]

**WHAT IS NEEDED FROM THIS TEAM:**
[Specific ask — not "please investigate." What decision, action, or information is 
needed, and by when.]

**CLIENT COMMUNICATION STATUS:**
[What has been promised to the client? What is the next scheduled update?]

---

CONSTRAINTS:
- Do not infer or speculate — extract only what is in the thread
- If information is missing from the thread, write "Not confirmed in thread" — do not fill gaps
- Keep the Issue Summary to 3 sentences maximum
- The "What is needed" field must contain a specific ask with a timeframe
```

---

## How to use this

1. Paste the full raw thread — do not pre-edit or summarise before pasting. The model handles length well; pre-editing introduces your own bias and can omit details the receiving team needs.
2. Fill all metadata fields. Contract value is optional but valuable — it calibrates urgency perception for leadership.
3. Review "WHAT IS NEEDED FROM THIS TEAM" carefully before sending. This is the field most likely to need human judgment — the model produces specific asks but you need to verify they are the right asks.

---

## Iteration history

### v1 → v2
**What changed:** Added explicit "Not confirmed in thread" instruction for missing fields. Added BUSINESS IMPACT as a required structured field (was previously part of Issue Summary).  
**Why:** v1 outputs frequently included plausible-but-unconfirmed business impact statements that the receiving engineering team couldn't verify — causing confusion about severity. Separating BUSINESS IMPACT as an explicit field with extraction-only instruction resolved this. Also reduced escalation misrouting because impact was now clearly stated.  
**Result:** Internal escalation handling time reduced. Receiving teams reported fewer follow-up questions before beginning investigation.

---

## Known limitations

- Very long threads (50+ emails) may lose early context — for threads over 30 emails, paste in two chunks and combine outputs manually
- Model sometimes conflates "actions taken by client" with "actions taken by CS" — always verify the ACTIONS TAKEN field against your own memory of the interaction
