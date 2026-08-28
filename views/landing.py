import streamlit as st
import streamlit.components.v1 as components


def show_landing():

    # =========================================
    # SPLINE 3D BACKGROUND
    # =========================================

    components.html(
        """
        <script type="module"
        src="https://cdn.spline.design/@splinetool/viewer@2.0.13/build/spline-viewer.js">
        </script>

        <spline-viewer
            url="https://prod.spline.design/a1TLXo7jvdcLeyGg/scene.splinecode"
            style="width: 100%; height: 900px;">
        </spline-viewer>
        """,
        height=900
    )


    # =========================================
    # LANDING PAGE TEXT
    # =========================================

    st.markdown(
        '<div class="landing-overlay">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<h1 class="landing-title">AI Career Coach</h1>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="landing-sub">Know exactly how well you match — before you apply.</p>',
        unsafe_allow_html=True
    )


    # =========================================
    # LOGIN + SIGN UP BUTTONS
    # =========================================

    col1, col2, col3, col4 = st.columns([2, 1, 1, 2])

    with col2:

        if st.button(
            "Log In",
            use_container_width=True
        ):
            st.session_state.page = "login"
            st.rerun()


    with col3:

        if st.button(
            "Sign Up",
            use_container_width=True
        ):
            st.session_state.page = "signup"
            st.rerun()


    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )