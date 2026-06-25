# LLM Output Evaluation Rubric
**For:** All client-facing prompt outputs  
**Time to complete:** ~60 seconds  
**Mandatory:** Yes — no output goes to a client without passing this check

---

## Why this exists

The most common failure mode in enterprise AI adoption is not bad prompts — 
it is skipped review. A CSM under time pressure sends a raw LLM output, 
the client receives something subtly wrong, and trust in the tool collapses 
for months.

This rubric takes 60 seconds. It prevents that.

---

## The five-point check

Run through these in order. If any check fails, revise before sending.

---

### ✅ Check 1: Factual accuracy
**Question:** Does every factual claim in the output match what you know to be true 
about the client, the issue, and your product?

**Look for:**
- Incorrect product names or feature descriptions
- Wrong dates, times, or SLA windows
- Inferred root causes that are not confirmed
- Any detail that "sounds right" but you cannot verify

**Fail condition:** Any claim you cannot personally verify. Mark it for removal 
or replacement — do not send uncertain facts to clients.

**Investment management context:** Pay particular attention to any reference to 
data types (NAV, AUM, reconciliation, fund structures) — models frequently 
produce plausible-sounding but technically incorrect statements about FinTech 
domain specifics.

---

### ✅ Check 2: Tone calibration
**Question:** Does the tone match the client relationship and situation?

**Look for:**
- Over-apologetic language in a stable account (signals weakness)
- Under-acknowledgement in a strained or escalated account (signals indifference)
- Corporate filler phrases ("rest assured", "please don't hesitate", "as per")
- Passive voice in descriptions of your team's actions ("the issue is being 
  investigated" → "our engineering team is investigating")

**Quick test:** Read the email aloud. If any sentence would make you wince in 
a room with the client, it needs rewriting.

---

### ✅ Check 3: Completeness
**Question:** Does the output answer what the client actually asked or needs?

**Look for:**
- Missing next steps or unclear ownership ("we will look into this" — who? by when?)
- Unanswered sub-questions in multi-part client messages
- Missing workaround information when one exists
- No stated timeline for follow-up when resolution is unknown

**Fail condition:** A client reads this and still doesn't know what happens next 
and when. That's an incomplete response regardless of how well-written it is.

---

### ✅ Check 4: Length and format
**Question:** Is the length appropriate, and does the format match the channel?

**Email length guide:**
- Acknowledgement / status update: 120–180 words
- Support response with technical detail: 150–250 words
- Knowledge / FAQ response: 80–200 words depending on complexity
- Escalation summary (internal): no word limit — completeness over brevity

**Look for:**
- Unnecessary preamble before the main point
- Padding at the end ("please let me know if you have any questions" as a 
  standalone closing sentence — cut it; the client knows they can ask questions)
- Bullet points in emotional or sensitive communications — prose only

---

### ✅ Check 5: The [REQUIRES HUMAN CONFIRMATION] scan
**Question:** Did the knowledge retrieval prompt leave any `[REQUIRES HUMAN 
CONFIRMATION]` placeholders?

This applies only to knowledge retrieval outputs — but it is a hard stop. 
Search the draft for this string before sending. If found: answer the flagged 
question yourself, escalate it, or explicitly tell the client you will follow up.

**Never send a draft containing this placeholder.**

---

## Scoring

| Checks passed | Decision |
|---|---|
| 5/5 | Send after personal read-through |
| 4/5 | Revise the failing check — re-run rubric |
| 3/5 or below | Rewrite from scratch or respond manually |

There is no partial credit on Check 5. Any `[REQUIRES HUMAN CONFIRMATION]` 
placeholder = automatic revision regardless of other scores.

---

## Logging failures

If an output fails the rubric, note which check failed and why in your prompt 
iteration log. This is how the prompts improve over time. A rubric failure that 
isn't logged is a bug that will happen again.

See `/docs/iteration-log-template.md` for the logging format.
