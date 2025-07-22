import streamlit as st
from main import generate_caption

st.set_page_config(page_title="Insta Caption Generator", page_icon="📸")

st.title("📸 Insta Caption Generator v2.0")
st.markdown("Generate 🔥 captions for your Instagram posts using AI")

mood = st.selectbox("Choose a mood", ["Happy", "Sad", "Romantic", "Funny", "Motivational", "Aesthetic"])
topic = st.text_input("Enter the topic of your post (e.g. coffee, travel, gym)")

if st.button("Generate Caption"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating..."):
            caption = generate_caption(mood, topic)
        st.success("Here's your caption:")
        st.markdown(f"**📝 {caption}**")
