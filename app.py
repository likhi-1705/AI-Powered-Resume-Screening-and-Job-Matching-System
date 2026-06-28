import streamlit as st
from skills import SKILLS
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills


def extract_text_from_pdf(uploaded_file):

    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


def calculate_similarity(resume, job_description):

    documents = [resume, job_description]

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(matrix[0:1], matrix[1:2])

    return similarity[0][0] * 100


st.title("AI-Powered Resume Screening & Job Matching System")

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description Here",
    height=250
)

resume_text = ""

if uploaded_resume is not None:
    resume_text = extract_text_from_pdf(uploaded_resume)

if st.button("Analyze"):

    if uploaded_resume is None:
        st.error("Please upload a resume PDF.")
    elif job_description.strip() == "":
        st.error("Please enter a job description.")
    else:

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)

        matched_skills = list(set(resume_skills) & set(jd_skills))
        missing_skills = list(set(jd_skills) - set(resume_skills))

        if len(jd_skills) > 0:
            skill_match = (len(matched_skills) / len(jd_skills)) * 100
        else:
            skill_match = 0

        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        final_score = (
            0.7 * similarity_score +
            0.3 * skill_match
        )

        st.subheader("Skills Found in Resume")
        st.write(resume_skills)

        st.subheader("Skills Required in Job Description")
        st.write(jd_skills)

        st.subheader("Matched Skills")
        st.write(matched_skills)

        st.subheader("Missing Skills")
        st.write(missing_skills)

        st.subheader("Skill Match Percentage")
        st.write(f"{skill_match:.2f}%")

        st.subheader("Resume-JD Similarity Score")
        st.write(f"{similarity_score:.2f}%")

        st.subheader("Final Match Score")
        st.write(f"{final_score:.2f}/100")

        if final_score >= 80:
            st.success("Excellent Match ✅")
        elif final_score >= 60:
            st.info("Good Match 👍")
        else:
            st.warning("Needs Improvement ⚠️")
