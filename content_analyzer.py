import os
from openai import OpenAI

def analyze_content(text, query, api_key):
    client = OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful research assistant."},
                {"role": "user", "content": f"Summarize this content with respect to the query: {query}\n\nContent:\n{text}"}
            ],
            max_tokens=100,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error during content analysis: {e}")
        return "Summary not available due to an error."
