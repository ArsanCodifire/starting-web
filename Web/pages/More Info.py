import streamlit as st
st.title("Website created by Arush Krishna A.S.")
st.title("My website")
st.write("This is the power of python")
yn=st.selectbox("Do you know python ?",["Yes","No"])
if yn=="Yes":
    st.write("Good,your the best!!")
else:
    st.write("No Problem.")
  
