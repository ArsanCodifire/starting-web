import streamlit as st
import time
import streamlit.components.v1 as prt
st.set_page_config(page_title="Discord Stats",page_icon=":robot:")
st.title("Discord Pybot is Running")
def reload():
  prt.iframe("https://discord.com/widget?id=1264247217158623262&theme=dark", width=350,height=500)
btn=st.button("Rerun")
if btn:
  reload()
