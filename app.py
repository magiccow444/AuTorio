import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# ---------- Ideas ----------
# - Add Tradinview API for stock stuff
# - Add ChatGPT API for some module
# - Maybe add a general module for any AI
# - Some kind of communication module like through Discord/WhatsApp/Gmail whatever is easiest
# - Module for MediaPipe hands
# - Module for Playwright for web automation and scraping
# - MODULE FOR POSTING VIDEOS?? + Module for text generationfor youtube/social media hehe



# ---------- Loading and functions ----------

load_dotenv()
genai.configure(api_key=os.getenv("MY_GEMINI_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_text(text: str) -> str:
    prompt = f"Summarize the following text:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()

# ---------- Application stuff ----------

st.title("⚙️ AuTorio (Gemini Edition)")

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
