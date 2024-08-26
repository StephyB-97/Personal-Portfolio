#main
import streamlit as st
from navbar import show_navbar

main_background = """
<style>
 .stApp {
    background: linear-gradient(to bottom, #F8F4FF,#EFDECD);
 }
</style>
"""
show_navbar()
st.markdown(main_background, unsafe_allow_html=True)








