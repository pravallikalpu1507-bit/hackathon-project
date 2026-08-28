import streamlit as st
from resume_parser import extract_text_from_pdf
from scorer import calculate_match_score, find_missing_keywords

st.set_page_config(page_title="Resume Match Scorer", page_icon="📄")

st.title("📄 Resume-to-Job Match Scorer")
st.write("Upload your resume and paste a job description to see how well they match.")

uploaded_resume = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])
jd_text = st.text_area("Paste the Job Description here", height=200)

if st.button("Check Match"):
    if uploaded_resume is not None and jd_text.strip() != "":
        resume_text = extract_text_from_pdf(uploaded_resume)

        score = calculate_match_score(resume_text, jd_text)
        missing_keywords = find_missing_keywords(resume_text, jd_text)

        st.subheader(f"Match Score: {score}%")
        st.progress(int(score))

        st.subheader("Missing Keywords/Skills")
        if missing_keywords:
            st.write(", ".join(missing_keywords))
        else:
            st.write("Great! No major keywords missing.")
    else:
        st.warning("Please upload a resume AND paste a job description first.")