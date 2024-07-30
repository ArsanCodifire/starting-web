import streamlit as st


def signin():
  st.title(f"Welcome{usr}")
#comment
lg=st.form("Sign in")
usr=lg.text_input("Username")
email=lg.text_input("Email")
psd=lg.text_input("Password")
st.form_submit_button("Login",help=None,on_click=signin)
