
from __future__ import annotations
import base64
from pathlib import Path
import streamlit as st
# ---------------- CONFIG ---------------- #
APP_DIR = Path(__file__).resolve().parent
PROFILE_IMAGE = APP_DIR / "profile.png"
PLACEHOLDER_AVATAR = (
    "https://ui-avatars.com/api/?name=Meet+Sharma&size=360&background=2563eb&color=fff&bold=true"
)
PROFILE = {
    "name": "Meet Sharma",
    "tagline": "B.Tech CSE · Python & Java Developer · FastAPI · Backend Systems",
    "bio": (
        "Computer Science undergraduate passionate about building scalable applications, "
        "backend systems, real-world projects, and data-driven solutions."
    ),
    "email": "meetsharma1569@gmail.com",
    "location": "India",
}
METRICS = [
    ("4+", "Projects", "🚀"),
    ("13+", "Skills", "💻"),
    ("3", "Internships", "🏢"),
]
SKILLS = [
    "Java",
    "Python",
    "FastAPI",
    "Streamlit",
    "SQLite",
    "MySQL",
    "Power BI",
    "Pandas",
    "NumPy",
    "Git",
    "Matplotlib",
    "OOP",
    "Data Structures",
]
EXPERIENCE = [
    {
        "role": "Python Intern",
        "org": "Ethereal Softech Pvt. Ltd.",
        "period": "MAY,2026 – Present",
        "points": [
            "Built data pipelines and automation scripts with Python.",
            "Worked with APIs, file handling, and reporting workflows.",
        ],
    },
]
EDUCATION = [
    {
        "degree": "B.Tech — Computer Science & Engineering",
        "school": "Undergraduate program",
        "period": "2023-2027",
        "note": "Coursework: DSA, OOP, DBMS, software engineering.",
    },
]
PROJECTS = [
    {
        "title": "✅ Todo Pro",
        "description": (
            "Full-stack style task manager with login/register, bcrypt password hashing, "
            "SQLite persistence, priority filters, and per-user task lists."
        ),
        "tech": "Python · Streamlit · SQLite · bcrypt",
        "demo": None,
        "github": "https://github.com/meetsharma14",
    },

    {
        "title": "📄 ATS Resume Checker",
        "description": (
            "ATS resume analyzer comparing resumes to job descriptions via keyword extraction "
            "and cosine similarity. Supports PDF/DOCX with ranking and missing keywords."
        ),
        "tech": "Python · Streamlit · Scikit-learn · NLP · pdfplumber · python-docx",
        "demo": None,
        "github": None,
    },
    {
        "title": "💰 EMI Calculator",
        "description": (
            "Desktop app calculating loan EMI from user inputs using standard financial formulas."
        ),
        "tech": "Python · Tkinter · OpenPyXL · PIL",
        "demo": None,
        "github": None,
    },
    {
        "title": "✈ Travel Booking System",
        "description": (
            "Console booking system with structured workflows, REST integration, and JSON handling."
        ),
        "tech": "Java · HttpClient · REST · JSON · org.json",
        "demo": None,
        "github": None,
    },
]
LINKS = [
    ("GitHub", "https://github.com/meetsharma14"),
    ("LinkedIn", "https://linkedin.com/in/meet-sharma-304956274"),
    ("LeetCode", "https://leetcode.com/u/SqVzfRkZOb/"),
]
NAV = [
    ("Home", "home"),
    ("About", "about"),
    ("Skills", "skills"),
    ("Projects", "projects"),
    ("Contact", "contact"),
]
# ---------------- HELPERS ---------------- #
def image_to_data_uri(path: Path) -> str | None:
    if not path.is_file():
        return None
    try:
        raw = path.read_bytes()
        b64 = base64.b64encode(raw).decode()
        suffix = path.suffix.lower().lstrip(".") or "png"
        mime = "jpeg" if suffix in {"jpg", "jpeg"} else suffix
        return f"data:image/{mime};base64,{b64}"
    except OSError:
        return None
def profile_src() -> str:
    data_uri = image_to_data_uri(PROFILE_IMAGE)
    return data_uri if data_uri else PLACEHOLDER_AVATAR
