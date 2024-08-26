import streamlit as st

def show_home():
    # Centered title, subheader, and Streamlit button using HTML and CSS
    st.markdown("""
    <style>
    .centered-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 60vh; /* Adjust this value based on your layout needs */
        text-align: center;
    }
    </style>
    <div class="centered-container">
        <h1>I'M STEPHANIE BERNADES</h1>
        <h2>An ambitious Computer Science student focused on mastering backend development, committed to building secure and efficient systems that drive success</h2>
    </div>
    """, unsafe_allow_html=True)

