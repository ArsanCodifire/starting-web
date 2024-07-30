import streamlit as st
st.title("Website created by Arush Krishna A.S.")
st.title("My website")
st.write("This is the power of python")
yn=st.selectbox("Do you know python ?",["N/A","Yes","No"])
if yn=="Yes":
    st.write("Good,your the best!!")
elif yn=="No":
    st.write("No Problem.")
else:
    print("Not applicable")
