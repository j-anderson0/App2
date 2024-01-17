import streamlit as st

def send_email(message):
    # Implement the email sending logic here
    pass

with st.form(key='email_form'):
    email = st.text_input(label='Your Email Address')
    topic = st.selectbox(label='What topic do you want to discuss?', options=['Job Inquiry', 'Project Proposals', 'Other'])
    message = st.text_area(label='Text')
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        send_email(message)  # Send the original message
        formatted_text = f"From: {email}\nTopic: {topic}\nMessage: {message}"
        st.info("Your email was sent successfully!")
        st.text("Formatted Text:")
        st.write(formatted_text)  # Display the formatted text
