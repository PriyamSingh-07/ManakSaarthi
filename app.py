import streamlit as st

st.set_page_config(
    page_title="ManakSaarthi",
    page_icon="M",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root{
  --navy:#0B2942; --navy2:#123E5D; --ink:#17324D; --muted:#6B7F91;
  --saffron:#E98A19; --cream:#F5F7F9; --white:#FFFFFF; --line:#DCE5EC;
  --green:#197A5A; --blue:#2167A5;
}
.stApp{background:var(--cream);color:var(--ink);font-family:'DM Sans',sans-serif}
[data-testid="stToolbar"]{display:none}
[data-testid="stHeader"]{background:rgba(245,247,249,.92)}
.block-container{max-width:1400px;padding:1.8rem 3rem 4rem}
[data-testid="stSidebar"]{background:var(--navy)}
[data-testid="stSidebar"] *{color:#F8FAFC !important}
[data-testid="stSidebar"] .stRadio label{padding:9px 12px;border-radius:8px}
[data-testid="stSidebar"] .stRadio label:hover{background:rgba(255,255,255,.10)}
[data-testid="stSidebar"] hr{border-color:rgba(255,255,255,.15)}
h1,h2,h3{font-family:'Playfair Display',serif !important;color:var(--navy) !important;letter-spacing:-.025em}
h1{font-size:2.55rem !important;margin-bottom:.15rem !important}
h2{font-size:1.75rem !important} h3{font-size:1.2rem !important}
p,.stCaption{color:var(--muted)}
.stTextInput input,.stTextArea textarea{
  border-radius:9px;border-color:#CAD6DF;background:#fff;color:#17324D !important;
  -webkit-text-fill-color:#17324D;caret-color:#17324D
}
.stTextInput input:focus,.stTextArea textarea:focus{
  border-color:var(--saffron);box-shadow:0 0 0 1px var(--saffron)
}
.stButton>button,.stDownloadButton>button{
  border-radius:8px;border:1px solid var(--navy);font-weight:600;padding:.58rem 1rem
}
.stButton>button[kind="primary"],.stDownloadButton>button[kind="primary"]{
  background:var(--navy);border-color:var(--navy);color:white
}
.stButton>button[kind="primary"]:hover,.stDownloadButton>button[kind="primary"]:hover{
  background:var(--navy2);border-color:var(--navy2)
}
div[data-testid="stVerticalBlockBorderWrapper"]{
  border:1px solid var(--line) !important;border-radius:14px !important;background:#fff;
  box-shadow:0 5px 20px rgba(16,42,67,.045)
}
div[data-testid="stMetric"]{
  background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;
  box-shadow:0 3px 14px rgba(16,42,67,.035)
}
div[data-testid="stMetricLabel"]{color:var(--muted);font-size:.78rem;text-transform:uppercase;letter-spacing:.07em}
div[data-testid="stMetricValue"]{color:var(--navy);font-family:'Playfair Display',serif}
div[data-baseweb="tab-list"]{gap:1rem}
button[data-baseweb="tab"]{font-weight:600;color:var(--muted)}
button[data-baseweb="tab"][aria-selected="true"]{color:var(--navy)}
.eyebrow{color:var(--saffron);font-size:.72rem;letter-spacing:.15em;text-transform:uppercase;font-weight:700;margin-bottom:.4rem}
.brand{font-family:'Playfair Display',serif;font-size:1.45rem;font-weight:700;color:#fff;margin-bottom:0}
.brand-sub{font-size:.72rem;color:#B9CAD7 !important;margin-top:-2px}
.hero{
  background:linear-gradient(115deg,#09263D 0%,#104262 58%,#1C5975 100%);
  border-radius:20px;padding:2.2rem 2.4rem;color:#fff;margin-bottom:1.8rem;
  box-shadow:0 15px 34px rgba(9,38,61,.18)
}
.hero h1{color:#fff !important;margin:0 !important}
.hero p{color:#D8E6EF;font-size:1rem;margin:.55rem 0 0;max-width:760px}
.hero-chip{
  display:inline-block;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.08);
  color:#E8F1F6;padding:.34rem .65rem;border-radius:999px;font-size:.75rem;margin-right:.35rem
}
.section-label{font-size:.73rem;text-transform:uppercase;letter-spacing:.13em;color:var(--saffron);font-weight:700;margin:1.7rem 0 .7rem}
.card-title{font-weight:700;color:var(--navy);font-size:1.05rem}
.card-copy{color:var(--muted);font-size:.9rem;line-height:1.45}
.badge{
  display:inline-block;border-radius:999px;padding:.22rem .55rem;font-size:.7rem;font-weight:700;
  background:#E8F4EF;color:var(--green)
}
.badge-blue{background:#EAF2FA;color:var(--blue)}
.score{font-size:1.7rem;font-weight:700;color:var(--navy);font-family:'Playfair Display',serif}
.result-head{display:flex;justify-content:space-between;gap:1rem;align-items:flex-start}
.search-box{background:#fff;border:1px solid var(--line);border-radius:14px;padding:1rem 1.1rem;margin-bottom:1rem}
.login-wrap{
  max-width:1060px;margin:5vh auto 0;background:#fff;border:1px solid var(--line);
  border-radius:22px;overflow:hidden;box-shadow:0 20px 55px rgba(16,42,67,.11)
}
.login-brand-panel{
  min-height:510px;padding:3.2rem 2.7rem;color:#fff;
  background:radial-gradient(circle at 90% 10%,rgba(233,138,25,.32),transparent 30%),
    linear-gradient(145deg,#09263D 0%,#104262 60%,#1C5975 100%);
}
.login-brand-panel .eyebrow{color:#F7B45F}
.login-brand-panel h1{color:#fff !important;font-size:2.35rem !important;line-height:1.12;margin:3.5rem 0 1rem !important}
.login-brand-panel p{color:#D8E6EF;line-height:1.65}
.login-logo{font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:700;color:#fff}
.login-form-panel{padding:3.2rem 3rem}
.login-form-panel h2{margin:.3rem 0 .35rem}
.login-form-panel [data-testid="stForm"]{border:0;padding:0}
.login-tag{display:inline-block;padding:.35rem .65rem;border-radius:999px;background:rgba(255,255,255,.1);color:#E8F1F6;font-size:.78rem}
.small-note{font-size:.78rem;color:var(--muted)}
@media(max-width:760px){.login-brand-panel{min-height:0;padding:2rem}.login-brand-panel h1{margin:2rem 0 .7rem !important}.login-form-panel{padding:2rem}}
</style>
""",
    unsafe_allow_html=True,
)

DEMO = [
    {
        "no": "IS 2925:1984",
        "title": "Industrial Safety Helmets",
        "scope": "Protective helmets used in industrial work.",
        "version": "1984",
        "cert": "BIS certification required",
        "category": "Safety",
    },
    {
        "no": "IS 2062:2011",
        "title": "Hot Rolled Structural Steel",
        "scope": "Structural steel products for construction.",
        "version": "2011",
        "cert": "BIS certification as applicable",
        "category": "Materials",
    },
    {
        "no": "IS 800:2007",
        "title": "General Construction in Steel",
        "scope": "Design, fabrication and erection of steel structures.",
        "version": "2007",
        "cert": "Not generally a product standard",
        "category": "Construction",
    },
]

for key, value in {
    "signed_in": False,
    "page": "Dashboard",
    "saved": [],
    "query_submitted": False,
    "recommendation_query": "",
}.items():
    st.session_state.setdefault(key, value)


def details(x, score=92):
    st.markdown(
        f"""
        <div class="result-head">
          <div>
            <div class="eyebrow">{x['category']} standard</div>
            <h3 style="margin:0">{x['no']} — {x['title']}</h3>
          </div>
          <div style="text-align:right">
            <div class="score">{score}%</div>
            <div class="small-note">relevance</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    a, b, c = st.columns(3)
    a.metric("Relevance", f"{score}%")
    b.metric("Published version", x["version"])
    c.metric("Catalogue status", "Active")
    st.write("**Scope:**", x["scope"])
    st.write("**Certification:**", x["cert"])
    st.caption("Amendments: verify the current BIS publication before final tender release.")
    st.caption("Related reference: IS 800:2007")


def go(page):
    st.session_state.page = page
    st.rerun()


if not st.session_state.signed_in:
    brand_col, form_col = st.columns([1.05, 1], gap="small")
    with brand_col:
        st.markdown(
            """
            <div class="login-wrap login-brand-panel">
              <div class="login-logo">मानकसारथी</div>
              <div class="eyebrow" style="margin-top:1.4rem">Procurement intelligence</div>
              <h1>Make every specification count.</h1>
              <p>Find relevant Indian Standards and prepare clearer, more confident procurement requirements.</p>
              <span class="login-tag">Indian Standards · Procurement workspace</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with form_col:
        with st.container(border=True):
            st.markdown('<div class="eyebrow">Welcome back</div><h2>Sign in to ManakSaarthi</h2>', unsafe_allow_html=True)
            st.caption("Use your department account to continue to your workspace.")
            with st.form("login"):
                st.text_input("Official email", placeholder="name@department.gov.in")
                st.text_input("Password", type="password", placeholder="Enter your password")
                if st.form_submit_button("Sign in", type="primary", use_container_width=True):
                    st.session_state.signed_in = True
                    st.rerun()
            st.markdown('<div class="small-note">Prototype access · any email and password will continue.</div>', unsafe_allow_html=True)
    st.stop()


with st.sidebar:
    st.markdown('<div class="brand">मानकसारथी</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="brand-sub">Indian Standards Recommendation & Procurement Assistant</div>',
        unsafe_allow_html=True,
    )
    st.divider()
    pages = ["Dashboard", "New Recommendation", "Search Standards", "History", "Reports", "Profile"]
    st.session_state.page = st.radio(
        "Navigation",
        pages,
        index=pages.index(st.session_state.page),
        label_visibility="collapsed",
    )
    st.divider()
    st.caption("SIGNED IN AS")
    st.markdown("**Procurement Officer**")
    st.caption("Procurement Department")
    if st.button("Sign out", use_container_width=True):
        st.session_state.signed_in = False
        st.session_state.page = "Dashboard"
        st.rerun()


p = st.session_state.page

if p == "Dashboard":
    st.markdown(
        """
        <div class="hero">
          <div class="eyebrow">Procurement workspace</div>
          <h1>Standards intelligence for better specifications.</h1>
          <p>Identify relevant Indian Standards, allied references and certification requirements before you publish a tender.</p>
          <div style="margin-top:1.15rem">
            <span class="hero-chip">Semantic recommendations</span>
            <span class="hero-chip">Allied standards</span>
            <span class="hero-chip">Certification checks</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-label">Start a task</div>', unsafe_allow_html=True)
    cards = [
        ("New Recommendation", "Describe a product or tender requirement.", "Generate a structured standards shortlist."),
        ("Search Standards", "Browse by IS number, product or requirement.", "Explore catalogue entries and scopes."),
        ("History", "Review saved recommendations and queries.", "Keep procurement research organised."),
    ]
    cols = st.columns(3)
    for col, (title, desc, copy) in zip(cols, cards):
        with col.container(border=True):
            st.markdown(f'<div class="card-title">{title}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card-copy">{desc}<br>{copy}</div>', unsafe_allow_html=True)
            st.write("")
            if st.button("Open workspace", key=f"dash_{title}", use_container_width=True):
                go(title)

    st.markdown('<div class="section-label">Workspace overview</div>', unsafe_allow_html=True)
    a, b, c, d = st.columns(4)
    a.metric("Recommendations", "18", "+4 this month")
    b.metric("Saved standards", len(st.session_state.saved))
    c.metric("Reports generated", "7")
    d.metric("Catalogue entries", "3", "demo dataset")

    st.markdown('<div class="section-label">How ManakSaarthi helps</div>', unsafe_allow_html=True)
    x, y, z = st.columns(3)
    with x.container(border=True):
        st.markdown("### 01 · Understand")
        st.write("Read natural-language product descriptions and technical requirements.")
    with y.container(border=True):
        st.markdown("### 02 · Connect")
        st.write("Surface primary, allied, normative and test-method references.")
    with z.container(border=True):
        st.markdown("### 03 · Verify")
        st.write("Review versions, amendments and applicable certification requirements.")

elif p == "New Recommendation":
    st.markdown('<div class="eyebrow">Recommendation engine</div>', unsafe_allow_html=True)
    st.title("New standards recommendation")
    st.caption("Enter the procurement requirement in plain language. This prototype displays a representative result set.")

    with st.form("rec"):
        item = st.text_input(
            "Product / item description",
            placeholder="Example: industrial safety helmet",
        )
        specification = st.text_area(
            "Technical specification or natural-language requirement",
            height=145,
            placeholder="Describe material, application, performance, safety or installation requirements...",
        )
        uploaded = st.file_uploader(
            "Tender document (optional)",
            type=["pdf", "docx"],
            help="Document processing can be connected to the existing backend later.",
        )
        submitted = st.form_submit_button("Find relevant standards", type="primary", use_container_width=True)

    if submitted:
        st.session_state.recommendation_query = " ".join(
            value.strip() for value in (item, specification) if value.strip()
        )
        st.session_state.query_submitted = bool(st.session_state.recommendation_query)
        if st.session_state.query_submitted:
            st.success("Recommendation workspace prepared from your description.")
        else:
            st.warning("Enter a product description or technical requirement to continue.")
    if st.session_state.query_submitted:
        st.caption(f"Requirement: {st.session_state.recommendation_query}")
        main, related, safety = st.tabs(
            ["Primary IS Standards", "Allied & Normative References", "Safety & Certification"]
        )
        with main:
            st.caption("Ranked by relevance in the demonstration dataset.")
            for i, x in enumerate(DEMO):
                with st.container(border=True):
                    details(x, 96 - i * 5)
                    if st.button("Save recommendation", key=f"save_{x['no']}"):
                        if x not in st.session_state.saved:
                            st.session_state.saved.append(x)
                        st.toast("Saved to your workspace.")
        with related:
            st.info("Allied standards, normative references, terminology and test methods will be surfaced here when the recommendation engine is connected.")
        with safety:
            st.info("Applicable BIS certification, safety requirements and scheme references will be displayed here when certification rules are connected.")

elif p == "Search Standards":
    st.markdown('<div class="eyebrow">Standards catalogue</div>', unsafe_allow_html=True)
    st.title("Search Indian Standards")
    st.caption("Search by IS number, product name, technical requirement or standard family.")
    with st.container(border=True):
        q = st.text_input(
            "Search catalogue",
            placeholder="Try: IS 2925, safety helmet, structural steel...",
        )
    query = q.strip().casefold()
    matches = [
        x for x in DEMO
        if query == "" or query in " ".join(x.values()).casefold()
    ]
    if not matches:
        st.info("No standards match that search. Try an IS number, product name or category.")
    for x in matches:
        with st.container(border=True):
            details(x, 89)

elif p == "History":
    st.markdown('<div class="eyebrow">Procurement workspace</div>', unsafe_allow_html=True)
    st.title("History & saved standards")
    st.caption("Keep recommendations you may need while drafting or reviewing procurement specifications.")
    st.subheader("Saved recommendations")
    if st.session_state.saved:
        for x in st.session_state.saved:
            with st.container(border=True):
                st.markdown(f"**{x['no']} — {x['title']}**")
                st.caption(x["scope"])
    else:
        st.info("No saved recommendations yet. Save a result from the recommendation workspace.")

elif p == "Reports":
    st.markdown('<div class="eyebrow">Export centre</div>', unsafe_allow_html=True)
    st.title("Recommendation report")
    st.caption("Review a clean report preview before exporting it for procurement records.")
    report = """MANAKSAARTHI — INDIAN STANDARDS RECOMMENDATION REPORT

Procurement requirement
Industrial safety helmet

Recommended standards
• IS 2925:1984 — Industrial Safety Helmets
• IS 2062:2011 — Hot Rolled Structural Steel
• IS 800:2007 — General Construction in Steel

Review notes
• Verify the current BIS publication and amendments.
• Confirm certification applicability before tender release.
• Review allied and normative references.
"""
    left, right = st.columns([1.2, 1])
    with left:
        st.text_area("Report preview", report, height=310)
    with right:
        with st.container(border=True):
            st.markdown("### Export")
            st.write("Generate a plain-text procurement research record from the current prototype results.")
            st.download_button(
                "Download report",
                report,
                "manaksaarthi_recommendation_report.txt",
                "text/plain",
                type="primary",
                use_container_width=True,
            )

else:
    st.markdown('<div class="eyebrow">Account workspace</div>', unsafe_allow_html=True)
    st.title("Profile")
    st.caption("Manage the procurement officer profile shown in the workspace.")
    with st.container(border=True):
        st.text_input("Full name", value="Procurement Officer")
        st.text_input("Department", value="Procurement Department")
        st.text_input("Official email", value="officer@department.gov.in")
        st.button("Save profile", type="primary")
