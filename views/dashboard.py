import streamlit as st
from resume_parser import extract_text_from_pdf
from scorer import calculate_match_score, find_missing_keywords

def show_dashboard():
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title("📄 AI Career Coach — Dashboard")
        st.caption(f"Logged in as {st.session_state.get('user_email', '')}")
    with col2:
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.session_state.page = "landing"
            st.rerun()

    tab1, tab2 = st.tabs(["🎯 Match Analysis", "✨ Resume Booster"])

    with tab1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        uploaded_resume = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])
        jd_text = st.text_area("Paste the Job Description here", height=200)

        if st.button("Check Match"):
            if uploaded_resume is not None and jd_text.strip() != "":
                resume_text = extract_text_from_pdf(uploaded_resume)
                score = calculate_match_score(resume_text, jd_text)
                missing_keywords = find_missing_keywords(resume_text, jd_text)

                st.session_state["resume_text"] = resume_text
                st.session_state["jd_text"] = jd_text
                st.session_state["missing_keywords"] = missing_keywords

                st.subheader(f"Match Score: {score}%")
                st.progress(int(score))

                st.subheader("Missing Keywords/Skills")
                if missing_keywords:
                    chips_html = "".join([f'<span class="keyword-chip">{kw}</span>' for kw in missing_keywords])
                    st.markdown(chips_html, unsafe_allow_html=True)
                else:
                    st.write("Great! No major keywords missing.")
            else:
                st.warning("Please upload a resume AND paste a job description first.")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        if "missing_keywords" not in st.session_state:
            st.warning("Run a match check in the first tab first.")
        else:
            st.write("Based on your match results, here's how to strengthen your resume:")
            st.info("🚧 AI rewrite suggestions plug in here (Round 2 feature).")
        st.markdown('</div>', unsafe_allow_html=True)