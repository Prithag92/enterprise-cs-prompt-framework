# Design Decisions — Why the Framework is Built This Way

This document explains the reasoning behind the non-obvious choices in this 
framework. If you're adapting it for a different context, this is where to start.

---

## Why structured variables instead of freeform context

The first version of these prompts asked users to "provide relevant context about 
the client and issue." Outputs were inconsistent — not because the model was 
inconsistent, but because users were.

One CSM wrote three sentences. Another wrote a paragraph. A third wrote nothing 
and hoped the model would infer from the question alone.

Structured variable fields (`{{CLIENT_NAME}}`, `{{SLA_STATUS}}`, etc.) solve this 
by making the context completeness visible before the prompt runs. An empty field 
is immediately obvious. A vague paragraph is not.

The tradeoff: structured variables make prompts feel more like forms and less like 
natural language. For non-technical users this is actually an advantage — it removes 
the ambiguity of "how much should I write?" For experienced prompt engineers, it 
may feel constraining. The framework is designed for CS teams, not prompt engineers.

---

## Why explicit banned phrases

Instruction-based tone guidance ("be professional and direct") produces inconsistent 
results. "Do not use the following phrases" produces consistent ones.

The banned phrases list (`rest assured`, `please don't hesitate`, `unfortunately`, 
`as per`) was built from real output review — these were the phrases that appeared 
most frequently in early outputs and that client-facing reviewers flagged most often 
as undermining the tone.

Negative constraints are more reliable than positive instructions for style control 
because they are easier for the model to verify: a phrase is either present or absent. 
"Be direct" is a judgment call; "do not use this word" is a binary check.

---

## Why the `[REQUIRES HUMAN CONFIRMATION]` pattern exists

This pattern was the most consequential design decision in the framework.

The alternative — asking the model to hedge with phrases like "I believe" or 
"you may want to verify" — produced outputs where uncertainty was present but 
not visually prominent. A CSM under time pressure reads quickly and the hedge 
disappears into the prose.

`[REQUIRES HUMAN CONFIRMATION]` is visually unmissable. It breaks the flow 
of the draft in a way that forces a pause. In a regulated industry where a 
wrong statement about data handling or process could create compliance exposure 
or client distrust, unmissable is the right design choice.

The cost: it can feel heavy-handed in low-stakes contexts. The benefit: it 
eliminates a category of error that is expensive and trust-damaging to fix.

---

## Why the rubric is five points, not more

Early versions of the rubric had eight checks. The team stopped using it by week two.

Five checks can be run in 60 seconds as a genuine habit. Eight checks became a 
form to fill rather than a thinking tool. The five that remained are the ones 
that caught the highest proportion of errors in production.

Evaluation frameworks that are thorough but unused are worse than lightweight 
frameworks that are consistently applied.

---

## Why relationship temperature has three levels, not five

More granularity in the tone calibration variable produced more model variability, 
not more precision. The model's ability to differentiate between "slightly cautious" 
and "moderately cautious" is lower than its ability to differentiate between "stable," 
"cautious," and "strained."

Three levels that produce reliable, consistent calibration are more valuable than 
five levels that produce nuanced but unpredictable output.

---

## Why the adoption playbook covers resistance explicitly

Most AI adoption guides assume buy-in. This one doesn't.

CS teams are often skeptical of AI tools for legitimate reasons: they've seen 
colleagues send bad AI outputs to clients, they've been burned by overhyped tools 
before, they know their client relationships are too important to risk on 
inconsistent outputs.

The playbook addresses this skepticism directly — not by dismissing it, but by 
building the framework around it. The rubric, the evaluation habit, the iteration 
log — these exist because skepticism is right. LLM outputs should not be trusted 
without review. The framework is designed for teams that don't trust LLMs by default, 
and builds trust through demonstrated reliability, not through assertion.

---

## What this framework deliberately does not do

**Automated sending:** No output in this framework goes to a client without human review. 
This is a deliberate design choice, not a technical limitation. In enterprise CS, 
the relationship is the product. Automating client communication without human 
review removes the judgment layer that is the CSM's primary value.

**Model selection automation:** The framework does not automatically route to 
Claude vs. GPT-4. Both work. Claude tends to produce slightly more calibrated 
tone on sensitive escalations; GPT-4 tends to be slightly more concise on 
technical summaries. Both require the same rubric pass. Model preference should 
be a team decision based on your own output review, not a framework prescription.

**Sentiment analysis:** Some CS AI tools analyse client email sentiment before 
drafting. This framework does not. Sentiment analysis adds a processing step, 
creates a false impression of objectivity about something that is inherently 
interpretive, and removes the CSM's own reading of the relationship from the 
loop — which is the most important input to tone calibration.
