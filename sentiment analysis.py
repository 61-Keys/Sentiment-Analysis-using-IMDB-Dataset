# -*- coding: utf-8 -*-
"""Sentiment Analysis using IMDB Dataset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jgj1byh7LoFrp_Fw9_KjkjnexdCb2J53
"""

import nltk
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')

import random
import requests
from nltk.corpus import movie_reviews, stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import ipywidgets as widgets
from IPython.display import display, HTML

# Load movie reviews dataset from nltk
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle the documents to get a balanced distribution of classes in training and testing data
random.shuffle(documents)

# Define a function to preprocess the movie reviews
def preprocess_movie_review(review_text):
    # Lowercase the text
    review_text = review_text.lower()
    # Tokenize the text
    words = word_tokenize(review_text)
    # Remove stopwords and non-alphanumeric characters
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return ' '.join(words)

# Preprocess the movie reviews and split into features and labels
reviews = [(preprocess_movie_review(' '.join(words)), label) for words, label in documents]
features, sentiments = zip(*reviews)

# Convert sentiments to binary classes (positive or negative sentiment)
sentiments = ['positive' if sentiment == 'pos' else 'negative' for sentiment in sentiments]

# Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(features)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_train_vectorized, sentiments, test_size=0.2, random_state=42)

# Train a Logistic Regression classifier
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Calculate and display the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# OMDB API Function to Fetch IMDb Rating
def fetch_imdb_rating(movie_name):
    api_key = 'ac178886'
    base_url = 'http://www.omdbapi.com/'

    params = {
        'apikey': api_key,
        't': movie_name
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'imdbRating' in data:
        imdb_rating = data['imdbRating']
        return float(imdb_rating)

    return None

# Function to get sentiment emoji based on sentiment
def get_sentiment_emoji(sentiment):
    if sentiment == 'positive':
        return '😃'
    elif sentiment == 'negative':
        return '😞'
    else:
        return '😐'

def predict_sentiment(movie_name):
    movie_review = preprocess_movie_review(movie_name)
    review_vectorized = vectorizer.transform([movie_review])
    sentiment = classifier.predict(review_vectorized)[0]
    return sentiment

# Create a Text widget for input movie name
movie_input = widgets.Text(placeholder="Enter a movie name", description="Movie Name:")

# Create a Button widget
button = widgets.Button(description="Predict Sentiment")

# Create a progress bar (speedometer-like representation) using custom CSS styling
progress_bar = widgets.FloatProgress(
    value=0.5,  # Initial value (50%)
    min=0,
    max=1.0,
    description='Sentiment:',
    bar_style='info',
    orientation='horizontal',
    style={'bar_color': '#0074D9', 'description_width': 'initial', 'border': '2px solid #d3d3d3'}
)

# Define a function to update the progress bar (speedometer)
def update_sentiment_meter(sentiment):
    sentiment_score = 1.0 if sentiment == 'positive' else 0.0
    progress_bar.value = sentiment_score

# Define a function to handle button click event
def on_button_click(b):
    movie_name = movie_input.value
    sentiment = predict_sentiment(movie_name)
    update_sentiment_meter(sentiment)
    emoji = get_sentiment_emoji(sentiment)
    imdb_rating = fetch_imdb_rating(movie_name)
    print(f"{emoji} The sentiment for '{movie_name}' is {sentiment}.")
    if imdb_rating is not None:
        print(f"IMDb Rating: {imdb_rating}/10")

# Attach the button click event to the button
button.on_click(on_button_click)

# Display the widgets and the speedometer-like representation
display(widgets.VBox([movie_input, button, progress_bar]))