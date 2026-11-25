# ✦ Sika AI — Intelligent ChatGPT Clone

A modern, compact, and responsive ChatGPT-style AI assistant powered by **Google Gemini API** (`gemini-2.5-flash`) and built with **Streamlit**.

---

## ✨ Features

- 🤖 **Multiple Gemini Models**: Switch smoothly between `gemini-2.5-flash`, `gemini-2.0-flash`, and `gemini-1.5-flash`.
- 🌓 **Dual Themes**: Instant Dark Mode and High-Contrast Light Mode with full moon / half moon toggle.
- 📄 **PDF Analysis**: Upload any PDF document up to 200MB and chat with its content.
- 🧠 **Custom System Prompt**: Customize the AI's persona, tone, and behavior in real-time.
- 📱 **Mobile-First Design**: Zero edge glitches, compact widgets, and a smooth collapsible sidebar for phones and desktops.
- 🗑️ **One-Click Clear**: Instantly reset conversation history.

---

## 🛠️ Tech Stack

- **Frontend & UI**: Streamlit, Custom HTML5 & Modern CSS3
- **AI Brain**: Google Gemini via `google-genai` SDK
- **Security**: Environment-based API keys (`python-dotenv`) & Streamlit Secrets

---

## 🚀 Local Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/SBharti1983/sika-ai.git
   cd sika-ai
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Google Gemini API Key:**
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Launch Sika AI:**
   ```bash
   streamlit run chatgpt_clone.py
   ```

---

*Built with passion by Sikandar ✦*
