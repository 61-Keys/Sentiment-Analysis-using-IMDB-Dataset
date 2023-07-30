# Sentiment-Analysis-using-IMDB-Dataset





This project is an implementation of sentiment analysis on movie reviews using machine learning techniques. The goal of this project is to predict whether a movie review is positive or negative based on its text. The project uses the Movie Reviews dataset from the NLTK library, and the model is trained using logistic regression.

## Table of Contents

- [Introduction](#introduction)
- [Data Preprocessing](#data-preprocessing)
- [Feature Extraction](#feature-extraction)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Introduction

Sentiment analysis, also known as opinion mining, is a natural language processing (NLP) technique used to determine the sentiment expressed in a piece of text. In this project, we apply sentiment analysis to movie reviews to classify them as positive or negative.

## Data Preprocessing

The movie reviews dataset is loaded from the NLTK library. The text data is preprocessed by converting it to lowercase, tokenizing the words, and removing stopwords and non-alphanumeric characters.

## Feature Extraction

The text data is vectorized using the TF-IDF (Term Frequency-Inverse Document Frequency) technique. TF-IDF assigns a weight to each word in the document based on its frequency in the document and its rarity across all documents.

## Model Training

We train a logistic regression classifier on the vectorized text data to predict the sentiment of movie reviews.

## Evaluation

The model's performance is evaluated using accuracy, which measures the proportion of correctly classified movie reviews in the test set.

## Usage

To use the sentiment analysis model, follow these steps:

1. Input a movie name in the provided text box.
2. Click the "Predict Sentiment" button.
3. The model will predict whether the movie review is positive or negative.
4. The sentiment will be displayed using an emoji and a bar-like representation.
5. If available, the IMDb rating of the movie will be shown.

## Instructions : 

Future updates : 

• To be able to create a user-friendly deployable website. 
• More accurate sentiment analysis using powerful models like BERT.



## Dependencies

The following libraries are required to run the code:

- nltk
- scikit-learn
- pandas
- requests
- ipywidgets

Install the dependencies using the following command:

```bash
pip install nltk scikit-learn pandas requests ipywidgets

