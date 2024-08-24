import streamlit as st

def show_about():

    col1, col2 =st.columns([2,1])
    with col1:
        st.header("Get to Know me!")
        st.text("I'm a Computer Science student at Hunter \nCollege, passionate about backend \ndevelopment and creating tools that make \neveryday tasks easier.")
        st.text("My programming journey began in high \nschool with Python, and since then, I've \nbeen dedicated to "
                "expanding my skills and \ntackling more complex challenges. \nAt college, I've focused on building \n"
                "practical solutions and diving deep into \nthe theories that drive technology.")
        st.text("I enjoy working on projects that \nchallenge me to learn new things and stay \nupdated with the latest developments in \nthe field")
        st.text("I’m looking forward to putting my skills \ninto practice on a larger scale. \nIf you have an opportunity that matches \nmy skills and interests, I’d be happy \nto connect!")
    with col2:
        st.header("My Skills ")
        st.subheader("Programming Languages")
        a1, a2 = st.columns(2)
        with a1:
            st.button("Python", type="primary")
            st.button("Java", type="primary")
            st.button("R", type="primary")
        with a2:
            st.button("C++", type="primary")
            st.button("HTML & CSS", type="primary")


        st.subheader("Tools")
        b1,b2 = st.columns(2)
        with b1:
            st.button("GitHub", type="primary")
            st.button("JUNIT", type="primary")
            st.button("Matplotlib", type="primary")
        with b2:
            st.button("Git", type="primary")
            st.button("Firebase", type="primary")
            st.button("Streamlit", type="primary")


    st.write(" \n")
    relevant_coursework, certificates, spoken_languages = st.tabs(["Relevant coursework", "Certificates", "Spoken Languages"])
    with relevant_coursework:
        r1, r2 = st.columns(2)
        with r1:
            st.subheader("Software Design and Analysis I & II:")
            st.write("Developed a strong foundation in designing and analyzing complex software systems. Gained experience with software design patterns, architecture, and best practices for creating scalable and maintainable applications.")
            st.write(" ")
            st.write(" ")
            st.subheader("Computer Architecture I & II:")
            st.write("Gained a comprehensive understanding of the inner workings of computer systems, including hardware-software interactions, processor design, memory management, and performance optimization.")
        with r2:
            st.subheader("Data Structures & Algorithms:")
            st.write("Acquired in-depth knowledge of essential data structures and algorithms, with a focus on optimizing problem-solving techniques. Applied these principles in various coding projects to improve efficiency and performance.")

    with certificates:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("JP Morgan Chase & Co. Software Engineering Lite Job Simulation")
            st.write("- Completed a simulation focused on the process of completing an engineering ticket for a system in the credit-card rewards department of JPMorgan Chase & Co.\n- Created a new class to get an existing system up and running \n- Wrote a test suite for the class added")
            with st.popover("Certificate"):
                st.image('Images/JP-forage.png')
                st.write("Issued April 2024")
        with c2:
            st.subheader("EFSET English Certificate")
            st.write("77/100")
            st.write("C2 Advanced")
            with st.popover("Certificate"):
                st.image('Images/english-certificate.png')
                st.write("Issued January 2023")

    with spoken_languages:
        s1, s2 = st.columns(2)
        with s1:
            st.subheader("English")
            st.write("Fluent (C2 Advanced - EFSET English Certificate)")
        with s2:
            st.subheader("Spanish")
            st.write("Native Speaker")