import streamlit as st
import cohere as ai
token=st.secrets["TOKEN"]
def gen(prompt):
    co = ai.Client(token)
    mdl="command-xlarge-nightly"
    response = co.generate(
        model=mdl,
        prompt=prompt,
        max_tokens=1000 
    )
    return response.generations[0].text.strip()
msg=st.container(height=250)
pr=msg.chat_input()
with msg.chat_message("user"):
    msg.chat_message("user").write(pr)
    msg.chat_message("assistant").write(gen(pr))
