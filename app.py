import streamlit as st
from views.landing import show_landing
from views.login import show_login
from views.signup import show_signup
from views.dashboard import show_dashboard

st.set_page_config(page_title="AI Career Coach", page_icon="📄", layout="wide")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "landing"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Route to the correct page
if st.session_state.page == "landing":
    show_landing()
elif st.session_state.page == "login":
    show_login()
elif st.session_state.page == "signup":
    show_signup()
elif st.session_state.page == "dashboard":
    if st.session_state.logged_in:
        show_dashboard()
    else:
        st.session_state.page = "landing"
        st.rerun()