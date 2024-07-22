import streamlit as st
import os
import requests
# from dotenv import load_dotenv
# load_dotenv()

url = st.secrets["URL"] 
#if "URL" in st.secrets else os.getenv("URL")

st.title("🦅 Rowdybot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    data = {"user_message": prompt}
    response = requests.post(url, json=data)
    msg = response.json()["message"]
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
