import streamlit as st
from deta import Deta
api="EyDDRDhg_iyiNV4ShnC617vy7Zww4iEJxFbTKUVzz"
dt=Deta(api)
db=dt.Base("Loginid")

def signin():
    db.put({"key":email,"username":usr,"password":psd})
    st.write(f"Hi{usr}")
def login():
    log_e=dB.fetch()["key"]
    log_p=dB.fetch()["password"]
    log_u=dB.fetch()["username"]
    if emaill==log_e:
        if psdl==log_p:
            st.write(f"Welcome back{log_u}")
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
