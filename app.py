import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="AI Career Navigator",
    page_icon="🚀",
    layout="wide"
)

# ==================================================
# CAREER DESCRIPTIONS
# ==================================================

career_descriptions = {

    "Data Scientist":
    "Analyzes large datasets and builds predictive models.",

    "AI Engineer":
    "Develops AI-powered applications and intelligent systems.",

    "Machine Learning Engineer":
    "Builds, trains and deploys machine learning models.",

    "Cloud Engineer":
    "Designs and manages cloud infrastructure and services.",

    "DevOps Engineer":
    "Automates software deployment and system operations.",

    "Backend Developer":
    "Develops APIs, databases and server-side applications.",

    "Frontend Developer":
    "Builds attractive and responsive user interfaces.",

    "Full Stack Developer":
    "Works on both frontend and backend technologies.",

    "Data Analyst":
    "Converts raw data into actionable business insights.",

    "Cyber Security Analyst":
    "Protects networks and systems from cyber threats."
}

# ==================================================
# HEADER
# ==================================================

st.title("🚀 AI Career Navigator")

st.markdown("""
### AI-Powered Career Recommendation System

This project recommends careers based on user skills using:

✅ TF-IDF Vectorization  
✅ Cosine Similarity  
✅ Machine Learning Concepts  
✅ Streamlit Dashboard  
✅ Skill Gap Analysis  
""")

st.markdown("---")

# ==================================================
# LOAD DATA
# ==================================================

jobs = pd.read_csv("jobs.csv")

# ==================================================
# USER INPUT
# ==================================================

skills = st.text_input(
    "Enter Your Skills",
    placeholder="Example: Python SQL Machine Learning"
)

# ==================================================
# BUTTON
# ==================================================

if st.button("🔍 Recommend Career"):

    if skills.strip() == "":
        st.warning("Please enter some skills.")
        st.stop()

    # =============================================
    # TF-IDF RECOMMENDATION ENGINE
    # =============================================

    corpus = jobs["Skills"].tolist()

    corpus.append(skills)

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(corpus)

    similarity_scores = cosine_similarity(
        tfidf_matrix[-1],
        tfidf_matrix[:-1]
    )

    scores = similarity_scores.flatten()

    jobs["Score"] = scores

    jobs = jobs.sort_values(
        by="Score",
        ascending=False
    )

    top3 = jobs.head(3)

    # =============================================
    # TOP MATCHES
    # =============================================

    st.subheader("🏆 Top Career Matches")

    for _, row in top3.iterrows():

        percentage = round(
            row["Score"] * 100,
            2
        )

        st.write(
            f"### ✅ {row['Role']} — {percentage}% Match"
        )

        st.progress(
            min(int(percentage), 100)
        )

        if row["Role"] in career_descriptions:

            st.caption(
                career_descriptions[row["Role"]]
            )

    # =============================================
    # CHART
    # =============================================

    st.subheader("📊 Career Match Visualization")

    chart_data = top3.copy()

    chart_data["Score"] = (
        chart_data["Score"] * 100
    )

    fig = px.bar(
        chart_data,
        x="Role",
        y="Score",
        color="Role",
        text="Score",
        title="Career Match Percentage"
    )

    st.plotly_chart(fig)

    # =============================================
    # SKILL GAP ANALYSIS
    # =============================================

    best_job = jobs.iloc[0]

    required_skills = best_job["Skills"].split()

    user_skill_list = skills.split()

    missing_skills = []

    for skill in required_skills:

        if skill not in user_skill_list:

            missing_skills.append(skill)

    st.subheader("📚 Skills To Learn")

    if len(missing_skills) == 0:

        st.success(
            "Excellent! You already possess all required skills."
        )

    else:

        for skill in missing_skills:

            st.write(
                f"🔹 {skill}"
            )

    # =============================================
    # LEARNING ROADMAP
    # =============================================

    st.subheader("🛣 Learning Roadmap")

    roadmap = []

    for skill in missing_skills:

        roadmap.append(
            f"Learn {skill}"
        )

    roadmap.extend([
        "Build 3 Projects",
        "Create a Portfolio",
        "Practice Interview Questions",
        "Apply for Internships"
    ])

    for i, step in enumerate(
        roadmap,
        start=1
    ):

        st.write(
            f"{i}. {step}"
        )

    # =============================================
    # BEST MATCH
    # =============================================

    st.success(
        f"🎯 Best Career Match: {best_job['Role']}"
    )

    st.balloons()

# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.markdown(
    "Developed by **Cheran Rajamanikam** | DecodeLabs Internship Project"
)