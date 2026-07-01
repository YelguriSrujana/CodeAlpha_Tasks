import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download('punkt', quiet=True)

# FAQ Questions
faq_questions = [
    "What is your name?",
    "How are you?",
    "What is AI?",
    "Who created you?",
    "What can you do?",
    "What is Python?",
    "What is machine learning?"
]

# FAQ Answers
faq_answers = [
    "I am CodeAlpha Chatbot.",
    "I am doing great!",
    "AI means Artificial Intelligence.",
    "I was created using Python.",
    "I can answer simple FAQ questions.",
    "Python is a popular programming language.",
    "Machine Learning is a branch of AI that enables computers to learn from data."
]

# Create TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Convert questions into vectors
faq_vectors = vectorizer.fit_transform(faq_questions)

# Function to generate chatbot response
def chatbot_response(user_input):
    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vector, faq_vectors)

    index = similarity.argmax()

    # Check confidence score
    if similarity[0][index] < 0.2:
        return "Sorry, I don't understand that question."

    return faq_answers[index]

# Chatbot Start
print("=" * 40)
print("      CodeAlpha FAQ Chatbot")
print("      Type 'exit' to quit")
print("=" * 40)

while True:
    query = input("\nYou: ")

    if query.lower() == "exit":
        print("Bot: Goodbye! Have a nice day.")
        break

    response = chatbot_response(query)
    print("Bot:", response)