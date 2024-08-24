import streamlit as st
import cohere as ai

token=st.secrets["TOKEN"]
def gen(prompt,mdl):
    co = ai.Client(token)
    response = co.generate(
        model=mdl,
        prompt=prompt,
        max_tokens=1000 
    )
    return response.generations[0].text.strip()

mdl=st.selectbox("Models",["command-xlarge-nightly","command-medium-nightly","generate-code-nightly"]) 

msg=st.container(height=350)
pr=msg.chat_input()
if pr:
    with msg.chat_message("user"):
        msg.markdown(pr)
    with msg.chat_message("assistant"):
        msg.markdown(gen(pr,mdl))
