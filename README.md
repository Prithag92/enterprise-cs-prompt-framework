# Enterprise CS AI Assistant

A web application that turns raw incident details, email threads, and client questions into polished, review-ready communications — using Claude (Anthropic) and the Enterprise CS Prompt Framework.

**Live demo:** `https://your-app.streamlit.app` *(add after deployment)*

---

## What it does

| Use Case | Input | Output |
|---|---|---|
| **Support Response** | Ticket details, client email | Draft reply email, 150–200 words |
| **Escalation Summary** | Raw email thread or ticket history | Structured internal handoff document |
| **Proactive Status Update** | Incident context + relationship temperature | Proactive client update email |
| **Knowledge / FAQ Answer** | Client question + knowledge base excerpt | Grounded, accurate client-facing answer |

Every output is evaluated against a **5-point rubric** (factual accuracy, tone, completeness, format, placeholder check) before you send.

---

## Tech stack

- **Python 3.10+**
- **Streamlit** — UI
- **Anthropic Claude** (`claude-sonnet-4-6`) — generation and evaluation
- **Prompt engineering framework** — 4 production-tested templates

---

## Local setup

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/enterprise-cs-prompt-framework.git
cd enterprise-cs-prompt-framework
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

```bash
cp .env.example .env
```

Edit `.env` and add your Anthropic API key:

```
ANTHROPIC_API_KEY=sk-ant-...
```

Get one at: https://console.anthropic.com

### 4. Run locally

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

---

## Deploy to Streamlit Cloud (free)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Set the main file path to `app.py`
4. Under **Settings → Secrets**, add:

```toml
ANTHROPIC_API_KEY = "sk-ant-your-key-here"
```

5. Deploy — you'll get a public URL at `https://your-app-name.streamlit.app`

---

## How the evaluation rubric works

After generating a draft, click **Run Rubric Check**. Claude evaluates the output on:

1. **Factual accuracy** — are all claims grounded in the context you provided?
2. **Tone calibration** — appropriate for enterprise FinTech? No weak/filler phrases?
3. **Completeness** — does the client know what happens next and when?
4. **Length & format** — right length, no unnecessary preamble?
5. **Placeholder check** — any `[REQUIRES INPUT]` or `[REQUIRES HUMAN CONFIRMATION]` markers unresolved?

**Verdict:** Send after review / Revise before sending / Rewrite manually

---

## Repo structure

```
enterprise-cs-prompt-framework/
│
├── app.py                    ← Streamlit UI
├── claude_client.py          ← Anthropic API wrapper + prompt loader
├── requirements.txt
├── .env.example              ← Copy to .env for local dev
│
├── prompts/
│   ├── support_response.txt
│   ├── escalation_summary.txt
│   ├── status_update.txt
│   └── knowledge_retrieval.txt
│
└── .streamlit/
    └── secrets.toml.example  ← For Streamlit Cloud deployment
```

---

## Design decisions

- **Claude over OpenAI** — the original prompt framework was built and tested on Claude. Using the same model in the app keeps behaviour consistent.
- **Two-call architecture** — generation and evaluation are separate API calls. This keeps each prompt focused and produces more reliable evaluation scores.
- **Human in the loop always** — no output is sent automatically. The app drafts; the CSM decides.

---

## Author

**Pritha Ghosh** — AI Customer Success Leader, FinTech SaaS
[linkedin.com/in/pritha-ghosh1](https://linkedin.com/in/pritha-ghosh1)
