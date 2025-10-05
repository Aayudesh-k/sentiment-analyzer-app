import streamlit as st
from transformers import pipeline
import random  # For random message selection

# Load the pre-trained 3-class sentiment model (downloads ~1.4GB first run—runs once)
@st.cache_resource  # Caches the model to avoid reloading
def load_model():
    return pipeline(
        "sentiment-analysis", 
        model="j-hartmann/sentiment-roberta-large-english-3-classes"
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
    st.write("**What it does:** Analyzes short text (like reviews or tweets) and classifies it as Positive, Neutral, or Negative sentiment. Tuned for better neutral detection on factual sentences!")
    st.write("**Tech:** Built with Streamlit for the UI and Hugging Face's RoBERTa-large model (fine-tuned on English reviews).")
    st.write("**GitHub:** [link to repo]")  # Update later