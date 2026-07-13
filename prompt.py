def get_prompt(cuisine, theme):
    return f"""
You are a restaurant branding expert.

Generate:
1. Restaurant Name
2. Tagline
3. 10 Menu Items
4. Short Description

Cuisine: {cuisine}
Theme: {theme}

Make it creative and attractive.
"""


def get_qa_prompt(question, history=None):
    context = ""
    if history:
        for role, msg in history[-6:]:
            context += f"{role}: {msg}\n"

    return f"""
You are a helpful, knowledgeable assistant who can answer questions on any topic.

Conversation so far:
{context}

New question: {question}

Give a clear, accurate, well-structured answer. Use bullet points or short paragraphs where helpful.
"""


def get_summary_prompt(text, length="medium"):
    length_map = {
        "short": "2-3 sentences",
        "medium": "a short paragraph (5-7 sentences)",
        "detailed": "a detailed multi-paragraph summary with key points as bullets",
    }

    detail = length_map.get(length, length_map["medium"])

    return f"""
You are an expert summarizer.

Summarize the following text in {detail}.

Capture the key ideas, avoid fluff, and keep it faithful to the original meaning.

Text:
\"\"\"
{text}
\"\"\"

Summary:
"""