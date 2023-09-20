import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download NLTK's VADER lexicon
nltk.download('vader_lexicon')

# Load the sentiment intensity analyzer
sid = SentimentIntensityAnalyzer()

# Set page configuration
st.set_page_config(page_title="Sentiment Analyzer", layout="wide")

# Define the form inputs
st.title("Sentiment Analyzer")
st.subheader("Enter a sentence:")
user_input = st.text_input("")

# Perform sentiment analysis when user clicks the "Analyze" button
if st.button("Analyze"):
    if user_input:
        # Analyze sentiment
        score = sid.polarity_scores(user_input)["compound"]

        # Determine the sentiment label
        if score > 0:
            label = "This sentence is positive"
        elif score == 0:
            label = "This sentence is neutral"
        else:
            label = "This sentence is negative"

        # Display the sentiment analysis result
        st.subheader("Sentiment Analysis Result:")
        st.write(label)
    else:
        st.warning("Please enter a sentence.")