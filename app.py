import streamlit as st
import requests

st.title("DreamActify ↔ n8n Test")

# Text input
user_input = st.text_input("Say something:")

# On button click, send to n8n webhook
if st.button("Send to n8n"):
    if user_input.strip():
        url = "https://n8n.dreamactify.com/webhook/1922d316-87de-46ef-b4e5-0283114ee83d"
        try:
            response = requests.post(url, json={"message": user_input}, timeout=10)
            st.success(f"n8n response: {response.text}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text first.")
