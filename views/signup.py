import streamlit as st
import re

def is_valid_email(email):
    return re.match(r"^[\w\.-]+@gmail\.com$", email) is not None

def show_signup():
    st.markdown('<div class="auth-wrapper"><div class="glass-card auth-card">', unsafe_allow_html=True)
    st.markdown('<p class="auth-icon">✨</p>', unsafe_allow_html=True)
    st.subheader("Create your account")
    st.caption("Start matching your resume in seconds")

    name = st.text_input("Full Name", placeholder="Your name")
    email = st.text_input("Gmail Address", placeholder="yourname@gmail.com")
    password = st.text_input("Password", type="password", placeholder="At least 6 characters")

    if st.button("Sign Up", use_container_width=True):
        if not name.strip():
            st.error("Please enter your name.")
        elif not is_valid_email(email):
            st.error("Please enter a valid Gmail address (e.g. name@gmail.com).")
        elif len(password) < 6:
            st.error("Password must be at least 6 characters.")
        else:
            if "users" not in st.session_state:
                st.session_state.users = {}
            st.session_state.users[email] = password
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.session_state.page = "dashboard"
            st.success("Account created!")
            st.rerun()

    if st.button("← Back", use_container_width=True):
        st.session_state.page = "landing"
        st.rerun()

    st.markdown('</div></div>', unsafe_allow_html=True)