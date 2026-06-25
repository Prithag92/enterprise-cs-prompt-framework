# Example: Support Response — Before vs. After Framework

**Scenario:** Inbound support email from an asset management client reporting 
a delayed data feed for NAV calculations. Issue reported at 9:15am. Engineering 
is investigating. No confirmed root cause. ETA unknown. Within SLA (just). 
Account is Priority tier, relationship is stable.

---

## The client's email

> Hi team,
>
> We're seeing a delay in our NAV data feed this morning — it should have 
> updated by 8:30am and it's now 9:15am with nothing coming through. 
> This is affecting our morning reconciliation run.
>
> Can you let us know what's happening?
>
> Thanks,
> Sarah

---

## ❌ Without the framework (raw ChatGPT, no prompt structure)

> Hi Sarah,
>
> I hope this email finds you well. Thank you for reaching out to us regarding 
> the delay you are experiencing with your NAV data feed.
>
> I understand that this is causing issues with your morning reconciliation run 
> and I want to assure you that we take these matters very seriously. Our team 
> is currently looking into the issue and we will do everything we can to resolve 
> it as quickly as possible.
>
> We appreciate your patience and understanding during this time. Please don't 
> hesitate to reach out if you have any further questions or concerns. We will 
> keep you updated as we have more information.
>
> Best regards,
> Customer Success Team

**What's wrong with this:**
- Opens with "I hope this email finds you well" — irrelevant filler when a client 
  is mid-incident
- "I want to assure you that we take these matters very seriously" — hollow; 
  every company says this
- "Do everything we can" — vague, implies uncertainty about capability
- "Please don't hesitate to reach out" — weak closing; the client already reached 
  out, that's why we're here
- No specific next action. No time. No ownership.
- A client reading this knows nothing more than before they sent the email.

---

## ✅ With the framework (support-response-v3, full context injection)

**Context injected:**
- CLIENT_NAME: Hartwell Asset Management
- CLIENT_TYPE: Asset manager
- ACCOUNT_TIER: Priority
- RELATIONSHIP_STAGE: Active
- KNOWN_SENSITIVITIES: None
- ISSUE_SUMMARY: NAV data feed delayed since 8:30am, affecting morning reconciliation
- CHANNEL: Email
- TIME_SINCE_REPORT: 45 minutes
- SLA_STATUS: Within SLA
- RESOLUTION_STATUS: Engineering investigating, no confirmed root cause
- ETA: Unknown
- WORKAROUND: No

**Output:**

> Hi Sarah,
>
> We're aware of the NAV feed delay you've flagged — it's been with our 
> engineering team since 9:20am and they're actively investigating. We don't 
> have a confirmed root cause yet and I won't give you a resolution time until 
> we do, but I'll send you a direct update by 10:30am IST whether or not 
> we have a fix in place by then.
>
> No workaround is available for the reconciliation run at this point — I'll flag 
> immediately if that changes.
>
> Pritha Ghosh, Customer Success, daappa

**What works:**
- Opens with the situation, not pleasantries
- Explicitly acknowledges no root cause — doesn't pretend to know more than it does
- Gives a specific update time (10:30am) — not "soon" or "shortly"
- Short. Confident. Complete.
- The client knows exactly what is happening, what isn't known, and when they 
  will hear next.

---

## Rubric scores

| Check | Without framework | With framework |
|---|---|---|
| Factual accuracy | ⚠️ No facts — generic | ✅ All details accurate |
| Tone calibration | ❌ Over-apologetic, weak | ✅ Direct, professional |
| Completeness | ❌ No next step or time | ✅ Specific next update at 10:30am |
| Length / format | ❌ 127 words, too long for content | ✅ 89 words, appropriate |
| Confirmation placeholder | ✅ N/A (not knowledge prompt) | ✅ N/A |

**Without framework:** 2/5 — would require rewrite before sending  
**With framework:** 5/5 — edit-ready after 30-second read-through

---

## Time comparison

| | Without framework | With framework |
|---|---|---|
| Prompt setup | 0 min (blank start) | 3 min (fill context variables) |
| Raw output quality | Poor — significant rewrite needed | Good — minor edits only |
| Edit time | ~15 min | ~2 min |
| **Total time** | **~15 min** | **~5 min** |

*Across 5 enterprise accounts with average 8–10 support interactions per week, 
this represents approximately 8–10 hours of CS capacity recovered per week.*
