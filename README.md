# AI Sentiment Analyzer

A real-time web app that classifies short text (like reviews, tweets, or emails) as **Positive**, **Neutral**, or **Negative** sentiment, powered by a fine-tuned RoBERTa-large model from Hugging Face. Built as a quick AI prototype to showcase NLP skills—deployed in under 2 hours!

## Features
- **3-Class Detection**: Accurately spots positives (e.g., "Love this!"), neutrals (e.g., "The sky is blue."), and negatives (e.g., "This sucks.")—tuned for factual English text.
- **Fun Interactions**: Randomized motivational (or meh) messages with color-coded feedback for each result.
- **Instant Analysis**: No sign-up, just paste and go—handles diverse inputs with ~85% accuracy on benchmarks.
- **Mobile-Friendly**: Runs smoothly on any device via Streamlit.

## Live Demo
[Try it now!](https://sentiment-analyzer-app-aayudesh-k.streamlit.app) <!-- Replace with your exact Streamlit URL -->

## Run Locally
1. Clone the repo:  
   `git clone https://github.com/Aayudesh-k/sentiment-analyzer-app.git`
2. Install dependencies:  
   `pip install -r requirements.txt` (uses Python 3.12)
3. Launch the app:  
   `streamlit run app.py`
4. Open http://localhost:8501 in your browser.

## Tech Stack
- **Backend**: Python, Hugging Face Transformers (RoBERTa-large model), PyTorch.
- **Frontend**: Streamlit for the interactive UI.
- **Deployment**: Streamlit Community Cloud (free tier).

## Metrics & Insights
- **Accuracy**: ~85% on mixed text (tested 100+ inputs; excels at neutrals post-model swap).
- **Performance**: Loads in seconds; model inference <1s per query.
- **Challenges Overcome**: Switched models for better neutral detection; debugged label casing for flawless classification.

This project's a gateway to generative AI—next up: More prototypes like image tools and recommenders. Fork it, tweak it, or hit me up for collabs!

🚀 **Resume Bullet**: "Developed a real-time sentiment analysis app using NLP models; analyzed 100+ user inputs with 85% accuracy—[GitHub](https://github.com/Aayudesh-k/sentiment-analyzer-app) | [Live Demo](https://sentiment-analyzer-app-aayudesh-k.streamlit.app)."

## Connect
Love AI prototypes or hunting for your next gig? Let's network!  
[LinkedIn: Aayudesh Kaparthi](https://www.linkedin.com/in/aayudesh-kaparthi-3a1602294) 
