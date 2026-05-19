import streamlit as st
import PyPDF2
from textblob import TextBlob
import random
import pandas as pd
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Recruitment & Interview Platform",
    page_icon="🚀",
    layout="wide",
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>
/* Remove White Top Space */
.block-container {
    padding-top: 1rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    max-width: 100% !important;
}

/* Full Width Layout */
.main .block-container {
    max-width: 100%;
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* Remove Streamlit Header Space */
header {
    visibility: hidden;
}


/* Main Background */
.stApp {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 54px;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    font-size: 20px;
    color: #f8fafc;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: #1e293b;
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 25px;
    border: 1px solid #38bdf8;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #020617;
}

/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(to right, #06b6d4, #2563eb);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
}

/* Download Buttons */
.stDownloadButton>button {
    background: linear-gradient(to right, #7c3aed, #2563eb);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 20px;
    font-size: 15px;
    font-weight: bold;
    margin-bottom: 10px;
}

/* Input Labels */
label, .stMarkdown, .stText {
    color: white !important;
    font-weight: 500;
}

/* Text Areas */
textarea {
    background-color: #f8fafc !important;
    color: black !important;
    border-radius: 10px !important;
}

/* Headers */
h1, h2, h3, h4 {
    color: #38bdf8 !important;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background: #1e293b;
    border: 1px solid #38bdf8;
    padding: 18px;
    border-radius: 15px;
    color: white;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    background-color: white;
}

/* File uploader text */
[data-testid="stFileUploader"] {
    color: white !important;
}

/* Success Message */
.stSuccess {
    background-color: #065f46 !important;
    color: white !important;
}

/* Warning Message */
.stWarning {
    background-color: #92400e !important;
    color: white !important;
}

/* Error Message */
.stError {
    background-color: #991b1b !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">AI Recruitment & Interview Platform</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">AI-Powered Resume Screening, Hiring Analytics & Mock Interview System</div>',
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📂 Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "🏠 Home",
        "👨‍💼 Candidate Portal",
        "📊 Recruiter Dashboard",
        "ℹ About Project"
    ]
)

# =========================================================
# HOME PAGE
# =========================================================

if page == "🏠 Home":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📄 Resume Templates", "5+")

    with col2:
        st.metric("🤖 AI Features", "10+")

    with col3:
        st.metric("📊 Analytics Modules", "6+")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("🚀 Platform Features")

    st.write("""
    ✔ ATS Resume Score Prediction  
    ✔ Resume Skill Extraction  
    ✔ AI Mock Interview Questions  
    ✔ Emotion & Sentiment Analysis  
    ✔ Confidence Score Prediction  
    ✔ Multiple Resume Screening  
    ✔ Candidate Ranking System  
    ✔ Hiring Analytics Dashboard  
    ✔ Downloadable Resume Templates  
    ✔ Recruiter Insights & Analytics  
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# CANDIDATE PORTAL
# =========================================================

elif page == "👨‍💼 Candidate Portal":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("📄 Resume Templates")

    resume_files = {
        "Data Scientist Resume": "Sample_Resume/data_scientist_sample.pdf",
        "Data Analyst Resume": "Sample_Resume/data_analyst_sample.pdf",
        "HR Resume": "Sample_Resume/HR_resume_sample.pdf",
        "ML Engineer Resume": "Sample_Resume/machine_learning_sample.pdf",
        "Web Developer Resume": "Sample_Resume/web_developer_sample.pdf"
    }

    for resume_name, file_path in resume_files.items():

        st.subheader(resume_name)

        try:
            with open(file_path, "rb") as pdf_file:

                st.download_button(
                    label=f"⬇ Download {resume_name}",
                    data=pdf_file,
                    file_name=file_path.split("/")[-1],
                    mime="application/pdf"
                )

        except:
            st.warning(f"{resume_name} file not found.")

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # UPLOAD RESUME
    # =====================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "📤 Upload Your Resume PDF",
        type=["pdf"]
    )

    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file is not None:

        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        resume_text = ""

        for page in pdf_reader.pages:
            resume_text += page.extract_text()

        resume_lower = resume_text.lower()

        skills_db = [
            "python",
            "machine learning",
            "deep learning",
            "data analysis",
            "sql",
            "java",
            "c++",
            "streamlit",
            "tensorflow",
            "pandas",
            "numpy",
            "web development",
            "html",
            "css",
            "javascript",
            "power bi",
            "communication",
            "leadership"
        ]

        detected_skills = []

        for skill in skills_db:

            if skill in resume_lower:
                detected_skills.append(skill)

        # =================================================
        # ATS SCORE
        # =================================================

        resume_score = len(detected_skills) * 10

        if resume_score > 100:
            resume_score = 100

        # =================================================
        # ROLE PREDICTION
        # =================================================

        data_analyst_score = 0
        ml_engineer_score = 0
        web_dev_score = 0
        hr_score = 0

        data_analyst_keywords = [
            "power bi",
            "excel",
            "sql",
            "tableau",
            "data analysis",
            "analytics",
            "dashboard"
        ]

        ml_keywords = [
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch",
            "neural network",
            "ai"
        ]

        web_keywords = [
            "html",
            "css",
            "javascript",
            "react",
            "node",
            "web development"
        ]

        hr_keywords = [
            "recruitment",
            "employee engagement",
            "talent acquisition",
            "hr",
            "payroll"
        ]

        for word in data_analyst_keywords:
            if word in resume_lower:
                data_analyst_score += 1

        for word in ml_keywords:
            if word in resume_lower:
                ml_engineer_score += 1

        for word in web_keywords:
            if word in resume_lower:
                web_dev_score += 1

        for word in hr_keywords:
            if word in resume_lower:
                hr_score += 1

        role_scores = {
            "Data Analyst": data_analyst_score,
            "ML Engineer": ml_engineer_score,
            "Web Developer": web_dev_score,
            "HR": hr_score
        }

        predicted_role = max(role_scores, key=role_scores.get)

        # =================================================
        # METRICS
        # =================================================

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("⭐ ATS Score", f"{resume_score}%")

        with col2:
            st.metric("🧠 Skills Detected", len(detected_skills))

        with col3:
            st.metric("🎯 Predicted Role", predicted_role)

        # =================================================
        # DETECTED SKILLS
        # =================================================

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.header("✅ Detected Skills")

        for skill in detected_skills:
            st.success(skill)

        st.markdown('</div>', unsafe_allow_html=True)

        # =================================================
        # MISSING SKILLS
        # =================================================

        important_skills = [
            "python",
            "sql",
            "communication",
            "machine learning",
            "data analysis"
        ]

        missing_skills = []

        for skill in important_skills:
            if skill not in detected_skills:
                missing_skills.append(skill)

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.header("📌 Recommended Skills")

        for skill in missing_skills:
            st.warning(skill)

        st.markdown('</div>', unsafe_allow_html=True)

        # =================================================
        # QUESTION GENERATION
        # =================================================

        questions = []

        if "python" in detected_skills:
            questions.extend([
                "Explain the advantages of Python.",
                "What are Python lists and tuples?",
                "Explain object-oriented programming in Python."
            ])

        if "machine learning" in detected_skills:
            questions.extend([
                "What is Machine Learning?",
                "Explain supervised and unsupervised learning.",
                "What is Random Forest Algorithm?",
                "Explain the train-test split concept."
            ])

        if "web development" in detected_skills:
            questions.extend([
                "Explain frontend and backend development.",
                "What is responsive web design?"
            ])

        if "data analysis" in detected_skills:
            questions.extend([
                "What is data analysis?",
                "Explain data preprocessing."
            ])

        if "power bi" in detected_skills:
            questions.extend([
                "What is Power BI?",
                "Explain DAX functions."
            ])

        selected_questions = random.sample(
            questions,
            min(5, len(questions))
        )

        # =================================================
        # MOCK INTERVIEW
        # =================================================

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.header("🎤 AI Mock Interview")

        answers = []

        for i, question in enumerate(selected_questions, 1):

            st.subheader(f"Question {i}")

            st.write(question)

            ans = st.text_area(
                f"Your Answer {i}",
                key=i
            )

            answers.append(ans)

        st.markdown('</div>', unsafe_allow_html=True)

        # =================================================
        # ANALYSIS
        # =================================================

        if st.button("Analyze Interview"):

            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.header("🧠 Emotion Analysis & AI Feedback")

            total_polarity = 0

            for i, ans in enumerate(answers, 1):

                analysis = TextBlob(ans)

                polarity = analysis.sentiment.polarity

                total_polarity += polarity

                st.subheader(f"Answer {i}")

                st.write(f"Sentiment Score: {polarity}")

                if polarity > 0:
                    st.success("Confident / Positive")

                elif polarity < 0:
                    st.error("Nervous / Negative")

                else:
                    st.warning("Neutral")

            average_polarity = total_polarity / len(answers)

            confidence_score = max(
                0,
                min(100, (average_polarity + 1) * 50)
            )

            st.subheader(
                f"⭐ Overall Confidence Score: {confidence_score:.2f}%"
            )

            st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# RECRUITER DASHBOARD
# =========================================================

elif page == "📊 Recruiter Dashboard":

    st.header("📊 Hiring Analytics Dashboard")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    uploaded_resumes = st.file_uploader(
        "📤 Upload Multiple Resumes",
        type=["pdf"],
        accept_multiple_files=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_resumes:

        candidate_names = []
        ats_scores = []
        predicted_roles = []

        for resume in uploaded_resumes:

            pdf_reader = PyPDF2.PdfReader(resume)

            text = ""

            for page in pdf_reader.pages:
                text += page.extract_text()

            text = text.lower()
            # =================================================
            # ADVANCED ATS SCORING
            # =================================================

            score = 0

            all_skills = [

                # Data Analyst
                "sql",
                "power bi",
                "excel",
                "tableau",
                "analytics",

                # ML Engineer
                "python",
                "machine learning",
                "deep learning",
                "tensorflow",
                "ai",

                # Web Developer
                "html",
                "css",
                "javascript",
                "react",
                "node",

                # HR
                "recruitment",
                "payroll",
                "employee engagement",
                "talent acquisition",

                # Common
                "communication",
                "leadership"
            ]

            for skill in all_skills:

                if skill in text:
                    score += 10

            if score > 100:
                score = 100

                        

            # =================================================
            # ADVANCED ROLE PREDICTION
            # =================================================

            data_analyst_score = 0
            ml_engineer_score = 0
            web_dev_score = 0
            hr_score = 0

            data_analyst_keywords = [
                "power bi",
                "excel",
                "sql",
                "tableau",
                "data analysis",
                "analytics",
                "dashboard"
            ]

            ml_keywords = [
                "machine learning",
                "deep learning",
                "tensorflow",
                "pytorch",
                "neural network",
                "ai"
            ]

            web_keywords = [
                "html",
                "css",
                "javascript",
                "react",
                "node",
                "web development"
            ]

            hr_keywords = [
                "recruitment",
                "employee engagement",
                "talent acquisition",
                "hr",
                "payroll"
            ]

            for word in data_analyst_keywords:
                if word in text:
                    data_analyst_score += 1

            for word in ml_keywords:
                if word in text:
                    ml_engineer_score += 1

            for word in web_keywords:
                if word in text:
                    web_dev_score += 1

            for word in hr_keywords:
                if word in text:
                    hr_score += 1

            role_scores = {
                "Data Analyst": data_analyst_score,
                "ML Engineer": ml_engineer_score,
                "Web Developer": web_dev_score,
                "HR": hr_score
            }

            role = max(role_scores, key=role_scores.get)

            candidate_names.append(resume.name)
            ats_scores.append(score)
            predicted_roles.append(role)

        # =================================================
        # DATAFRAME
        # =================================================

        df = pd.DataFrame({
            "Candidate": candidate_names,
            "ATS Score": ats_scores,
            "Predicted Role": predicted_roles
        })

        df = df.sort_values(
            by="ATS Score",
            ascending=False
        )

        # =================================================
        # METRICS
        # =================================================

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("👨‍💼 Total Applicants", len(df))

        with col2:
            st.metric(
                "🏆 Highest ATS Score",
                f"{df['ATS Score'].max()}%"
            )

        with col3:
            st.metric(
                "📈 Average ATS Score",
                f"{df['ATS Score'].mean():.1f}%"
            )

        # =================================================
        # TABLE
        # =================================================

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("🏆 Candidate Ranking")

        st.dataframe(df)

        st.markdown('</div>', unsafe_allow_html=True)

        # =================================================
        # BAR CHART
        # =================================================

        st.markdown('<div class="card">', unsafe_allow_html=True)

        fig = px.bar(
            df,
            x="Candidate",
            y="ATS Score",
            color="Predicted Role",
            title="Candidate ATS Score Comparison",
            text="ATS Score"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # =================================================
        # PIE CHART
        # =================================================

        st.markdown('<div class="card">', unsafe_allow_html=True)

        role_count = df["Predicted Role"].value_counts()

        pie_fig = px.pie(
            values=role_count.values,
            names=role_count.index,
            title="Applicant Role Distribution"
        )

        st.plotly_chart(pie_fig, use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# ABOUT PROJECT
# =========================================================

elif page == "ℹ About Project":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.title("ℹ About Project")

    st.write("""
    The AI Recruitment & Interview Platform is an AI-powered
    career and hiring assistance system designed for both
    candidates and recruiters.

    Features:
    
    ✔ ATS Resume Score Prediction  
    ✔ Resume Skill Extraction  
    ✔ AI Mock Interview Questions  
    ✔ Emotion & Sentiment Analysis  
    ✔ Confidence Score Prediction  
    ✔ Multiple Resume Screening  
    ✔ Candidate Ranking System  
    ✔ Hiring Analytics Dashboard  
    ✔ Recruiter Insights & Analytics  

    Technologies Used:
    - Python
    - Streamlit
    - NLP
    - TextBlob
    - PyPDF2
    - Plotly
    - Pandas
    """)

    st.markdown('</div>', unsafe_allow_html=True)