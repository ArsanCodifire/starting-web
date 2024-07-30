import streamlit as st
import pyrebase as fb
firebaseConfig = {
  "apiKey": "AIzaSyDWruUPKro1RzE5ZejZ2G7ie9Pm22hz814",
  "authDomain": "py-login-55126.firebaseapp.com",
  "databaseURL":"https://console.firebase.google.com/project/py-login-55126/database/py-login-55126-default-rtdb/data/~2F",
  "projectId": "py-login-55126",
  "storageBucket": "py-login-55126.appspot.com",
  "messagingSenderId": "378309201398",
  "appId": "1:378309201398:web:bda344222cbea996030bd7",
  "measurementId": "G-3B7H2D1QD5"
}

fb.initialize_app(firebaseConfig)
auth=fb.auth()
def signin():
  ul=auth.create_user_with_email_and_password(email,psd)
  st.title(f"Welcome{usr}")
lg=st.form("Sign in")
usr=lg.text_input("Username")
email=lg.text_input("Email")
psd=lg.text_input("Password")
frmbtn=st.form_submit_button("Login",help=None,on_click=signin)
