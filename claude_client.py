import anthropic
import os
from dotenv import load_dotenv

load_dotenv()


def get_client():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found.")
    return anthropic.Anthropic(api_key=api_key)


def generate_response(prompt: str) -> str:
    client = get_client()
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def evaluate_response(original_context: str, generated_response: str, use_case: str) -> dict:
    client = get_client()
    eval_prompt = f"""You are evaluating an AI-generated customer success communication.

USE CASE: {use_case}

ORIGINAL CONTEXT:
{original_context}

GENERATED RESPONSE:
{generated_response}

Return ONLY a JSON object, no markdown, no extra text:

{{
  "factual_accuracy": {{"score": 8, "feedback": "one sentence"}},
  "tone_calibration": {{"score": 8, "feedback": "one sentence"}},
  "completeness": {{"score": 8, "feedback": "one sentence"}},
  "length_and_format": {{"score": 8, "feedback": "one sentence"}},
  "placeholder_check": {{"score": 8, "feedback": "one sentence"}},
  "overall": {{"score": 8, "verdict": "Send after review", "top_improvement": "one sentence"}}
}}"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": eval_prompt}],
    )

    import json
    raw = message.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())


def load_prompt_template(use_case: str, user_input: str) -> str:
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
