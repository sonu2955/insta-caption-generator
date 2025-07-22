import openai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_caption(prompt_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # use "gpt-4" if upgraded
            messages=[
                {"role": "system", "content": "You're a helpful assistant who writes short, cool, trendy Instagram captions."},
                {"role": "user", "content": f"Generate a caption for: {prompt_text}"}
            ],
            temperature=0.8,
            max_tokens=100
        )
        caption = response['choices'][0]['message']['content'].strip()
        return caption
    except Exception as e:
        return f"Error: {str(e)}"
