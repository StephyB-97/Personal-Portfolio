import streamlit as st


def show_projects():
    st.markdown("""
        <style>
        .centered-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 30vh; /* Adjust this value based on your layout needs */
            text-align: center;
        }
        </style>
        <div class="centered-container">
            <h1>PROJECTS</h1>
            <h6>Explore a collection of personal projects I've developed. Each project reflects my passion for coding and problem-solving, showcasing the skills and knowledge I've gained throughout my journey in computer science</h6>
        </div>
        """, unsafe_allow_html=True)

    st.write(" ")
    st.write(" ")

    # Code for student assistant coming soon
    with st.container(border=True, height=490):
        a1_assistant, a2_assistant = st.columns([1, 1])
        with a1_assistant:
            st.subheader("AI Student Assistant Tool")
            st.image('Images/student-assistant.png')
        with a2_assistant:
            st.subheader(" ")
            st.write("This Python-powered AI Student Assistant helps students manage their academic and personal schedules efficiently. Users can input their semester schedule, study requirements, assignments, and exams. The tool generates a daily to-do list, prioritizing tasks by deadlines and importance, and adds preparatory tasks in advance with an integrated AI chat feature, students can ask questions and receive personalized responses based on their schedule. The assistant also includes an internship tracker that aggregates opportunities, tracks applications, and provides easy access to internship records. This project combines time management, AI support, and career tools in one streamlined application.")


    #Code for one whole card
    with st.container(border=True, height=460):
        a1, a2 = st.columns([1, 1])
        with a1:
            st.subheader("Portfolio Management Dashboard")
            st.image('Images/portfolio-dashboard.png')
        with a2:
            st.subheader(" ")
            st.write("A portfolio management dashboard that helps users track their investments, analyze performance over time, and compare growth against market indices like the S&P 500. With real-time data integration and intuitive design.")
            st.subheader("Tech Stack")
            b1,b2,b3 = st.columns([1, 1,1])
            with b1:
                st.button("Python", type="primary")
            with b2:
                st.button("Firebase", type="primary")
            with b3:
                st.button("Streamlit", type="primary")
            st.write(" ")
            st.write(" ")

            view_code, live_demo = st.columns([1, 1])
            with view_code:
                st.write(" ")
                st.markdown('<a href="https://github.com/StephyB-97/Portfolio_Management" style="color:blue; text-decoration:none;">View Code</a>',unsafe_allow_html=True)
            with live_demo:
                st.write(" ")
                st.markdown('<a href="https://sb-portfolio-management.streamlit.app" style="color:blue; text-decoration:none;">Live Demo</a>',unsafe_allow_html=True)





    # Code for one whole card (Rentals website)
    with st.container(border=True, height=560):
        a1_rental, a2_rental = st.columns([1, 1])
        with a1_rental:
            st.subheader("Dynamic Rentals: Cloud-Optimized Web Application")
            st.image('Images/rental.png')
        with a2_rental:
            st.subheader(" ")
            st.write(" ")
            st.write("Dynamic Rentals is a secure and scalable property rental app that enhances user experience with cloud-based image storage, dynamic map features, and robust authentication. Integration with Cloudinary and Mapbox ensures fast response times and seamless navigation, making property exploration efficient and secure for tenants.")
            st.subheader("Tech Stack")
            b1_rental, b2_rental, b3_rental = st.columns([1, 1, 1])
            with b1_rental:
                st.button("JavaScript", type="primary")
                st.button("MongoDB", type="primary")
            with b2_rental:
                st.button("Express", type="primary")
                st.button("HTML & CSS", type="primary")
            with b3_rental:
                st.button("Passport", type="primary")
                st.button("Node.js", type="primary")

            st.write(" ")
            view_code_rental, live_demo_rental = st.columns([1, 1])
            with view_code_rental:

                st.markdown('<a href="https://github.com/StephyB-97/Rentals" style="color:blue; text-decoration:none;">View Code</a>',
                            unsafe_allow_html=True)
                with live_demo_rental:

                    st.markdown('<a href="https://sb-portfolio-management.streamlit.app" style="color:blue; text-decoration:none;">Live Demo</a>',
                            unsafe_allow_html=True)

     # Code for one whole card
    with st.container(border=True, height=460):
        a1_budget, a2_budget = st.columns([1, 1])
        with a1_budget:
            st.subheader("Budget Tool")
            st.image('Images/budget.png')
        with a2_budget:
            st.subheader(" ")
            st.write("A budgeting tool built with JavaScript and Express that allows users to set a monthly budget, track expenses by name and price, and view the total spent, remaining balance, and percentage of the budget utilized. The tool also includes a detailed list of all expenses, providing a clear financial overview for effective budget management.")
            st.subheader("Tech Stack")
            b1_budget, b2_budget = st.columns([1, 1])
            with b1_budget:
                st.button("Javascript", type="primary")
            with b2_budget:
                st.button("express", type="primary")

            view_code_budget, live_demo_budget = st.columns([1, 1])
            with view_code_budget:
                st.write(" ")
                st.markdown('<a href="https://github.com/StephyB-97/Budget-Application" style="color:blue; text-decoration:none;">View Code</a>',
                        unsafe_allow_html=True)
            with live_demo_budget:
                st.write(" ")
                st.markdown('<a href="https://sb-portfolio-management.streamlit.app" style="color:blue; text-decoration:none;">Live Demo</a>',
                        unsafe_allow_html=True)
