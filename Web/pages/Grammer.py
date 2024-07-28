import streamlit as st
import language_tool_python 
st.title("Grammer Checker")
txt=st.text_area("Type here")

def check_grammar(text):
    parser = language_tool_python.LanguageToolPublicAPI('en-US')
    result = parser.check(text)
    ans = parser.correct(text)
    return ans
st.write("Corrected text")
st.markdown("---")
st.write(check_grammar(txt))
st.write("by Arush")