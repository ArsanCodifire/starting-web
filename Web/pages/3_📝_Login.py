import streamlit as st
api="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRvanZpYm16bHZvcW5jY3p0cHZiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjI1MjQzMzgsImV4cCI6MjAzODEwMDMzOH0.O88obpltWJCPqXrWSu_mKsgvEpU3xAREv8A9SMbjqyY"
def signin():
    st.write(f"Hi{usr}")
def login():
    st.write(f"Welcome back{usr}")
#comment
login=st.selectbox("Choose",options=("NA","Sign In","Login"))
if login=="Login":
    lg=st.form("Sign in")
    emaill=lg.text_input("Email")
    psdl=lg.text_input("Password",type="password")
    btn=lg.form_submit_button("Sign in",help=None,on_click=signin)
elif login=="Sign In":
    lg=st.form("Sign in")
    usr=lg.text_input("Username")
    email=lg.text_input("Email")
    psd=lg.text_input("Password",type="password")
    btn=lg.form_submit_button("Sign in",help=None,on_click=signin)
else:
    lol=1
