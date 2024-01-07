import streamlit as st 
import pandas as pd 

st.set_page_config(layout="wide")

col1 = st.columns(1)

st.title("The Best Company")
st.write("""This is the best company ever! We are the best at everything we do.
         Come kiss our asses and give us your money. And don't forget to tell your friends!
         But seriously, give us your money.""")

st.header("Our Team")

Col2, Col3, Col4 = st.columns([1,1,1])

df = pd.read_csv("data.csv", sep=",")
with col2:
    for index,row in df[["Name", "Position"]].iterrows():
        st.write(row["Name"])
        st.write(row["Position"])
        st.image("images/" + row["image"])
with col3:
    for index,row in df[["Name", "Position"]].iterrows():
        st.write(row["Name"])
        st.write(row["Position"])
        st.image("images/" + row["image"])
with col4:
    for index,row in df[["Name", "Position"]].iterrows():
        st.write(row["Name"])
        st.write(row["Position"])
        st.image("images/" + row["image"])