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