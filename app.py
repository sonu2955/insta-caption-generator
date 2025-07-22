import streamlit as st
from main import generate_caption

# --- Page Setup ---
st.set_page_config(page_title="Caption Generator", page_icon="✨", layout="centered")

# --- Title & Subtitle ---
st.markdown(
    "<h1 style='text-align: center; color: #ff4b4b;'>📸 CaptionCraft AI</h1>"
    "<h4 style='text-align: center; color: gray;'>Turn your mood into magic 💬✨</h4><br>",
    unsafe_allow_html=True
)

# --- Custom CSS Styling ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fef6f0;
        font-family: 'Segoe UI', sans-serif;
    }
    .css-1cpxqw2 {padding-top: 2rem;}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Mood and Topic Mappings ---
mood_options = {
    "😊 Happy": "😊 happy",
    "😢 Sad": "😢 sad",
    "✈️ Travel": "✈️ travel",
    "❤️ Love": "❤️ love"
}

topic_options = {
    "😊 Happy": ["Travel", "Food", "Friends"],
    "😢 Sad": ["Life", "Alone", "Breakup"],
    "✈️ Travel": ["Mountains", "Beach", "Adventure"],
    "❤️ Love": ["Romantic", "Self Love", "Crush"]
}

# --- Topic Key Mapping to lowercase ---
topic_key_map = {
    "Travel": "travel",
    "Food": "food",
    "Friends": "friends",
    "Life": "life",
    "Alone": "alone",
    "Breakup": "breakup",
    "Mountains": "mountains",
    "Beach": "beach",
    "Adventure": "adventure",
    "Romantic": "romantic",
    "Self Love": "self love",
    "Crush": "crush"
}

# --- Mood Selection ---
selected_mood = st.selectbox("🎭 What's your mood today?", list(mood_options.keys()))

# --- Topic Selection ---
selected_topic = st.selectbox("📌 Pick a topic", topic_options[selected_mood])

# --- Generate Button ---
if st.button("✨ Generate My Caption"):
    mood_key = mood_options[selected_mood]
    topic_key = topic_key_map[selected_topic]

    caption = generate_caption(mood_key, topic_key)
    st.success(f"📝 **Your Caption:**\n\n{caption}")
