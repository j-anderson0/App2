import streamlit as st
from send_email import send_email

st.header('Contact Us')

with st.form(key='email_form'):
    email = st.text_input(label='Your Email Address')
    topic = st.selectbox(label='What topic do you want to discuss?', options=['Job Inquiry', 'Project Proposals', 'Other'])
    message = st.text_area(label='Text')
    formatted_text = f"""\
From:{email}
Topic:{topic}
Message:{message}
"""
    submit_button = st.form_submit_button(label='Submit')
    print(submit_button)
    if submit_button:
        send_email(message)  # send the original message, not the formatted text
        st.info("Your email was sent successfully!")