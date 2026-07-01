# Basic Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! How can I help you today?"

    elif user_input == "hi":
        return "Hello! Nice to meet you."

    elif user_input == "how are you":
        return "I'm fine, thanks for asking!"

    elif user_input == "what is your name":
        return "I am CodeAlpha ChatBot."

    elif user_input == "who created you":
        return "I was created using Python."

    elif user_input == "bye":
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that."

print("===== BASIC CHATBOT =====")
print("Type 'bye' to exit.\n")

while True:
    user_message = input("You: ")

    response = chatbot_response(user_message)

    print("Bot:", response)

    if user_message.lower() == "bye":
        break