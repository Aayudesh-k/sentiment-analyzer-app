import streamlit as st
from transformers import pipeline
import random  # For random message selection

# Load lighter 3-class sentiment model (~500MB, low RAM)
@st.cache_resource  # Caches to load once per session
def load_model():
    return pipeline(
        "sentiment-analysis", 
        model="cardiffnlp/twitter-roberta-base-sentiment",
        tokenizer="cardiffnlp/twitter-roberta-base-sentiment"
    )

# Random messages for variety
positive_messages = [
    "Positive vibes! 🎉",
    "Yay, sunshine ahead! ☀️",
    "High five—that rocks! ✋",
    "Sweet success! 🍭"
]
neutral_messages = [
    "Neutral take—meh. 🤷",
    "Straight facts—no drama. 📝",
    "Boring but balanced. 😐",
    "Middle ground detected. ⚖️"
]
negative_messages = [
    "Negative feels... 😔",
    "Oof, tough break... 💔",
    "Bummer city. 😞",
    "Rough patch ahead. 🌧️"
]

st.title("AI Sentiment Analyzer")
st.write("Paste text below to get instant sentiment analysis (positive, negative, or neutral).")

# User input
user_input = st.text_area("Enter text:", height=150, placeholder="E.g., 'This weather is terrible!'")

if st.button("Analyze Sentiment") and user_input:
    model = load_model()
    result = model(user_input)[0]  # Get the top prediction
    sentiment_lower = result['label']  # Lowercase: 'positive', 'neutral', or 'negative'

    # Capitalize for display
    sentiment_display = sentiment_lower.capitalize()

    # Display results
    st.subheader("Results:")
    st.write(f"**Sentiment:** {sentiment_display}")
    
    # Pick & display random message with color-code (check lowercase)
    if sentiment_lower == 'positive':
        msg = random.choice(positive_messages)
        st.success(msg)
    elif sentiment_lower == 'neutral':
        msg = random.choice(neutral_messages)
        st.warning(msg)
    else:  # 'negative'
        msg = random.choice(negative_messages)
        st.error(msg)

# Sidebar for info
with st.sidebar:
    st.header("About")
    st.write("**What it does:** Analyzes short text (like reviews or tweets) and classifies it as Positive, Neutral, or Negative sentiment. Tuned for low-resource deploys!")
    st.write("**Tech:** Built with Streamlit for the UI and Hugging Face's RoBERTa-base model (trained on 124M+ tweets).")
    st.write("**GitHub:** https://github.com/Aayudesh-k/sentiment-analyzer-app")