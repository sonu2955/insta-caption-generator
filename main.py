import random
import openai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Mood to example topics
mood_topic_examples = {
    "Romantic": ["A cafe date", "Sunset with partner", "Anniversary vibes"],
    "Funny": ["Awkward selfie", "Monday mood", "Too cool for logic"],
    "Adventure": ["On top of a mountain", "Road trip moments", "Jungle walk"],
    "Motivational": ["Gym grind", "Early morning hustle", "Never give up"],
    "Friends": ["Squad goals", "Throwback party", "Weekend with homies"],
    "Travel": ["Paris streets", "Beach getaway", "Backpacking vibes"],
    "Food": ["Pasta night", "Dessert first", "Street food vibes"],
    "Fitness": ["Leg day", "Post-run glow", "Healthy habits"],
    "Fashion": ["OOTD", "New drop alert", "Styled to slay"]
}

# Global in-session memory
caption_history = []
last_inputs = {"mood": None, "topic": None, "type": None}

def get_topic_example(mood):
    return random.choice(mood_topic_examples.get(mood, ["Your photo story"]))

def get_random_seed():
    seed_phrases = [
        "Be a creative pro with fresh ideas.",
        "Make the tone feel real and human.",
        "Avoid repeating common IG lines.",
        "Focus on uniqueness and good vibes.",
        "Make it sound original and natural.",
        "No cliché. Just real and creative."
    ]
    return random.choice(seed_phrases)

def get_prompt(caption_type, mood, topic):
    system_seed = get_random_seed()

    history_note = ""
    if caption_history:
        joined_history = "\n".join(f"- {c}" for c in caption_history)
        history_note = f"\nAvoid repeating or copying any of these recent captions:\n{joined_history}"

    if caption_type == "Story":
        base_prompt = f"""{system_seed}
You are helping someone write a short Instagram Story caption. It should feel expressive, emotional, or casual — like a vibe or mood they're feeling today.
Write a 1-liner or short aesthetic caption for a story about '{topic}' in a '{mood}' mood.
Use emojis if it fits. Keep it natural and relatable. Output only the caption.
"""

    elif caption_type == "Post":
        base_prompt = f"""{system_seed}
You are a social media expert writing short, stylish Instagram photo post captions.
Write a cool, confident caption for a photo about '{topic}' in a '{mood}' mood.
Make it:
- 1–2 lines
- Catchy and real
- Not too deep or fake
- Emojis allowed, but natural
Output only the caption.
"""

    elif caption_type == "Notes":
        base_prompt = f"""{system_seed}
You're helping someone post a daily quote or note on Instagram. It should reflect their current thoughts, mindset, or something inspiring.
Write a short, meaningful daily note based on the theme '{topic}' in a '{mood}' tone.
Keep it grounded, original, and not generic. Emojis optional. Output only the quote.
"""

    elif caption_type == "Reels":
        base_prompt = f"""{system_seed}
You are writing a punchy caption for an Instagram Reel. It should match a fast, catchy video style — with attitude or trendiness.
Write a short, bold caption for a reel about '{topic}' in a '{mood}' mood.
Make it viral-style. Use short phrases, emojis, or even something cryptic. Output only the caption.
"""

    elif caption_type == "Attitude & stylish":
        base_prompt = f"""{system_seed}
You're writing a powerful Instagram caption that shows confidence and style.
Write a bold, stylish, and attitude-filled caption based on '{topic}' in a '{mood}' mood.
Make it short, impactful, and cool. Use emojis to add energy. No explanation, just the caption.
"""

    else:
        base_prompt = f"""{system_seed}
Write a short, creative Instagram caption for a post about '{topic}' in a '{mood}' mood.
Keep it fun, confident, and real.
"""

    return base_prompt + history_note

def generate_caption(caption_type, mood, topic):
    global last_inputs, caption_history

    # Reset history if any input changed
    if mood != last_inputs["mood"] or topic != last_inputs["topic"] or caption_type != last_inputs["type"]:
        caption_history.clear()
        last_inputs = {"mood": mood, "topic": topic, "type": caption_type}

    prompt = get_prompt(caption_type, mood, topic)

    tries = 0
    max_attempts = 5
    caption = ""

    while tries < max_attempts:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a skilled caption writer with a natural tone. Keep things real, creative, and unique."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=60,
            temperature=1.0,
            top_p=0.95
        )

        new_caption = response.choices[0].message["content"].strip()

        if new_caption not in caption_history:
            caption = new_caption
            break  # Found unique
        tries += 1

    if caption:
        caption_history.append(caption)
        if len(caption_history) > 5:
            caption_history.pop(0)

    return caption
