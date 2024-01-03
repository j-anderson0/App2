import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/replacement_photo.tiff", width=400)

with col2:
    st.title("J Mathias")
    content = """
    Hi! I'm J, humble student of the world. I'm a data scientist and a budding software engineer. 
    I'm passionate about using data to solve problems and build products that make life easier. 
    I'm a self-taught programmer, and I'm always looking for opportunities to learn and grow. 
    I'm currently looking for a job as a data scientist or software engineer. 
    If you're looking for a passionate, hard-working, and dedicated person to join your team, please reach out to me. 
    I'd love to hear from you!
    """
    st.write(content)  # This will display the content within the right column under the title

# This section will be outside the 'with col2' context, and will display at the bottom of the page.
st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
