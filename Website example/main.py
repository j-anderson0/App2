import streamlit as st 
import pandas as pd 

st.set_page_config(layout="wide")

col1 = st.columns(1)

st.title("The Best Company")
content = """
    <div style='text-align: justify; font-size: 20px;'>
    Great achievements are rarely the work of a single person. 
         Our success is built on the foundation of collaboration, 
         where diverse ideas converge, creating innovative solutions. 
         Together, as a unified team, we transform challenges into 
         opportunities, driving our collective mission forward.<br><br>
         """

st.markdown(content, unsafe_allow_html=True)


st.header("Our Team")

col2, col3, col4 = st.columns(3)
df = pd.read_csv("data.csv")
with col2:
    for index,row in df[:4].iterrows():
        #Add the first and last name together and capitalize the first letter of each
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        #Write the role
        st.write(row["role"])
        #Display the image
        st.image("images/" + row["image"]) 
with col3:
    for index,row in df[5:8].iterrows():
        first_name = row["first name"].capitalize()
        last_name = row["last name"].capitalize()
        st.subheader(first_name + " " + last_name)
        st.write(row["role"])
        st.image("images/" + row["image"]) 
with col4:
    for index,row in df[9:].iterrows():
        first_name = row["first name"].capitalize()
        last_name = row["last name"].capitalize()
        st.subheader(first_name + " " + last_name)
        st.write(row["role"])
        st.image("images/" + row["image"])