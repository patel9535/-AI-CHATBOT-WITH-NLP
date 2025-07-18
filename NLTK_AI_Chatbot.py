import nltk
from nltk.chat.util import Chat, reflections
import re
import random

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Define intents with patterns and responses
intents = {
    "greeting": {
        "patterns": [
            "hello", "hi", "hey", "good morning", "good evening", "how are you"
        ],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! How may I assist you?",
            "I'm good! Tell me how I can help you?"
        ]
    },
    "goodbye": {
        "patterns": [
            "bye", "see you later", "goodbye", "have a nice day", "catch you later"
        ],
        "responses": [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! Feel free to chat anytime."
        ]
    },
    "thanks": {
        "patterns": [
            "thanks", "thank you", "that's helpful", "thanks a lot"
        ],
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "Anytime! Let me know if you have more questions."
        ]
    },
    "name_query": {
        "patterns": [
            "what is your name", "who are you", "identify yourself", "your name"
        ],
        "responses": [
            "I am an NLP Chatbot developed to assist you.",
            "You can call me Chatbot.",
            "I'm your friendly chatbot here to help."
        ]
    },
    "weather_query": {
        "patterns": [
            "what's the weather", "tell me the weather", "weather forecast", "how's the weather"
        ],
        "responses": [
            "I'm sorry, I don't have weather data yet.",
            "I can't provide weather updates currently.",
            "Try checking a weather website for that."
        ]
    },
    "general_knowledge": {
        "patterns": [
            "what is the capital of france", "what is the largest ocean"
        ],
        "responses": [
            "The capital of France is Paris.",
            "The Pacific Ocean is the largest ocean on Earth."
        ]
    },
    "joke": {
        "patterns": [
            "tell me a joke", "make me laugh", "tell me something funny"
        ],
        "responses": [
            "Why don't skeletons fight each other? They don't have the guts!",
            "What do you call fake spaghetti? An impasta!",
            "Why do seagulls fly over the sea? If they flew over the bay, they would be bagels." ,
            "Why did the computer go to the doctor? Because it had a virus!"
        ]
    }
}

# Default responses for unmatched inputs
default_responses = [
    "I am sorry, I don't understand. Could you please rephrase?",
    "I'm not sure I understand. Can you ask differently?",
    "Apologies, I didn't get that. Could you clarify?"
]

# Preprocess user input
def preprocess_input(user_input):
    # Convert to lowercase
    user_input = user_input.lower()
    # Remove punctuation
    user_input = re.sub(r'[^\w\s]', '', user_input)
    return user_input

# Create pattern-response pairs for NLTK Chat
pairs = []
for intent in intents.values():
    for pattern in intent["patterns"]:
        # Match whole input (add anchors)
        pattern_regex = rf".*\b{pattern}\b.*"
        pairs.append((pattern_regex, intent["responses"]))

# Initialize the chatbot
chat = Chat(pairs, reflections)

# Start the chatbot
def start_chat():
    print("Hi! I'm your friendly chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            break
        # Preprocess user input
        user_input = preprocess_input(user_input)
        # Check for matching pattern
        response = None
        for pattern, responses in pairs:
            if re.match(pattern, user_input):
                response = random.choice(responses)
                break
        if response:
            print(response)
        else:
            print(random.choice(default_responses))

if __name__ == "__main__":
    start_chat()