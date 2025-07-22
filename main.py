import random

def generate_caption(mood, topic):
    captions = {
        "😊 happy": {
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
            "friends": [
                "Good times + Crazy friends = Amazing memories 🥳",
                "Surround yourself with people who lift you higher 👯‍♂️",
                "Friendship is the golden thread of life 💛"
            ]
        },
        "😢 sad": {
            "life": [
                "Some days are just hard... and that’s okay 😔",
                "Not every day has a happy ending 📉",
                "Rainy minds, cloudy hearts 🌧️🖤"
            ],
            "alone": [
                "Sometimes being alone is better than being around fake people 🌑",
                "Silence is my loudest cry 🤐",
                "Alone but not lonely 💭"
            ],
            "breakup": [
                "Letting go is the hardest part 💔",
                "From strangers to lovers to strangers again 💔",
                "Tears speak when words can't 💧"
            ]
        },
        "✈️ travel": {
            "mountains": [
                "Climbing to new heights 🏔️",
                "The best view comes after the hardest climb ⛰️",
                "Mountain air, don't care 😌"
            ],
            "beach": [
                "Sandy toes, sun-kissed nose 🏖️",
                "Ocean vibes and salty tides 🌊",
                "Beach more, worry less 🌞"
            ],
            "adventure": [
                "Life’s an adventure – go live it! 🧭",
                "Daring to go where others won’t 🚵‍♂️",
                "Find yourself in the unknown 🌌"
            ]
        },
        "❤️ love": {
            "romantic": [
                "You had me at hello 💘",
                "In your arms is my favorite place 💑",
                "Love written in the stars ✨"
            ],
            "self love": [
                "Loving myself more each day 💕",
                "I am enough. Always. 💖",
                "Self-love is the best love 🪞"
            ],
            "crush": [
                "Butterflies every time you text 💬🦋",
                "Thinking of you more than I should ☺️",
                "My heart skips a beat when I see you 💓"
            ]
        }
    }

    mood = mood.lower()
    topic = topic.lower()

    if mood in captions and topic in captions[mood]:
        return random.choice(captions[mood][topic])
    else:
        return "No caption found for that combination. Try another!"

# Optional test
if __name__ == "__main__":
    print(generate_caption("😊 Happy", "Travel"))
