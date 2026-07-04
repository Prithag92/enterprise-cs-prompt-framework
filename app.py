import streamlit as st
from claude_client import generate_response, evaluate_response, load_prompt_template

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CS AI Assistant",
    page_icon="📨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  /* Google Fonts */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=DM+Serif+Display&display=swap');

  html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
  }

  /* Sidebar */
  [data-testid="stSidebar"] {
    background-color: #0f1923;
    border-right: 1px solid #1e2d3d;
  }
  [data-testid="stSidebar"] * {
    color: #c8d8e8 !important;
  }
  [data-testid="stSidebar"] .sidebar-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #4a6fa5 !important;
    margin-bottom: 0.25rem;
  }

  /* Main background */
  .main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 900px;
  }

  /* Header */
  .app-header {
    margin-bottom: 2rem;
  }
  .app-header h1 {
    font-family: 'DM Serif Display', serif;
    font-size: 2rem;
    font-weight: 400;
    color: #0f1923;
    margin: 0;
    line-height: 1.2;
  }
  .app-header p {
    color: #64748b;
    margin: 0.4rem 0 0 0;
    font-size: 0.95rem;
  }
  .header-rule {
    border: none;
    border-top: 2px solid #1a56db;
    width: 48px;
    margin: 0.75rem 0 0 0;
  }

  /* Use-case pill buttons */
  .stRadio > div {
    flex-direction: column;
    gap: 0.4rem;
  }
  .stRadio label {
    background: #1e2d3d;
    border: 1px solid #2d4a6a;
    border-radius: 6px;
    padding: 0.6rem 1rem;
    cursor: pointer;
    transition: all 0.15s ease;
    font-size: 0.88rem;
    color: #c8d8e8 !important;
  }
  .stRadio label:hover {
    background: #1a3a5c;
    border-color: #1a56db;
  }

  /* Text area */
  .stTextArea textarea {
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
    border: 1.5px solid #e2e8f0;
    border-radius: 8px;
    background: #fafbfc;
    transition: border-color 0.15s;
  }
  .stTextArea textarea:focus {
    border-color: #1a56db;
    box-shadow: 0 0 0 3px rgba(26,86,219,0.08);
  }

  /* Generate button */
  .stButton > button {
    background: #1a56db;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.65rem 2rem;
    font-weight: 600;
    font-size: 0.95rem;
    letter-spacing: 0.01em;
    transition: background 0.15s ease;
    width: 100%;
  }
  .stButton > button:hover {
    background: #1648c0;
  }

  /* Output card */
  .output-card {
    background: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-radius: 10px;
    padding: 1.5rem 1.75rem;
    margin-top: 1.25rem;
    font-size: 0.95rem;
    line-height: 1.7;
    color: #1e293b;
    white-space: pre-wrap;
    font-family: 'Inter', sans-serif;
  }

  /* Section label */
  .section-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #94a3b8;
    margin-bottom: 0.5rem;
  }

  /* Score cards */
  .score-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 0.75rem;
    margin-top: 0.75rem;
  }
  .score-card {
    background: #f8fafc;
    border: 1.5px solid #e2e8f0;
    border-radius: 8px;
    padding: 0.9rem 1rem;
  }
  .score-card .sc-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #64748b;
    margin-bottom: 0.3rem;
  }
  .score-card .sc-score {
    font-size: 1.6rem;
    font-weight: 700;
    font-family: 'DM Serif Display', serif;
    line-height: 1;
  }
  .score-card .sc-feedback {
    font-size: 0.75rem;
    color: #64748b;
    margin-top: 0.3rem;
    line-height: 1.4;
  }
  .score-high { color: #16a34a; }
  .score-mid  { color: #d97706; }
  .score-low  { color: #dc2626; }

  /* Verdict badge */
  .verdict-badge {
    display: inline-block;
    padding: 0.35rem 0.9rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
  }
  .verdict-send    { background: #dcfce7; color: #15803d; }
  .verdict-revise  { background: #fef9c3; color: #854d0e; }
  .verdict-rewrite { background: #fee2e2; color: #b91c1c; }

  /* Tip box */
  .tip-box {
    background: #eff6ff;
    border-left: 3px solid #1a56db;
    border-radius: 0 6px 6px 0;
    padding: 0.75rem 1rem;
    font-size: 0.82rem;
    color: #1e40af;
    margin-top: 0.5rem;
  }

  /* Hide Streamlit chrome */
  #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-label">Use Case</div>', unsafe_allow_html=True)
    use_case = st.radio(
        label="",
        options=[
            "Support Response",
            "Escalation Summary",
            "Proactive Status Update",
            "Knowledge / FAQ Answer",
        ],
        label_visibility="collapsed",
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="sidebar-label">About</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:0.8rem; line-height:1.6; color:#8aacc8;">
    Built on the <strong style="color:#c8d8e8;">Enterprise CS Prompt Framework</strong> —
    production-tested across 5 enterprise FinTech accounts.<br><br>
    Every output runs through a <strong style="color:#c8d8e8;">5-point evaluation rubric</strong>
    before you send.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="sidebar-label">Context tips</div>', unsafe_allow_html=True)

    tips = {
        "Support Response": "Include: client name, account tier, issue description, SLA status, resolution status, ETA if known.",
        "Escalation Summary": "Paste the full raw email thread or ticket history. Include contract value and urgency level if known.",
        "Proactive Status Update": "Include: what's affected, when it started, current status, root cause (confirmed/investigating), relationship temperature (stable/cautious/strained).",
        "Knowledge / FAQ Answer": "Include: the client's exact question, their familiarity with the product, and paste the relevant knowledge base / documentation excerpt.",
    }
    st.markdown(f'<div class="tip-box">{tips[use_case]}</div>', unsafe_allow_html=True)


# ── Main area ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
  <h1>Enterprise CS AI Assistant</h1>
  <p>AI-drafted communications for enterprise customer success — reviewed, not raw.</p>
  <hr class="header-rule">
</div>
""", unsafe_allow_html=True)

labels = {
    "Support Response":        "Paste the support ticket, client email, or incident details",
    "Escalation Summary":      "Paste the full email thread or ticket history for internal handoff",
    "Proactive Status Update": "Describe the ongoing incident — what's affected, current status, client context",
    "Knowledge / FAQ Answer":  "Paste the client's question + relevant product documentation or knowledge",
}

st.markdown(f'<div class="section-label">{use_case} — Context Input</div>', unsafe_allow_html=True)
user_input = st.text_area(
    label="",
    placeholder=labels[use_case],
    height=220,
    label_visibility="collapsed",
)

col_btn, col_spacer = st.columns([1, 2])
with col_btn:
    generate_clicked = st.button("Generate Draft", use_container_width=True)


# ── Generation ─────────────────────────────────────────────────────────────────
if generate_clicked:
    if not user_input.strip():
        st.warning("Add some context above before generating.")
    else:
        with st.spinner("Drafting with Claude…"):
            try:
                prompt = load_prompt_template(use_case, user_input)
                result = generate_response(prompt)
                st.session_state["result"] = result
                st.session_state["use_case"] = use_case
                st.session_state["input"] = user_input
                st.session_state["eval"] = None  # reset eval on new generation
            except Exception as e:
                st.error(f"Generation failed: {e}")


# ── Output ─────────────────────────────────────────────────────────────────────
if "result" in st.session_state and st.session_state.get("use_case") == use_case:
    result = st.session_state["result"]

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Generated Draft</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="output-card">{result}</div>', unsafe_allow_html=True)

    col_dl, col_eval, col_spacer2 = st.columns([1, 1, 2])
    with col_dl:
        st.download_button(
            label="⬇ Download",
            data=result,
            file_name=f"{use_case.lower().replace(' ', '_')}_draft.txt",
            mime="text/plain",
            use_container_width=True,
        )
    with col_eval:
        eval_clicked = st.button("Run Rubric Check →", use_container_width=True)

    if eval_clicked:
        with st.spinner("Evaluating against the 5-point rubric…"):
            try:
                eval_result = evaluate_response(
                    st.session_state["input"], result, use_case
                )
                st.session_state["eval"] = eval_result
            except Exception as e:
                st.error(f"Evaluation failed: {e}")

    # ── Evaluation results ─────────────────────────────────────────────────────
    if st.session_state.get("eval"):
        ev = st.session_state["eval"]
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-label">Rubric Evaluation</div>', unsafe_allow_html=True)

        def score_class(s):
            if s >= 8: return "score-high"
            if s >= 6: return "score-mid"
            return "score-low"

        dimensions = [
            ("Factual Accuracy",   ev["factual_accuracy"]),
            ("Tone Calibration",   ev["tone_calibration"]),
            ("Completeness",       ev["completeness"]),
            ("Length & Format",    ev["length_and_format"]),
            ("Placeholder Check",  ev["placeholder_check"]),
        ]

        cards_html = '<div class="score-grid">'
        for label, dim in dimensions:
            s = dim["score"]
            cards_html += f"""
            <div class="score-card">
              <div class="sc-label">{label}</div>
              <div class="sc-score {score_class(s)}">{s}<span style="font-size:0.9rem;color:#94a3b8;">/10</span></div>
              <div class="sc-feedback">{dim['feedback']}</div>
            </div>"""
        cards_html += "</div>"
        st.markdown(cards_html, unsafe_allow_html=True)

        # Overall verdict
        overall = ev["overall"]
        verdict_map = {
            "Send after review":   ("verdict-send",    "✅ Send after review"),
            "Revise before sending": ("verdict-revise", "⚠️ Revise before sending"),
            "Rewrite manually":    ("verdict-rewrite", "❌ Rewrite manually"),
        }
        v_key = overall.get("verdict", "Revise before sending")
        v_class, v_label = verdict_map.get(v_key, ("verdict-revise", v_key))

        st.markdown("<br>", unsafe_allow_html=True)
        overall_score = overall.get("score", "–")
        top_fix = overall.get("top_improvement", "")

        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:1rem; flex-wrap:wrap;">
          <span class="section-label" style="margin:0;">Overall</span>
          <span style="font-family:'DM Serif Display',serif; font-size:1.6rem; color:#0f1923; font-weight:700;">{overall_score}<span style="font-size:1rem; color:#94a3b8;">/10</span></span>
          <span class="verdict-badge {v_class}">{v_label}</span>
        </div>
        {"<div class='tip-box' style='margin-top:0.75rem;'>💡 " + top_fix + "</div>" if top_fix else ""}
        """, unsafe_allow_html=True)
