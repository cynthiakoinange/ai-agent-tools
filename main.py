import streamlit as st
from agent import agent

st.title("AI Agent With Tools")

user_input = st.text_input("Enter your query:")

if st.button("Run"):
    result = agent.run(user_input)
    st.write(result)
