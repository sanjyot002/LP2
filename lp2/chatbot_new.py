import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by OpenAI.",]
    ],
    [
        r"how are you ?",
        ["I'm good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry",]
    ],
    [
        r"quit",
        ["Bye-bye! Take care.", "Nice chatting with you!"]
    ]
]

def simple_chatbot():
    print("Hello! I am a simple chatbot. How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

simple_chatbot()