def inject_css() -> None:
    st.markdown(
        """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; height: 0; }
.stApp {
  background:
    radial-gradient(circle at 12% 8%, #2563eb33, transparent 32%),
    radial-gradient(circle at 88% 92%, #7c3aed33, transparent 32%),
    linear-gradient(135deg, #020617, #0f172a 45%, #1e293b);
  color: #e2e8f0;
}
.block-container { max-width: 1100px; padding-top: 1.5rem; padding-bottom: 3rem; }
.section-title {
  font-size: 1.75rem;
  font-weight: 600;
  margin: 2rem 0 1.25rem;
  background: linear-gradient(90deg, #93c5fd, #c4b5fd);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.hero {
  padding: 3.5rem 2rem;
  border-radius: 28px;
  background: rgba(255,255,255,.05);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255,255,255,.1);
  text-align: center;
  margin-bottom: 1.5rem;
  box-shadow: 0 20px 50px rgba(15,23,42,.45);
}
.profile-img {
  width: 170px; height: 170px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid #60a5fa;
  margin-bottom: 1.25rem;
  box-shadow: 0 0 40px rgba(96,165,250,.45);
  transition: transform .35s ease, box-shadow .35s ease;
}
.profile-img:hover {
  transform: scale(1.04);
  box-shadow: 0 0 55px rgba(124,58,237,.75);
}
.name {
  font-size: clamp(2rem, 5vw, 3.2rem);
  font-weight: 700;
  line-height: 1.15;
  background: linear-gradient(90deg, #60a5fa, #818cf8, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.tagline { color: #94a3b8; font-weight: 500; margin-top: .5rem; }
.bio { color: #cbd5e1; max-width: 640px; margin: 1rem auto 0; line-height: 1.65; }
.card {
  background: rgba(255,255,255,.05);
  padding: 1.4rem 1.5rem;
  border-radius: 18px;
  backdrop-filter: blur(16px);
  border: 1px solid rgba(255,255,255,.08);
  transition: transform .3s ease, box-shadow .3s ease, border-color .3s ease;
  margin-bottom: 1rem;
  height: 100%;
}
.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 32px rgba(37,99,235,.25);
  border-color: rgba(96,165,250,.45);
}
.metric-card { text-align: center; }
.metric-number {
  font-size: 2.4rem;
  font-weight: 700;
  color: #60a5fa;
  line-height: 1.1;
}
.metric-label { color: #94a3b8; margin-top: .35rem; }
.skill {
  display: inline-block;
  padding: .45rem .95rem;
  margin: .35rem;
  border-radius: 999px;
  background: linear-gradient(45deg, #2563eb, #7c3aed);
  font-size: .82rem;
  font-weight: 500;
  color: #fff;
}
.project-btn {
  display: inline-block;
  padding: .55rem 1rem;
  margin: .35rem .5rem 0 0;
  background: linear-gradient(45deg, #2563eb, #7c3aed);
  border-radius: 10px;
  text-decoration: none !important;
  color: #fff !important;
  font-size: .9rem;
  font-weight: 500;
}
.project-btn:hover { opacity: .92; }
.timeline-item h4 { margin: 0 0 .25rem; color: #f1f5f9; }
.timeline-item .meta { color: #64748b; font-size: .9rem; margin-bottom: .5rem; }
.timeline-item ul { margin: 0; padding-left: 1.1rem; color: #cbd5e1; }
.divider {
  border: none;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(148,163,184,.35), transparent);
  margin: 2rem 0;
}
[data-testid="stSidebar"] {
  background: rgba(15,23,42,.92);
  border-right: 1px solid rgba(255,255,255,.08);
}
[data-testid="stSidebar"] .stMarkdown { color: #e2e8f0; }
.contact-email {
  display: inline-block;
  margin-top: 1rem;
  padding: .65rem 1rem;
  border-radius: 12px;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.1);
  color: #93c5fd;
}
</style>
        """,
        unsafe_allow_html=True,
    )
