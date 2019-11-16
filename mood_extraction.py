# TODO
# This file will conduct sentiment analysis to the user's responses in order to find his mood.
# Should return vector of emotions

from chatbot import talk_to_user

mood_related_response = " ".join(talk_to_user()[0:3])

print(mood_related_response)