import streamlit as st
from streamlit_navigation_bar import st_navbar
from Home import show_home
from About import show_about
from Projects import show_projects
from contact import contact_form


def show_navbar():
    pages = ["Home", "About", "Projects", "Contact"]
    styles = {
        "nav": {
            "background-color": "#eeddf3",
            "width": "100%",
            "margin": "0",
            "padding": "0"
        },
        "div": {
            "max-width": "32rem",
        },
        "span": {
            "border-radius": "0.5rem",
            "color": "#31333F",
            "margin": "0 0.125rem",
            "padding": "0.4375rem 0.625rem",
        },
        "active": {
            "background-color": "rgba(255, 255, 255, 0.25)",
        },
        "hover": {
            "background-color": "rgba(255, 255, 255, 0.35)",
        },
    }

    if 'page' not in st.session_state:
        st.session_state.page = "Home"

    page = st_navbar(pages, styles=styles)
    st.session_state.page = page

    if page == "Home":
        show_home()
    elif page == "About":
        show_about()
    elif page == "Projects":
        show_projects()
    elif page == "Contact":
        contact_form()

