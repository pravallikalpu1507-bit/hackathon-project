import streamlit as st

st.title("My Hackathon Project")

st.write("My hackathon setup is working!")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Hello {name}!")