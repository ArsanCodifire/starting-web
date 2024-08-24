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
with msg.chat_message("user"):
    msg.chat_message("user").write(pr)
    msg.chat_message("assistant").write(gen(pr,mdl))

