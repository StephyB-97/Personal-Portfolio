import streamlit as st
from st_social_media_links import SocialMediaIcons


def contact_form():
    st.write(" ")
    st.title("Contact Form")

    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label='Send', type="primary", )

    if submit_button:
        if name and email and message:
            # FormSubmit endpoint
            form_submit_url = "https://formsubmit.co/sbernades1011@gmail.com"

            # Hidden form fields and auto-submit script
            form_code = f"""
            <form action="{form_submit_url}" method="POST" style="display:none;">
                <input type="hidden" name="_captcha" value="false">
                <input type="hidden" name="name" value="{name}">
                <input type="hidden" name="email" value="{email}">
                <input type="hidden" name="message" value="{message}">
                <input type="hidden" name="_template" value="table">
            </form>
            <script>
                document.forms[0].submit();
            </script>
            """

            # Display success message
            st.success("Your message has been sent successfully!")

            # Trigger the form submission
            st.markdown(form_code, unsafe_allow_html=True)
        else:
            st.warning("Please fill out all fields.")

    social_media_links = [
        "https://www.linkedin.com/in/stephanie-bernades/",
        "https://github.com/StephyB-97?tab=repositories",
    ]

    social_media_icons = SocialMediaIcons(social_media_links)

    social_media_icons.render()
