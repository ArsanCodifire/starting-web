import streamlit as st
from gingerit.gingerit import GingerIt
st.title("Grammer Checker")
txt=st.text_area("Type here")

def check_grammar(text):
    parser = GingerIt() 
    result = parser.check(text)
    ans = parser.correct(text)
    return ans
st.write("Corrected text")
st.markdown("---")
st.write(check_grammar(txt))
st.write("by Arush")
