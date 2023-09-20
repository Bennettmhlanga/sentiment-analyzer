import streamlit as st
import pandas as pd
import nltk
import base64
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download NLTK's VADER lexicon
nltk.download('vader_lexicon')

# Load the sentiment intensity analyzer
sid = SentimentIntensityAnalyzer()

# Set page configuration
st.set_page_config(page_title="Sentiment Analyzer", layout="wide")

# Define the form inputs
st.title("Sentiment Analyzer")

# Function for single sentence sentiment analysis
def analyze_single_sentence():
    st.subheader("Enter a sentence:")
    user_input = st.text_input("")
    
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

# Function for CSV sentiment analysis
def analyze_csv_sentiments():
    st.subheader("Upload a CSV file:")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if st.button("Analyze"):
        if uploaded_file is not None:
            # Read the CSV file
            df = pd.read_csv(uploaded_file)

            # Perform sentiment analysis on each text in the CSV file
            sentiments = []
            for text in df['text']:
                score = sid.polarity_scores(text)["compound"]
                if score > 0:
                    sentiment = "positive"
                elif score == 0:
                    sentiment = "neutral"
                else:
                    sentiment = "negative"
                sentiments.append(sentiment)

            # Create a new DataFrame with text and sentiment columns
            result_df = pd.DataFrame({'text': df['text'], 'sentiment': sentiments})

            # Display the processed data
            st.subheader("Processed Data:")
            st.dataframe(result_df)

            # Download link for the processed data
            st.markdown(get_download_link(result_df), unsafe_allow_html=True)

        else:
            st.warning("Please upload a CSV file.")

# Function to generate a download link for a DataFrame as a CSV file
def get_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Encode to base64
    href = f'<a href="data:file/csv;base64,{b64}" download="sentiment_results.csv">Download CSV</a>'
    return href

# Render the appropriate analysis based on user selection
analysis_option = st.selectbox("Select Analysis Option", ("Single Sentence", "CSV Sentiments"))

if analysis_option == "Single Sentence":
    analyze_single_sentence()
elif analysis_option == "CSV Sentiments":
    analyze_csv_sentiments()
