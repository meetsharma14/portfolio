import streamlit as st
import base64

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Meet Sharma Portfolio",
    page_icon="💻",
    layout="wide"
)

# ---------------- IMAGE FUNCTION ---------------- #

def get_base64(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_base64("profile.png")

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
font-family:'Poppins',sans-serif;
}

.stApp{
background:
radial-gradient(circle at top left,#2563eb22,transparent 30%),
radial-gradient(circle at bottom right,#7c3aed22,transparent 30%),
linear-gradient(
135deg,
#020617,
#0f172a,
#1e293b
);

color:white;
}

.block-container{
max-width:1200px;
padding-top:2rem;
}

.hero{
padding:70px;
border-radius:30px;

background:rgba(255,255,255,.05);

backdrop-filter:blur(20px);

border:1px solid rgba(255,255,255,.08);

text-align:center;

margin-bottom:35px;

box-shadow:0 0 40px rgba(37,99,235,.2);
}

.profile-img{

width:180px;
height:180px;

border-radius:50%;

object-fit:cover;

border:4px solid #60a5fa;

margin-bottom:25px;

box-shadow:
0 0 40px rgba(96,165,250,.6);

transition:0.4s;
}

.profile-img:hover{

transform:scale(1.05);

box-shadow:
0 0 60px rgba(124,58,237,.9);
}

.name{
font-size:55px;
font-weight:700;

background:linear-gradient(
90deg,
#60a5fa,
#818cf8,
#c084fc
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.card{

background:rgba(255,255,255,.05);

padding:25px;

border-radius:20px;

backdrop-filter:blur(20px);

border:1px solid rgba(255,255,255,.08);

transition:.4s;

margin-bottom:20px;
}

.card:hover{

transform:translateY(-10px);

box-shadow:
0 0 30px rgba(96,165,250,.5);

border-color:#60a5fa;
}

.skill{

display:inline-block;

padding:10px 16px;

margin:6px;

border-radius:30px;

background:linear-gradient(
45deg,
#2563eb,
#7c3aed
);

font-size:13px;
font-weight:500;
}

.metric-card{
text-align:center;
}

.metric-number{
font-size:42px;
font-weight:bold;
color:#60a5fa;
}

.project-btn{

display:inline-block;

padding:10px 18px;

margin-top:15px;

background:linear-gradient(
45deg,
#2563eb,
#7c3aed
);

border-radius:12px;

text-decoration:none;

color:white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ---------------- #

st.markdown(f"""

<div class='hero'>

<img src="data:image/png;base64,{img}"
class='profile-img'>

<div class='name'>
Meet Sharma
</div>

<br>

<h3>
B.Tech CSE Student |
Python Intern |
Java Developer |
Python Developer |
FastAPI Developer
</h3>

<p>

Computer Science undergraduate passionate about
building scalable applications, backend systems,
real-world projects and data-driven solutions.

</p>

</div>

""", unsafe_allow_html=True)

# ---------------- OVERVIEW ---------------- #

st.markdown("## Overview")

m1,m2,m3=st.columns(3)

with m1:
    st.markdown("""
    <div class='card metric-card'>
    <div class='metric-number'>4+</div>
    🚀 Projects
    </div>
    """,unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class='card metric-card'>
    <div class='metric-number'>13+</div>
    💻 Skills
    </div>
    """,unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class='card metric-card'>
    <div class='metric-number'>3</div>
    🏢 Internships
    </div>
    """,unsafe_allow_html=True)

st.write("---")

# ---------------- SKILLS ---------------- #

st.markdown("## Skills")

skills=[

"Java",
"Python",
"FastAPI",
"MySQL",
"Power BI",
"Pandas",
"NumPy",
"Git",
"Matplotlib",
"VS Code",
"Jupyter Notebook",
"OOP",
"Data Structures"

]

skill_html=""

for skill in skills:

    skill_html += f"""
    <span class='skill'>
    {skill}
    </span>
    """

st.markdown(skill_html,unsafe_allow_html=True)

st.write("---")

# ---------------- PROJECTS ---------------- #

st.header("Projects")

p1,p2=st.columns(2)

with p1:

    st.markdown("""

    <div class='card'>

    <h3>✅ Todo List Application</h3>

    <br>

    Developed a live task management application that
    allows users to add, update, delete and organize
    tasks efficiently. Implemented task status tracking
    with completed and pending task summaries.

    <br><br>

    <b>Tech:</b>

    Python | Streamlit | Session State

    <br><br>

    <a href="https://aegqkbatupkj8gec5yurqn.streamlit.app/"
    target="_blank"
    class="project-btn">

    🚀 Live Demo

    </a>

    </div>

    """, unsafe_allow_html=True)

with p2:

    st.markdown("""

    <div class='card'>

    <h3>📄 ATS Resume Checker</h3>

    <br>

    Built an ATS-based resume analyzer that compares
    resumes against job descriptions using keyword
    extraction and cosine similarity scoring.
    Supports PDF and DOCX files with resume ranking
    and missing keyword suggestions.

    <br><br>

    <b>Tech:</b>

    Python | Streamlit | Scikit-learn |
    NLP | pdfplumber | python-docx

    </div>

    """, unsafe_allow_html=True)

p3,p4=st.columns(2)

with p3:

    st.markdown("""

    <div class='card'>

    <h3>💰 EMI Calculator</h3>

    <br>

    Developed a Python-based application to calculate
    loan EMI using financial formulas and user inputs.

    <br><br>

    <b>Tech:</b> Python | Tkinter | ttk | OpenPyXL | PIL (Pillow) | File Handling | Excel | Web Browser API

    </div>

    """, unsafe_allow_html=True)

with p4:

    st.markdown("""

    <div class='card'>

    <h3>✈ Travel Booking System</h3>

    <br>

    Developed a console-based travel booking system
    demonstrating structured programming logic,
    booking workflows and user interaction.

    <br><br>

    <b>Tech:</b> Java | Java HttpClient API | REST API | JSON | org.json | IPInfo API

    </div>

    """, unsafe_allow_html=True)

# ---------------- CONTACT ---------------- #

st.write("---")
st.markdown("## Connect")

c1,c2,c3=st.columns(3)

with c1:
    st.link_button(
        "GitHub",
        "https://github.com/meetsharma14"
    )

with c2:
    st.link_button(
        "LinkedIn",
        "https://linkedin.com/in/meet-sharma-304956274"
    )

with c3:
    st.link_button(
        "LeetCode",
        "https://leetcode.com/u/SqVzfRkZOb/"
    )

st.write("📧 Email: meetsharma1569@gmail.com")