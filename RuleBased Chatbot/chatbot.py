import datetime
import random

# ============================================
# RULE-BASED AI CHATBOT
# Developed by: Cheran
# Internship Project - DecodeLabs
# ============================================


# Bot Responses Database
responses = {

    "hello": [
        "Hello! Nice to meet you.",
        "Hi there!",
        "Hey! How can I help you?"
    ],

    "hi": [
        "Hi!",
        "Hello!",
        "Greetings!"
    ],

    "how are you": [
        "I'm functioning perfectly!",
        "Doing great. Thanks for asking!",
        "All systems operational!"
    ],

    "your name": [
        "I'm DecodeLabs AI Assistant.",
        "You can call me AI Bot."
    ],

    "who created you": [
        "I was created by Cheran during his AI internship project."
    ],

    "college": [
        "Oxford College of Engineering."
    ],

    "course": [
        "Artificial Intelligence and Machine Learning."
    ],

    "time": [
        f"Current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    ],

    "date": [
        f"Today's date is {datetime.date.today()}"
    ],

    "help": [
        "You can ask me basic questions like time, date, greetings, and more."
    ],

    "bye": [
        "Goodbye! Have an amazing day.",
        "See you later!",
        "Exiting chatbot..."
    ]
}


# ============================================
# Function to display chatbot header
# ============================================

def show_header():

    print("\n" + "=" * 50)
    print("        RULE-BASED AI CHATBOT")
    print("=" * 50)

    print("Internship Project")
    print("Developer : Cheran")
    print("Organization : DecodeLabs")

    print("=" * 50)
    print("Type 'bye' to exit the chatbot.")
    print("=" * 50 + "\n")


# ============================================
# Function to sanitize user input
# ============================================

def clean_text(text):

    return text.lower().strip()


# ============================================
# Function to generate bot response
# ============================================

def get_response(user_message):

    cleaned_message = clean_text(user_message)

    if cleaned_message in responses:

        return random.choice(responses[cleaned_message])

    else:

        fallback_responses = [

            "Sorry, I don't understand that.",
            "Can you rephrase your question?",
            "I'm still learning. Try asking something else.",
            "That command is not in my knowledge base."
        ]

        return random.choice(fallback_responses)


# ============================================
# Main chatbot function
# ============================================

def run_chatbot():

    show_header()

    while True:

        user_input = input("You : ")

        cleaned_input = clean_text(user_input)

        if cleaned_input == "bye":

            print("Bot :", random.choice(responses["bye"]))
            break

        bot_reply = get_response(user_input)

        print("Bot :", bot_reply)


# ============================================
# Program Entry Point
# ============================================

if __name__ == "__main__":

    run_chatbot()