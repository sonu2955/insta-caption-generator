import streamlit as st
from main import generate_caption

st.set_page_config(page_title="Insta Caption Generator", page_icon="📸")

st.title("📸 Insta Caption Generator")
st.write("Create cool captions instantly based on your mood and topic!")

# Mood selection
mood = st.selectbox("Select your mood", ["Happy", "Sad"])

# Topic selection
if mood == "Happy":
    topic = st.selectbox("Choose a topic", ["Travel", "Food"])
elif mood == "Sad":
    topic = st.selectbox("Choose a topic", ["Life", "Love"])
else:
    topic = None

# Generate button
if st.button("Generate Caption"):
    if mood and topic:
        caption = generate_caption(mood, topic)
        st.success(caption)
    else:
        st.warning("Please select both mood and topic.")