def render_hero() -> None:
    src = profile_src()
    st.markdown(
        f"""
        <div class="hero" id="home">
          <img src="{src}" alt="Meet Sharma" class="profile-img">
          <div class="name">{PROFILE["name"]}</div>
          <p class="tagline">{PROFILE["tagline"]}</p>
          <p class="bio">{PROFILE["bio"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
def render_metrics() -> None:
    cols = st.columns(len(METRICS))
    for col, (value, label, icon) in zip(cols, METRICS):
        with col:
            st.markdown(
                f"""
                <div class="card metric-card">
                  <div class="metric-number">{value}</div>
                  <div class="metric-label">{icon} {label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
def render_skills() -> None:
    st.markdown('<p class="section-title" id="skills">Skills</p>', unsafe_allow_html=True)
    chips = "".join(f'<span class="skill">{s}</span>' for s in SKILLS)
    st.markdown(f'<div class="card">{chips}</div>', unsafe_allow_html=True)
def render_project_card(project: dict) -> str:
    links = ""
    if project.get("demo"):
        links += (
            f'<a href="{project["demo"]}" target="_blank" rel="noopener" '
            f'class="project-btn">🚀 Live Demo</a>'
        )
    if project.get("github"):
        links += (
            f'<a href="{project["github"]}" target="_blank" rel="noopener" '
            f'class="project-btn">📂 GitHub</a>'
        )
    return f"""
    <div class="card">
      <h3 style="margin-top:0;">{project["title"]}</h3>
      <p style="color:#cbd5e1;line-height:1.6;">{project["description"]}</p>
      <p><b>Tech:</b> {project["tech"]}</p>
      {links}
    </div>
    """
def render_projects() -> None:
    st.markdown('<p class="section-title" id="projects">Projects</p>', unsafe_allow_html=True)
    for i in range(0, len(PROJECTS), 2):
        row = PROJECTS[i : i + 2]
        cols = st.columns(len(row))
        for col, project in zip(cols, row):
            with col:
                st.markdown(render_project_card(project), unsafe_allow_html=True)
def render_about() -> None:
    st.markdown('<p class="section-title" id="about">About</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Education")
        for item in EDUCATION:
            st.markdown(
                f"""
                <div class="card timeline-item">
                  <h4>{item["degree"]}</h4>
                  <div class="meta">{item["school"]} · {item["period"]}</div>
                  <p style="margin:0;color:#cbd5e1;">{item["note"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
    with c2:
        st.markdown("#### Experience")
        for item in EXPERIENCE:
            bullets = "".join(f"<li>{p}</li>" for p in item["points"])
            st.markdown(
                f"""
                <div class="card timeline-item">
                  <h4>{item["role"]}</h4>
                  <div class="meta">{item["org"]} · {item["period"]}</div>
                  <ul>{bullets}</ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
def render_contact() -> None:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-title" id="contact">Connect</p>', unsafe_allow_html=True)
    cols = st.columns(len(LINKS))
    for col, (label, url) in zip(cols, LINKS):
        with col:
            st.link_button(label, url, use_container_width=True)
    st.markdown(
        f"""
        <p class="contact-email">
          📧 <a href="mailto:{PROFILE["email"]}" style="color:#93c5fd;text-decoration:none;">
          {PROFILE["email"]}</a>
          &nbsp;·&nbsp; {PROFILE["location"]}
        </p>
        """,
        unsafe_allow_html=True,
    )
    if not PROFILE_IMAGE.is_file():
        st.info(
            f"Add your photo as `{PROFILE_IMAGE.name}` in the app folder for a custom profile image."
        )
# ---------------- APP ---------------- #
st.set_page_config(
    page_title="Meet Sharma | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)
inject_css()
with st.sidebar:
    st.markdown("### 💻 Portfolio")
    st.caption("Navigate")
    for label, anchor in NAV:
        st.markdown(f"- [{label}](#{anchor})")
    st.divider()
    st.markdown("**Quick links**")
    for label, url in LINKS:
        st.link_button(label, url, use_container_width=True)
render_hero()
render_metrics()
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Overview</p>', unsafe_allow_html=True)
st.markdown(
    "I build **backend APIs**, **data tools**, and **interactive web apps** with Python and Java. "
    "Focused on clean code, real deployments, and measurable impact.",
)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
render_about()
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
render_skills()
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
render_projects()
render_contact()
