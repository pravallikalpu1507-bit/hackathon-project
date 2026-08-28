import streamlit as st
import re

def is_valid_email(email):
    return re.match(r"^[\w\.-]+@gmail\.com$", email) is not None

def show_login():
    st.markdown('<div class="auth-wrapper"><div class="glass-card auth-card">', unsafe_allow_html=True)
    st.markdown('<p class="auth-icon">🔐</p>', unsafe_allow_html=True)
    st.subheader("Welcome back")
    st.caption("Log in to continue to your dashboard")

    email = st.text_input("Gmail Address", placeholder="yourname@gmail.com")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    if st.button("Log In", use_container_width=True):
        if not is_valid_email(email):
            st.error("Please enter a valid Gmail address (e.g. name@gmail.com).")
        elif len(password) < 6:
            st.error("Password must be at least 6 characters.")
        else:
            users = st.session_state.get("users", {})
            if email in users and users[email] == password:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.session_state.page = "dashboard"
                st.rerun()
            else:
                st.error("Incorrect email or password. Don't have an account? Sign up below.")

    st.markdown('<p class="auth-divider">or</p>', unsafe_allow_html=True)

    if st.button("Continue with Google", use_container_width=True):
        st.session_state.logged_in = True
        st.session_state.user_email = "demo.user@gmail.com"
        st.session_state.page = "dashboard"
        st.rerun()

    if st.button("← Back", use_container_width=True):
        st.session_state.page = "landing"
        st.rerun()

    st.markdown('</div></div>', unsafe_allow_html=True)