import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK resources
nltk.download('punkt')

# Pairs is a list of patterns and responses
pairs = [
    [r'hi|hello|hey', ['Hello! How can I help you?']],
    [r'(.*) your name?', ['I am a chatbot created to assist you.']],
    [r'how are you?', ['I am doing well, thank you!']],
    [r'(.*) help (.*)', ['Sure, I can help you with that.']],
    [r'bye', ['Goodbye! Have a great day!']]
]

chatbot = Chat(pairs, reflections)

def get_response(user_input):
    return chatbot.respond(user_input)
