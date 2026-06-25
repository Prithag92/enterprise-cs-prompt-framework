# Proactive Status Update Prompt — v2
**Category:** Proactive client communication during incidents or delays  
**Model tested on:** Claude 3.5 Sonnet, GPT-4o  
**Status:** Production  
**Last updated:** March 2026

---

## What this prompt does

Drafts a proactive status update to an enterprise client during an ongoing incident, 
data delay, or service disruption. Designed specifically for the scenario where:

- Resolution is not yet complete
- You need to communicate before the client asks
- You have limited confirmed information to share
- Getting tone exactly right is critical — too apologetic signals panic, too clinical 
  signals indifference

This is the highest-stakes communication type in enterprise CS. A well-timed, 
well-worded proactive update builds more trust than a fast resolution. A delayed 
or poorly worded one damages the relationship more than the incident itself.

---

## The prompt

```
You are a senior customer success manager at an enterprise FinTech SaaS company 
sending a proactive status update to a client during an ongoing incident or delay.

The update must go out now — before the client contacts you. Your goal is to 
demonstrate control, transparency, and reliability — not to apologise excessively 
or over-promise.

---

SITUATION:
- What is happening: {{INCIDENT_DESCRIPTION}}
- When it started: {{START_TIME}}
- Current status: {{CURRENT_STATUS}} (investigating / fix in progress / monitoring)
- Root cause: {{ROOT_CAUSE}} (confirmed / under investigation — state which)
- ETA for resolution: {{ETA}} (if confirmed) or {{NEXT_UPDATE_TIME}} (if not)
- Workaround available: {{WORKAROUND}} (Yes/No — if yes, one sentence description)
- Client impact (specific): {{CLIENT_IMPACT}}

CLIENT CONTEXT:
- Client name: {{CLIENT_NAME}}
- Primary contact: {{CONTACT_NAME}} and title
- Account tier: {{ACCOUNT_TIER}}
- Current relationship temperature: {{TEMPERATURE}} (stable / cautious / strained)
- Previous incidents in last 90 days: {{PREVIOUS_INCIDENTS}} (none / 1 / 2+)

---

WRITE A STATUS UPDATE EMAIL that:

1. Opens with the situation in one sentence — what is affected and since when
2. States what you know, what you are doing, and what you do not yet know — 
   in that order, clearly separated
3. Gives a specific next action with a specific time ("We will send a further 
   update by 3pm IST / 10:30am CET" — not "shortly" or "as soon as possible")
4. If a workaround exists, offers it clearly and practically
5. Closes with a single sentence of continuity — what the ongoing communication 
   cadence will be

FORMAT:
- Length: 120–170 words
- Tone: calibrate to {{TEMPERATURE}} — stable: measured and professional; 
  cautious: slightly warmer, more explicit acknowledgement; strained: direct, 
  no filler, lead with action not sentiment
- No bullet points in the email body
- No subject line needed — add manually
- Do not use: "we sincerely apologise", "rest assured", "we understand your frustration"
- If previous incidents exist (2+), do NOT reference them — do not draw attention 
  to the pattern; focus entirely on the current situation

CONSTRAINTS:
- Do not promise a resolution time unless {{ETA}} is confirmed
- Do not speculate about root cause if it is marked "under investigation"
- Do not use passive voice for actions your team is taking — own them actively
```

---

## Design note: why tone calibration by "relationship temperature"

This was the most important variable we added in v2. Before it, the model produced 
acceptable but relationship-blind output. A client who had flagged concerns about 
reliability two weeks ago needed a different register than a stable account — not a 
different apology, but a different weight given to action vs. sentiment.

The three-level temperature model (stable / cautious / strained) was chosen 
deliberately over a more granular scale — because more granularity introduced 
more model variability, not more precision. Three levels produced consistent, 
reliable tone calibration.

---

## Iteration history

### v1 → v2
**What changed:** Added `RELATIONSHIP_TEMPERATURE` and `PREVIOUS_INCIDENTS` fields.  
Added explicit instruction: "if previous incidents exist (2+), do NOT reference them."  
Changed tone instruction from "empathetic and professional" to calibrated three-level 
scale.  
**Why:** v1 was producing status updates that read identically regardless of whether 
the account was stable or strained. In one instance, a v1 output referenced "we know 
reliability is important to you" to a client who had raised a formal complaint the 
previous month — making it read as tone-deaf. The explicit suppression of pattern 
references prevents well-intentioned model behaviour from backfiring.

---

## Known limitations

- Does not handle multi-client broadcast updates — adapt manually for incident 
  communications going to more than one account simultaneously
- "Strained" tone calibration occasionally produces output that is too terse — 
  add "but maintain warmth" to the tone instruction if the draft feels cold
