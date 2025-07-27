import streamlit as st
import random
import base64
import gspread
from google.oauth2.service_account import Credentials
from main import generate_caption, get_topic_example

# ------------------- Google Sheets Setup -------------------
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=SCOPE)
CLIENT = gspread.authorize(CREDS)
SHEET = CLIENT.open_by_url("https://docs.google.com/spreadsheets/d/1ULA7sKGUAnXYWIIY-CLxTNJAarzW4iAH2xs13iGiHtU/edit?usp=sharing")
WORKSHEET = SHEET.sheet1

def like_caption(caption_text, mood_val, type_val, topic_val):
    records = WORKSHEET.get_all_records()
    for idx, record in enumerate(records):
        if (record["caption"] == caption_text and record["mood"] == mood_val and
            record["type"] == type_val and record["topic"] == topic_val):
            WORKSHEET.update_cell(idx + 2, 5, record["likes"] + 1)  # Row + header, Column 5 = likes
            return
    WORKSHEET.append_row([caption_text, mood_val, type_val, topic_val, 1])

def get_top_liked_captions(mood_val, type_val):
    records = WORKSHEET.get_all_records()
    filtered = [rec for rec in records if rec["mood"] == mood_val and rec["type"] == type_val]
    sorted_filtered = sorted(filtered, key=lambda x: x["likes"], reverse=True)
    return sorted_filtered[:5]

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
caption_type_selected = st.selectbox("📝 Select Caption Type", ["Story", "Post", "Notes", "Reels", "Attitude & stylish"])

mood_emojis = {
    "Romantic": "💖", "Funny": "😂", "Adventure": "🗺️", "Motivational": "💪",
    "Friends": "👫", "Travel": "✈️", "Food": "🍕", "Fitness": "🏋️", "Fashion": "👗"
}
moods = list(mood_emojis.keys())
selected_mood = st.selectbox("🎭 Select Photo Mood", [f"{mood_emojis[m]} {m}" for m in moods])
selected_mood = selected_mood.split(" ", 1)[1]

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
            result_caption = generate_caption(caption_type_selected, selected_mood, topic_input)
            st.session_state.caption = result_caption
            st.session_state.last_input = {
                "mood": selected_mood,
                "type": caption_type_selected,
                "topic": topic_input
            }
            st.session_state.history.insert(0, result_caption)
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
        import streamlit.components.v1 as components

        copy_text = st.session_state.caption.replace("'", "\\'")
        components.html(
            f"""
            <button onclick="navigator.clipboard.writeText('{copy_text}')"
                style="
                    padding: 10px 20px;
                    font-size: 16px;
                    color: white;
                    background-color: #4CAF50;
                    border: none;
                    border-radius: 8px;
                    cursor: pointer;
                    transition: background-color 0.3s ease;
                "
                onmouseover="this.style.backgroundColor='#45a049'"
                onmouseout="this.style.backgroundColor='#4CAF50'"
            >
                📋 Copy Caption
            </button>
            """,
            height=60,
        )

    with col2:
        if st.button("👍 Like this caption", key="like_btn"):
            like_caption(
                st.session_state.caption,
                st.session_state.last_input["mood"],
                st.session_state.last_input["type"],
                st.session_state.last_input["topic"]
            )
            st.success("💜 Saved to liked captions!")

# ------------------- Top Liked Captions -------------------
top_liked = get_top_liked_captions(selected_mood, caption_type_selected)

if top_liked and isinstance(top_liked, list):
    with st.expander("💜 Top Liked Captions (Filtered)", expanded=False):
        for i, top_row in enumerate(top_liked):
            caption = top_row.get('caption', 'No caption')
            likes = top_row.get('likes', 0)
            st.markdown(f"{i+1}. {caption} ❤️ ({likes})")
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
