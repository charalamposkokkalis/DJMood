# This file asks the user some personal questions to determine his emotions

def talk_to_user():
    # Add more meaningful Qs, actual chatbot to make it like a conversation
    questions = ["How are you feeling today? ", "What have you been up to? ", "What are you doing next? ", "What are your top 3 favorite music genres? "]

    # Abstraction of chatbot
    user_answers = []

    for q in range(0,len(questions)):
        user_reply = input(questions[q]+ ' ')
        user_answers.append(user_reply)

    return user_answers