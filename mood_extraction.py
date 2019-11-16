# TODO
# This file will conduct sentiment analysis to the user's responses in order to find his mood.
# Should return vector of emotions

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# local imports
from chatbot import talk_to_user

# other imports
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'OxHack19-26166b4bf395.json'

mood_related_response = " ".join(talk_to_user()[0:3])

def sentiment_analysis(text):

    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    text = mood_related_response
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    return [sentiment.score, sentiment.magnitude]

# print('Text: {}'.format(text))
# print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
