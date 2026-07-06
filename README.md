<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:2E9EF7,100:16C784&height=180&section=header&text=AI%20Restaurant%20Name%20Generator&fontSize=32&fontColor=ffffff&animation=fadeIn" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=2E9EF7&center=true&vCenter=true&width=600&lines=Generate+catchy+restaurant+names+with+AI;Powered+by+LangChain+%2B+Groq+(Llama+3.1);Built+with+Streamlit" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-Llama_3.1-orange" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
</p>

---

## 🍽️ About

A simple AI-powered web app that generates creative restaurant names based on your chosen **cuisine** and **theme** — built with **Streamlit**, **LangChain**, and **Groq's Llama 3.1** model.

## ✨ Demo

<p align="center">
  <!-- Replace this with an actual screenshot or GIF of your app once deployed -->
  <img src="https://via.placeholder.com/700x350?text=Add+a+screenshot+or+GIF+of+your+app+here" alt="App demo" />
</p>

🔗 **Live app:** [your-app-name.streamlit.app](https://your-app-name.streamlit.app)

## 🚀 Features

- 🧠 Uses Groq's blazing-fast `llama-3.1-8b-instant` model via LangChain
- 🎨 Simple, clean Streamlit UI
- ⚡ Instant name generation based on cuisine + theme inputs
- 🔐 Secure API key handling via environment variables / Streamlit secrets

## 🛠️ Tech Stack

<p align="left">
  <img src="https://skillicons.dev/icons?i=python,git,github" />
</p>

## 📦 Installation

Clone the repo and set up locally:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/langchain_project.git
cd langchain_project

python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS/Linux

pip install -r requirements.txt
```

Create a `.env` file in the root folder:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Run the app:

```bash
streamlit run app.py
```

## 📁 Project Structure

```
langchain_project/
├── app.py             # Main Streamlit app
├── prompt.py           # Prompt template logic
├── requirements.txt     # Python dependencies
├── .env                # API keys (not committed)
└── README.md
```

## 🔑 Getting a Groq API Key

1. Sign up at [console.groq.com](https://console.groq.com)
2. Go to **API Keys** → generate a new key
3. Add it to your `.env` file locally, and to **Streamlit Cloud → Settings → Secrets** if deploying

## 🌐 Deployment

This app is deployed on **Streamlit Community Cloud**. To deploy your own copy:

1. Push this repo to your GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → New app
3. Select this repo, set main file to `app.py`
4. Add `GROQ_API_KEY` under **Settings → Secrets**
5. Deploy 🚀

## 📄 License

This project is licensed under the MIT License.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:16C784,100:2E9EF7&height=100&section=footer" />
</p>
