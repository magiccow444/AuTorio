import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# ---------- Loading and functions ----------

load_dotenv()
genai.configure(api_key=os.getenv("MY_GEMINI_KEY"))

model = genai.GenerativeModel("gemini-2.5-pro")

def summarize_text(text: str) -> str:
    prompt = f"Summarize the following text:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()

# ---------- Application stuff ----------

st.title("🧠 AutoPilotOps (Gemini Edition)")

uploaded = st.file_uploader("Upload a .txt file", type=["txt"])

if uploaded:
    raw = uploaded.read().decode()
    st.subheader("Original Text:")
    st.text_area("", raw, height=200)

    if st.button("Summarize"):
        with st.spinner("Summarizing with Gemini..."):
            summary = summarize_text(raw)
        st.subheader("Summary:")
        st.write(summary)
