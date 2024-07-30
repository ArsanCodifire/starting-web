import streamlit as st
import pyrebase 
firebaseConfig = {'apiKey': "AIzaSyDm2HeGl3bApix5KsbhI8NOjdwXkhNTaJM",
                  'authDomain': "trialauth-7eea1.firebaseapp.com",
                  'databaseURL': "https://trialauth-7eea1.firebaseio.com",
                  'projectId': "trialauth-7eea1",
                  'storageBucket': "trialauth-7eea1.appspot.com",
                  'messagingSenderId': "441088628124",
                  'appId': "1:441088628124:web:59f51ba5b6a475032f2459",
                  'measurementId': "G-TNR2V3DEQD"}

fb=pyrebase.initialize_app(firebaseConfig)
auth=fb.auth()
def signin():
  ul=auth.create_user_with_email_and_password(email,psd)
  if ul:
    st.title(f"Welcome{usr}")
#comment
lg=st.form("Sign in")
usr=lg.text_input("Username")
email=lg.text_input("Email")
psd=lg.text_input("Password")
frmbtn=st.form_submit_button("Login",help=None,on_click=signin)
