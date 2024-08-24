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

mdl=st.selectbox("Models",["command-xlarge-nightly","command-medium-nightly"])
if mdl=="command-xlarge-nightly":
    st.write("Slow chatbot")
elif mdl=="command-medium-nightly":
    st.write("Fast chatbot")

pr=st.chat_input()
if pr:
    with st.chat_message("user"):
        st.markdown(pr)
    with st.chat_message("assistant"):
        st.markdown(gen(pr,mdl))
        st.toast("You are chatting with Cohere AI")
        st.balloons("Yay")
