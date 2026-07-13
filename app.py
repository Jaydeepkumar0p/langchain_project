import streamlit as st
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from prompt import get_prompt, get_qa_prompt, get_summary_prompt

load_dotenv()

st.set_page_config(page_title="AI Assistant Suite", page_icon="🤖", layout="centered")

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)

# ---------- Sidebar: mode selector ----------
st.sidebar.title("🤖 Choose a Tool")
mode = st.sidebar.radio(
    "Select mode",
    ["🍽️ Restaurant Name Generator", "💬 Ask Anything", "📝 Summarize Text"],
)

st.sidebar.markdown("---")
st.sidebar.caption("Powered by Groq Llama 3.1")

# ================= MODE 1: Restaurant Generator =================
if mode == "🍽️ Restaurant Name Generator":
    st.title("🍽️ AI Restaurant Name Generator")

    cuisine = st.text_input("Enter Cuisine (Indian, Italian, Chinese)")
    theme = st.text_input("Enter Theme (Luxury, Street Food, Modern)")

    if st.button("Generate"):
        if cuisine and theme:
            with st.spinner("Cooking up ideas..."):
                prompt = get_prompt(cuisine, theme)
                response = llm.invoke(prompt)
            st.subheader("🍴 Result")
            st.write(response.content)
        else:
            st.warning("Please enter both fields")

# ================= MODE 2: Ask Anything (Chat) =================
elif mode == "💬 Ask Anything":
    st.title("💬 Ask Anything")
    st.caption("Chat with an AI on any topic — general knowledge, coding, advice, etc.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []  # list of (role, message)

    # Render past messages
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(msg)

    user_question = st.chat_input("Ask me anything...")

    if user_question:
        # Show user message immediately
        st.session_state.chat_history.append(("user", user_question))
        with st.chat_message("user"):
            st.markdown(user_question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                prompt = get_qa_prompt(user_question, st.session_state.chat_history)
                response = llm.invoke(prompt)
                st.markdown(response.content)

        st.session_state.chat_history.append(("assistant", response.content))

    if st.session_state.chat_history:
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

# ================= MODE 3: Summarize Text =================
elif mode == "📝 Summarize Text":
    st.title("📝 Text Summarizer")

    text_input = st.text_area("Paste the text you want summarized", height=250)
    length = st.select_slider(
        "Summary length",
        options=["short", "medium", "detailed"],
        value="medium",
    )

    if st.button("Summarize"):
        if text_input.strip():
            with st.spinner("Summarizing..."):
                prompt = get_summary_prompt(text_input, length)
                response = llm.invoke(prompt)
            st.subheader("📋 Summary")
            st.write(response.content)
        else:
            st.warning("Please paste some text first")
