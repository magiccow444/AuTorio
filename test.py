# import streamlit as st

# st.title("Welcome to AuTorio")
# name = st.text_input("Enter your name:")
# st.write(f"Hello, {name}!")

import streamlit as st

st.title("🧠 AutoPilotOps Flow Builder (Prototype)")

col1, col2, col3 = st.columns(3)

with col1:
    trigger = st.selectbox("Trigger", ["File Upload", "Webhook", "Email"])
with col2:
    processor = st.selectbox("Processor", ["Summarize", "OCR", "Regex Match"])
with col3:
    output = st.selectbox("Output", ["Email", "Save File", "Slack"])

if st.button("Run Pipeline"):
    st.success(f"Trigger: {trigger} → Processor: {processor} → Output: {output}")

