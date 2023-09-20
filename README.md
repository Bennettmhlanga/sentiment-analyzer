# sentiment-analyzer
**Abstract Documentation**: Sentiment Analyzer App

# Overview:
The Sentiment Analyzer app is a user-friendly web application developed using Streamlit and NLTK's VADER lexicon. Its primary purpose is to analyze the sentiment of a given sentence and provide a sentiment label indicating whether the sentence is positive, neutral, or negative. The app has been enhanced with new features to further improve its functionality and usability.

# Functionality:

# Input: 
The user enters a sentence into the text input field provided by the app.
**Sentiment Analysis**: When the user clicks the "Analyze" button, the app performs sentiment analysis on the entered sentence.
**Sentiment Label**: Based on the sentiment analysis results, the app determines the sentiment label of the sentence (positive, neutral, or negative).
**Result Display**: The sentiment label is displayed on the app interface, indicating the sentiment of the input sentence.
# New Features:

**Sentiment Score**: In addition to the sentiment label, the app now provides a sentiment score that represents the intensity of the sentiment in the input sentence. The score ranges from -1 (highly negative) to +1 (highly positive), with 0 indicating a neutral sentiment. This allows users to gain more insights into the sentiment intensity.
**Multi-Sentence Analysis**: The app has been enhanced to support the analysis of multiple sentences at once. Users can now enter multiple sentences separated by line breaks or commas and analyze their sentiments collectively. The app provides sentiment labels and scores for each sentence, as well as an overall sentiment label and score for the entire input.
**Visualization**: The app now offers visualizations to help users better understand the sentiment distribution of their input. A bar chart is displayed, showing the number of positive, neutral, and negative sentences in the input. This allows users to quickly grasp the overall sentiment composition.
**Enhanced Language Support**: While the app is primarily trained on English language data, it has been improved to provide basic sentiment analysis for other commonly spoken languages. Although the accuracy may vary for non-English languages, users can now analyze sentiments in texts written in languages such as Spanish, French, German, and more.
# App Usage Recommendations:

**Text Length**: The Sentiment Analyzer app works best with shorter texts, such as sentences or short phrases. It is specifically designed for analyzing sentiments expressed in social media or informal texts.
**Informal Language**: The app is optimized for analyzing sentiment in texts that contain informal language, slang, and emoticons typically found in social media platforms.
**Real-Time Analysis**: The app provides instant sentiment analysis as the user interacts with it. It is suitable for quick sentiment checks or exploratory analysis.
# Deployment:
To deploy the Sentiment Analyzer app with the new features, the following dependencies should be considered:

**Streamlit library**: Required for creating the web application interface.
**NLTK library**: Necessary for accessing the VADER lexicon and performing sentiment analysis.
The app can be deployed on platforms such as Streamlit Cloud, Heroku, or any other hosting service that supports Streamlit applications. Remember to include a requirements.txt file listing the required libraries (in this case, streamlit and nltk) for smooth deployment.
