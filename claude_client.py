import anthropic
import os
from dotenv import load_dotenv

load_dotenv()


def get_client():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found. Add it to your .env file.")
    return anthropic.Anthropic(api_key=api_key)


def generate_response(prompt: str) -> str:
    """Generate a CS response using Claude."""
    client = get_client()
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def evaluate_response(original_context: str, generated_response: str, use_case: str) -> dict:
    """
    Run the 5-point evaluation rubric on a generated response.
    Returns scores and brief feedback for each dimension.
    """
    client = get_client()

    eval_prompt = f"""You are evaluating an AI-generated customer success communication against a professional rubric.

USE CASE: {use_case}

ORIGINAL CONTEXT PROVIDED:
{original_context}

GENERATED RESPONSE:
{generated_response}

Evaluate the response on EXACTLY these 5 dimensions. Return ONLY a JSON object, no markdown, no explanation outside the JSON:

{{
  "factual_accuracy": {{
    "score": <integer 1-10>,
    "feedback": "<one sentence: what was accurate or what was speculated beyond the context>"
  }},
  "tone_calibration": {{
    "score": <integer 1-10>,
    "feedback": "<one sentence: is the tone appropriate for enterprise FinTech? any weak/filler phrases?>"
  }},
  "completeness": {{
    "score": <integer 1-10>,
    "feedback": "<one sentence: does the client know what happens next and when?>"
  }},
  "length_and_format": {{
    "score": <integer 1-10>,
    "feedback": "<one sentence: appropriate length? no unnecessary preamble or padding?>"
  }},
  "placeholder_check": {{
    "score": <integer 1-10>,
    "feedback": "<one sentence: any [REQUIRES INPUT] or [REQUIRES HUMAN CONFIRMATION] placeholders that need resolving?>"
  }},
  "overall": {{
    "score": <integer 1-10>,
    "verdict": "<'Send after review' OR 'Revise before sending' OR 'Rewrite manually'>",
    "top_improvement": "<single most important thing to fix, if any>"
  }}
}}"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": eval_prompt}],
    )

    import json
    raw = message.content[0].text.strip()
    # Strip markdown code fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())


def load_prompt_template(use_case: str, user_input: str) -> str:
    """Load the correct prompt template and inject user input."""
   template_map = {
    "Support Response": "prompts/support/support-response-v3.md",
    "Escalation Summary": "prompts/escalation/escalation-summary-v2.md",
    "Proactive Status Update": "prompts/status/status-update-v2.md",
    "Knowledge / FAQ Answer": "prompts/knowledge/knowledge-retrieval-v2.md",
}
    filepath = template_map.get(use_case)
    if not filepath or not os.path.exists(filepath):
        raise FileNotFoundError(f"Prompt template not found for: {use_case}")

    with open(filepath, "r") as f:
        template = f.read()

    return template.replace("{input}", user_input)
