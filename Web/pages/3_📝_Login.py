import streamlit as st


def signin():
  st.write(f"Welcome {usr}")
#comment
st.selectbox("",)
if login="Login":
    lg=st.form("Sign in")
    email=lg.text_input("Email")
    psd=lg.text_input("Password",type="password")
    btn=lg.form_submit_button("Sign in",help=None,on_click=signin)
else:
    lg=st.form("Sign in")
    usr=lg.text_input("Username")
    email=lg.text_input("Email")
    psd=lg.text_input("Password",type="password")
    btn=lg.form_submit_button("Sign in",help=None,on_click=signin)
