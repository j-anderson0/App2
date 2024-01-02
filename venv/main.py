import streamlit as st 

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/replacement_photo.tiff", width=700)
    
with col2:
    st.title("J Mathias")
    content = """Hi! I'm J,humble student of the world. I'm a data scientist and a budding software engineer. 
    I'm passionate about using data to solve problems and build products that make life easier. 
    I'm a self-taught programmer, and I'm always looking for opportunities to learn and grow. 
    I'm currently looking for a job as a data scientist or software engineer. 
    If you're looking for a passionate, hard-working, and dedicated person to join your team, please reach out to me. I'd love to hear from you!
    """
    st.write(content)