import streamlit as st
from transformers import pipeline
import random  # For random message selection

# Load lighter 3-class sentiment model (~440MB, optimized for neutral factuals)
@st.cache_resource  # Caches to load once per session
def load_model():
    return pipeline(
        "sentiment-analysis", 
        model="finiteautomata/bertweet-base-sentiment-analysis"
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
    sentiment = result['label']  # Clean: 'POS', 'NEU', or 'NEG'

    # Map to display-friendly
    if sentiment == 'POS':
        sentiment_display = 'Positive'
    elif sentiment == 'NEU':
        sentiment_display = 'Neutral'
    else:  # 'NEG'
        sentiment_display = 'Negative'

    # Display results
    st.subheader("Results:")
    st.write(f"**Sentiment:** {sentiment_display}")
    
    # Pick & display random message with color-code
    if sentiment == 'POS':
        msg = random.choice(positive_messages)
        st.success(msg)
    elif sentiment == 'NEU':
        msg = random.choice(neutral_messages)
        st.warning(msg)
    else:  # 'NEG'
        msg = random.choice(negative_messages)
        st.error(msg)

# Sidebar for info
with st.sidebar:
    st.header("About")
    st.write("**What it does:** Analyzes short text (like reviews or tweets) and classifies it as Positive, Neutral, or Negative sentiment. Tuned for low-resource deploys and neutral factuals!")
    st.write("**Tech:** Built with Streamlit for the UI and Hugging Face's BERTweet-base model (trained on SemEval tweets for balanced 3-class).")
    st.write("**GitHub:** https://github.com/Aayudesh-k/sentiment-analyzer-app")