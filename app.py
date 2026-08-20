import streamlit as st
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from prompt import get_prompt, get_qa_prompt, get_summary_prompt

load_dotenv()

st.set_page_config(
    page_title="AI Assistant Suite",
    page_icon="🤖",
    layout="centered"
)

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-20b"
)

# ---------------- Sidebar ----------------

st.sidebar.title("🤖 Choose a Tool")

mode = st.sidebar.radio(
    "Select Mode",
    [
        "🍽️ Restaurant Name Generator",
        "💬 Ask Anything",
        "📝 Summarize Text"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Powered by Groq Llama 3.1")

# ---------------- Restaurant Generator ----------------

if mode == "🍽️ Restaurant Name Generator":

    st.title("🍽️ AI Restaurant Name Generator")

    cuisine = st.text_input("Cuisine")
    theme = st.text_input("Theme")

    if st.button("Generate"):

        if cuisine and theme:

            with st.spinner("Generating..."):
                prompt = get_prompt(cuisine, theme)
                response = llm.invoke(prompt)

            st.subheader("Result")
            st.write(response.content)

        else:
            st.warning("Please enter both cuisine and theme.")

# ---------------- Chat ----------------

elif mode == "💬 Ask Anything":

    st.title("💬 Ask Anything")
    st.caption("Ask questions about coding, science, history, or anything else.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(message)

    user_question = st.chat_input("Ask me anything...")

    if user_question:

        st.session_state.chat_history.append(("user", user_question))

        with st.chat_message("user"):
            st.markdown(user_question)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                prompt = get_qa_prompt(
                    user_question,
                    st.session_state.chat_history
                )

                response = llm.invoke(prompt)

                st.markdown(response.content)

        st.session_state.chat_history.append(
            ("assistant", response.content)
        )

    if st.session_state.chat_history:

        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

# ---------------- Summarizer ----------------

elif mode == "📝 Summarize Text":

    st.title("📝 Text Summarizer")

    text = st.text_area(
        "Paste your text",
        height=250
    )

    length = st.select_slider(
        "Summary Length",
        options=["short", "medium", "detailed"],
        value="medium"
    )

    if st.button("Summarize"):

        if text.strip():

            with st.spinner("Summarizing..."):

                prompt = get_summary_prompt(text, length)

                response = llm.invoke(prompt)

            st.subheader("Summary")
            st.write(response.content)

        else:
            st.warning("Please paste some text first.")
