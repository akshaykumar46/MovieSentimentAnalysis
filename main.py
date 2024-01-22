from string import punctuation
import nltk
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords
import re 
from flask import Flask
import os
from os.path import dirname, join, realpath
import joblib
import uvicorn
from fastapi import FastAPI

from flask import Flask, jsonify, request

app = FastAPI(
    title="Sentiment model API",
    description="test API to predict movie review sentiment",
    version="0.1",
)

with open(join(dirname(realpath(__file__)), "models/sentiment_model_pipeline.pkl"), "rb") as f:
    model = joblib.load(f)

def text_cleaning(text, remove_stop_words=True):
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"http\S+", " link ", text)
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)  # remove numbers

    text = "".join([c for c in text if c not in punctuation])

    if remove_stop_words:

        stop_words = stopwords.words("english")
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)


    return text


@app.get("/predict-review")
def predict_sentiment(review: str):

    cleaned_review = text_cleaning(review)
    prediction = model.predict([cleaned_review])
    output = int(prediction[0])
    probas = model.predict_proba([cleaned_review])
    output_probability = "{:.2f}".format(float(probas[:, output]))

    sentiments = {0: "Negative", 1: "Positive"}

    result = {"prediction": sentiments[output], "Probability": output_probability}
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)