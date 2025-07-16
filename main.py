import random

def generate_caption(mood, topic):
    captions = {
        "happy": {
            "travel": [
                "Wander often, wonder always 🌍✨",
                "Collecting moments, not things 🚀",
                "Smiles and sunsets everywhere I go 🌅😊"
            ],
            "food": [
                "Happiness is homemade 🍝❤️",
                "You can’t live a full life on an empty stomach 🍔😁",
                "Sweet treats & sweeter memories 🍩✨"
            ],
        },
        "sad": {
            "life": [
                "Some days are just hard... and that’s okay 😔",
                "Not every day has a happy ending 📉",
                "Rainy minds, cloudy hearts 🌧️🖤"
            ],
            "love": [
                "Missing you in every heartbeat 💔",
                "Love faded, memories stayed 🕊️",
                "Echoes of what we were 💭💘"
            ],
        },
    }

    mood = mood.lower()
    topic = topic.lower()

    if mood in captions and topic in captions[mood]:
        return random.choice(captions[mood][topic])
    else:
        return "No caption found for that combination. Try another!"

# Optional for testing
if __name__ == "__main__":
    print(generate_caption("happy", "travel"))
