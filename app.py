import streamlit as st
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from prompt import get_prompt

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)

st.title("🍽️ AI Restaurant Name Generator")

cuisine = st.text_input("Enter Cuisine (Indian, Italian, Chinese)")
theme = st.text_input("Enter Theme (Luxury, Street Food, Modern)")

if st.button("Generate"):
    if cuisine and theme:
        prompt = get_prompt(cuisine, theme)

        response = llm.invoke(prompt)

        st.subheader("🍴 Result")
        st.write(response.content)
    else:
        st.warning("Please enter both fields")