from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Apoorv Gupta"
PAGE_ICON = ":waving_black_flag:"
NAME = "Apoorv Gupta"
DESCRIPTION = """
Student | BTech. in Information Technology | Data Analyst
"""
EMAIL = "mailto:apoorvg26@gmail.com"
SOCIAL_MEDIA = { "":"",
    "LinkedIn": "https://www.linkedin.com/in/aapoorvv/",
    "   ":"",
    "GitHub": "https://github.com/aapoorvv",
    "     ":"",
    "E-mail": EMAIL,
    "":""
}
PROJECTS = {
    "◼︎ Sales Dashboard - Comparing sales across three stores": "https://link",
    "◼︎ Income and Expense Tracker - Web app with NoSQL database": "https:link",
    "◼︎ Desktop Application - Excel2CSV converter with user settings & menubar": "https://link",
    "◼︎ MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://link",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- INFO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.link_button("View Resume", "http://tiny.cc/apoorv-resume",  help=None, type="primary", disabled=False, use_container_width=False)
    # st.write(":e-mail:", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(7)
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[<b>{platform}]({link}</b>)",unsafe_allow_html=True)


# # --- EXPERIENCE & QUALIFICATIONS ---
# st.write('\n')
# st.subheader("Experience & Qulifications")
# st.write(
#     """
# - ✔️ 7 Years expereince extracting actionable insights from data
# - ✔️ Strong hands on experience and knowledge in Python and Excel
# - ✔️ Good understanding of statistical principles and their respective applications
# - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
# """
# )


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")

# st.write(
#     """
# - 👩‍💻 Programming: Python (Scikit-learn, Pandas etc.), SQL, Java
# - 📊 Data Visulization: Tableau, PowerBi, MS Excel
# - 📚 Courses: DBMS, Big Data, OOPS etc.
# - 🗄️ Databases: MySQL
# - 📒 Non Technical: Financial Analysis
# """
# )

st.write(
    """
- ◼︎ Programming: Python (Scikit-learn, Pandas etc.), SQL, Java
- ◼︎ Data Visulization: Tableau, PowerBi, MS Excel
- ◼︎ Courses: DBMS, Big Data, OOPS etc.
- ◼︎ Databases: MySQL
- ◼︎ Non Technical: Financial Analysis
"""
)
# # --- WORK HISTORY ---
# st.write('\n')
# st.subheader("Work History")
# st.write("---")

# # --- JOB 1
# st.write("🚧", "**Senior Data Analyst | Ross Industries**")
# st.write("02/2020 - Present")
# st.write(
#     """
# - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
# - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
# - ► Redesigned data model through iterations that improved predictions by 12%
# """
# )

# # --- JOB 2
# st.write('\n')
# st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
# st.write("01/2018 - 02/2022")
# st.write(
#     """
# - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
# - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
# - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
# """
# )

# # --- JOB 3
# st.write('\n')
# st.write("🚧", "**Data Analyst | Chegg**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"- [<c>{project}]({link}</c>)",unsafe_allow_html=True)
st.write("\n")

# ---- CONTACT ----
with st.container():
    st.subheader("Get In Touch With Me!")
    st.write("---")

    # Documention: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/apoorvg26@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()