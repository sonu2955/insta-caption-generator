import streamlit as st
import pandas as pd
import os
import random
import base64
from main import generate_caption, get_topic_example

# ------------------- Page Setup -------------------
st.set_page_config(page_title="My_Caption", page_icon="📸", layout="centered")

# ------------------- Descriptions -------------------
descriptions = [
    "💬 A free tool to turn your moods and moments into words.",
    "🤖 Your AI-powered assistant for perfect Instagram captions.",
    "✍️ Write captions that reflect you — every single time.",
    "🎯 Find the perfect Instagram caption for your vibe.",
    "💡 Helping you express yourself through powerful words."
]

# ------------------- Logo Setup (base64) -------------------
logo_path = "assets/logo.png"
with open(logo_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()

# ------------------- UI: Logo + Title -------------------
st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <img src="data:image/png;base64,{encoded_logo}" width="60" style="vertical-align: middle; margin-right: 10px;">
        <span style="font-size: 2.3rem; font-weight: 700; vertical-align: middle;">My_Caption</span>
    </div>
""", unsafe_allow_html=True)

# ------------------- UI: Tagline + Description -------------------
st.markdown(f"""
    <div style="text-align: center; margin-top: 10px;">
        <p style="font-size: 1.05rem; color: gray; margin-bottom: 0.3rem;">
            📍 Find the Perfect Caption for Any Mood
        </p>
        <p style="font-size: 0.95rem; color: #888;">
            {random.choice(descriptions)}
        </p>
    </div>
""", unsafe_allow_html=True)

# ------------------- Mood & Caption Type -------------------
st.markdown("---")
caption_types = ["Story", "Post", "Notes", "Reels", "Attitude & stylish"]
caption_type = st.selectbox("📝 Select Caption Type", caption_types)

mood_emojis = {
    "Romantic": "💖", "Funny": "😂", "Adventure": "🗺️", "Motivational": "💪",
    "Friends": "👯", "Travel": "✈️", "Food": "🍕", "Fitness": "🏋️", "Fashion": "👗"
}
moods = list(mood_emojis.keys())
selected_mood = st.selectbox("🎭 Select Photo Mood", [f"{mood_emojis[m]} {m}" for m in moods])
selected_mood = selected_mood.split(" ", 1)[1]  # Get actual mood text

example_topic = get_topic_example(selected_mood)
st.markdown(f"**📌 Describe Your Photo Topic**  &nbsp;&nbsp; *(e.g., '{example_topic}')*")
topic_input = st.text_input(" ", max_chars=50, placeholder="Type your topic here...✍️")

if topic_input and len(topic_input.strip()) < 5:
    st.warning("Please enter a bit more detailed topic.")


# ------------------- Caption Generation -------------------
if st.button("✨ Generate Caption"):
    if topic_input.strip() == "":
        st.warning("Please enter a topic to generate a caption.")
    else:
        with st.spinner("Generating caption..."):
            caption = generate_caption(caption_type, selected_mood, topic_input)
            st.session_state.caption = caption
            st.session_state.last_input = {
                "mood": selected_mood,
                "type": caption_type,
                "topic": topic_input
            }
            st.session_state.history.insert(0, caption)
            st.session_state.history = st.session_state.history[:5]

# ------------------- Output Caption -------------------
if 'caption' not in st.session_state:
    st.session_state.caption = ""
if 'history' not in st.session_state:
    st.session_state.history = []
if 'last_input' not in st.session_state:
    st.session_state.last_input = {}

if st.session_state.caption:
    st.success("✨ Your Caption:")
    st.code(st.session_state.caption, language='text')

    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("📋 Copy Caption", key="copy_btn", help="Copy to clipboard")
    with col2:
        if st.button("👍 Like this caption", key="like_btn"):
            LIKED_FILE = "liked_captions.csv"
            if os.path.exists(LIKED_FILE):
                liked_df = pd.read_csv(LIKED_FILE)
            else:
                liked_df = pd.DataFrame(columns=["caption", "mood", "type", "topic", "likes"])

            new_entry = {
                "caption": st.session_state.caption,
                "mood": st.session_state.last_input["mood"],
                "type": st.session_state.last_input["type"],
                "topic": st.session_state.last_input["topic"]
            }

            match = (
                (liked_df["caption"] == new_entry["caption"]) &
                (liked_df["mood"] == new_entry["mood"]) &
                (liked_df["type"] == new_entry["type"]) &
                (liked_df["topic"] == new_entry["topic"])
            )

            if isinstance(match, pd.Series) and match.any():
                liked_df.loc[match, "likes"] += 1
            else:
                new_entry["likes"] = 1
                liked_df = pd.concat([liked_df, pd.DataFrame([new_entry])], ignore_index=True)

            liked_df.to_csv(LIKED_FILE, index=False)
            st.success("💜 Saved to liked captions!")

# ------------------- Top Liked Captions -------------------
LIKED_FILE = "liked_captions.csv"
if os.path.exists(LIKED_FILE):
    liked_df = pd.read_csv(LIKED_FILE)
    filtered_likes = liked_df[
        (liked_df["mood"] == selected_mood) &
        (liked_df["type"] == caption_type)
    ]

    if not filtered_likes.empty:
        top_liked = filtered_likes.sort_values(by="likes", ascending=False).head(5)
        liked_options = [f"{i+1}. {row['caption']}  ❤️ ({row['likes']})"
                         for i, row in top_liked.reset_index().iterrows()]

        with st.expander("💜 Top Liked Captions (Filtered)", expanded=False):
            for caption in liked_options:
                st.markdown(f"- {caption}")
    else:
        st.info("No liked captions yet for this mood and caption type.")

# ------------------- Caption History -------------------
if st.session_state.history:
    st.markdown("---")
    st.markdown("### 🕘 Last 5 Captions")
    for i, cap in enumerate(st.session_state.history, 1):
        st.markdown(f"**{i}.** {cap}")

# ------------------- Feedback Button -------------------
st.markdown("---")
st.markdown("### 💡 Have Ideas to Make This Better?")
st.markdown(
    '<a href="https://forms.gle/n4VB5aTm87XNkuYFA" target="_blank">'
    '<button style="background-color:#4CAF50; color:white; padding:10px 20px; '
    'border:none; border-radius:8px; font-size:16px;">🚀 Help Us Improve</button>'
    '</a>',
    unsafe_allow_html=True
)
