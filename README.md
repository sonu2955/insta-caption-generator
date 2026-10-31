# My_Caption ✍️

**An AI-powered social media caption generator that helps turn your thoughts and post ideas into engaging captions.**

My_Caption is a web application built with Python, Streamlit, and the OpenAI API. It allows users to generate social media captions based on their preferred mood and caption style, making content creation easier and more personalized.

The idea behind this project was simple: coming up with captions that match the mood and context of a social media post can be frustrating. I wanted to experiment with AI and build a simple tool that could make this process easier.

## ✨ Features

- **AI-Powered Caption Generation:** Generate captions using the OpenAI API.
- **Mood Selection:** Choose a mood to influence the tone of the generated caption.
- **Multiple Caption Styles:** Select different caption types depending on your content.
- **Liked Captions:** Save captions you like for future reference.
- **Caption History:** Store liked captions in a CSV file.
- **Filtered Favorites:** Find previously liked captions based on mood and caption type.
- **Dynamic Interface:** Rotating descriptions to make the application experience more engaging.
- **User Feedback:** Integrated Google Forms to collect user feedback and suggestions.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend / UI:** Streamlit
- **AI Integration:** OpenAI API
- **Data Storage:** CSV
- **Version Control:** Git and GitHub
- **Deployment:** Streamlit Community Cloud

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- OpenAI API key
- Git

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/my-caption-ai.git
cd my-caption-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Create a `.streamlit/secrets.toml` file:

```toml
OPENAI_API_KEY = "your_openai_api_key"
```

Never commit your API key or secrets file to GitHub.

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📂 Project Structure

```text
my-caption-ai/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── .streamlit/
│   └── secrets.toml
│
└── liked_captions.csv
```

*The structure above represents the intended repository organization. Your actual files may vary.*

## 💡 What I Learned

Building My_Caption helped me explore several practical aspects of application development:

- Integrating an AI model through an external API.
- Working with API requests and responses.
- Building interactive applications using Streamlit.
- Managing user preferences and application state.
- Saving and retrieving structured data using CSV files.
- Considering API token consumption and usage costs.
- Deploying a Python application using Streamlit Community Cloud.
- Improving an application based on user feedback.

## 🔮 Future Improvements

Some ideas I would like to explore:

- Support for additional social media platforms.
- More customization options for generated captions.
- Improved caption history and management.
- Better control over AI generation costs.
- Additional personalization based on user preferences.

## 🎯 Project Motivation

This project started as an experiment to understand how AI APIs could be used to solve everyday problems.

Rather than simply learning how to make API calls, I wanted to turn that knowledge into a working application that someone could actually use.

My_Caption represents one of my early steps into building AI-powered products and exploring the possibilities of AI-assisted application development.

---

**Built with curiosity, Python, and a little help from AI.** 🚀
