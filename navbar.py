import streamlit as st
from streamlit_navigation_bar import st_navbar
from Home import show_home

def show_navbar():
    pages = ["Home", "About", "Projects", "Contact"]
    styles = {
        "nav": {
            "background-color": "#FFFFFF",
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

    page = st_navbar(pages, styles=styles)


    if page == "Home":
        show_home()

