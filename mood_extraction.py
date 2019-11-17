import paralleldots
from chatbot import talk_to_user

paralleldots.set_api_key("C4hoTyr6iYapNCizZ1QCvHs99NbJ3A0g4aaWRG50Uow")

def sentiment_analysis(text):
    return paralleldots.emotion(text)['emotion']
