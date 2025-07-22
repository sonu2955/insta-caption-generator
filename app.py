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

# --- Mood Selection ---
mood = st.selectbox("🎭 What's your mood today?", ["😊 Happy", "😢 Sad", "✈️ Travel", "❤️ Love"])

# --- Topic Selection ---
topics = {
    "😊 Happy": ["Travel", "Food", "Friends"],
    "😢 Sad": ["Life", "Alone", "Breakup"],
    "✈️ Travel": ["Mountains", "Beach", "Adventure"],
    "❤️ Love": ["Romantic", "Self Love", "Crush"]
}
topic = st.selectbox("📌 Pick a topic", topics[mood])

# --- Generate Button ---
if st.button("✨ Generate My Caption"):
    if mood and topic:
        caption = generate_caption(mood, topic)
        st.success(f"📝 **Your Caption:**\n\n{caption}")
    else:
        st.warning("Please select both mood and topic.")
