import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_caption(mood, topic):
    prompt = f"Generate a cool, short Instagram caption for a post that feels {mood} and is about {topic}. Add emojis. Keep it under 20 words."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative social media caption writer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60,
        temperature=0.9
    )

    return response['choices'][0]['message']['content'].strip()
