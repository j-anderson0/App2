import streamlit as st
from send_email import send_email

st.header('Contact Us')

with st.form(key='email_form'):
    name = st.text_input(label='Name') 
    email = st.text_input(label='Email')
    message = st.text_area(label='Message')
    message = f"""\
Subject: {name} has sent you a message

From: {email}
{message}
"""
    submit_button = st.form_submit_button(label='Submit')
    print(submit_button)
    if submit_button:
        send_email(message)
        st.info("Your email was sent successfully!")