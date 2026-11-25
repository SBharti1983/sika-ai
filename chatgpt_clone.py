import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
raw_key = os.getenv("GEMINI_API_KEY") or (st.secrets.get("GEMINI_API_KEY") if hasattr(st, "secrets") else None)
API_KEY = str(raw_key).strip().strip('"').strip("'") if raw_key else ""

st.set_page_config(
    page_title="Sika AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "theme" not in st.session_state:
    st.session_state.theme = "dark"

if "messages" not in st.session_state:
    st.session_state.messages = []


def load_css(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


load_css("style.css")

if st.session_state.theme == "light":
    load_css("style_light.css")


@st.cache_resource
def get_client(key: str):
    return genai.Client(api_key=key)


client = get_client(API_KEY)

with st.sidebar:
    st.markdown("""
    <div class="sb-logo">
        <div class="sb-logo-icon">✦</div>
        <div class="sb-logo-title">Sika AI</div>
        <div class="sb-logo-sub">Powered by Google Gemini</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-section">', unsafe_allow_html=True)
    st.markdown('<span class="sb-label">🤖 AI Model</span>', unsafe_allow_html=True)
    selected_model = st.selectbox(
        label="model",
        options=["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"],
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sb-section">', unsafe_allow_html=True)
    st.markdown('<span class="sb-label">🧠 System Prompt</span>', unsafe_allow_html=True)
    system_prompt = st.text_area(
        label="system",
        value="You are a helpful, smart, and friendly AI assistant. Answer clearly and concisely.",
        height=80,
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sb-section">', unsafe_allow_html=True)
    st.markdown('<span class="sb-label">📄 Upload PDF</span>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "pdf",
        type=["pdf"],
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    pdf_text = ""
    if uploaded_file:
        pdf_bytes = uploaded_file.read()
        text_parts = []
        start = 0
        while True:
            start = pdf_bytes.find(b'BT', start)
            if start == -1:
                break
            end = pdf_bytes.find(b'ET', start)
            if end == -1:
                break
            chunk = pdf_bytes[start:end]
            for part in chunk.split(b'('):
                if b')' in part:
                    text = part[:part.index(b')')].decode('latin-1', errors='ignore')
                    if text.strip():
                        text_parts.append(text)
            start = end + 2
        pdf_text = ' '.join(text_parts) if text_parts else ""
        if pdf_text:
            st.success("✅ PDF Ready!")
        else:
            st.warning("⚠️ Could not extract text from this PDF.")

    st.markdown('<div class="sb-section sb-actions">', unsafe_allow_html=True)
    if st.button("🗑️  Clear Conversation", key="clear_btn"):
        st.session_state.messages = []
        st.session_state.pop(f"chat_{selected_model}", None)
        st.rerun()

    is_dark = st.session_state.theme == "dark"
    moon_text = "🌕  Switch to Light" if is_dark else "🌓  Switch to Dark"
    if st.button(moon_text, key="theme_toggle_btn"):
        st.session_state.theme = "light" if is_dark else "dark"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="sb-footer">Built by Sikandar ✦</div>
    """, unsafe_allow_html=True)


chat_key = f"chat_{selected_model}"
if chat_key not in st.session_state:
    st.session_state[chat_key] = client.chats.create(
        model=selected_model,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt
        )
    )

if user_input := st.chat_input("Message Sika AI..."):
    full_prompt = (
        f"Context from uploaded PDF:\n---\n{pdf_text[:8000]}\n---\n"
        f"User question: {user_input}"
    ) if pdf_text else user_input

    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = st.session_state[chat_key].send_message(full_prompt)
        ai_reply = response.text
    except Exception as e:
        st.session_state.pop(chat_key, None)
        ai_reply = f"Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    st.rerun()

if not st.session_state.messages:
    with open("welcome_screen.html", "r", encoding="utf-8") as f:
        st.markdown(f.read(), unsafe_allow_html=True)
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
