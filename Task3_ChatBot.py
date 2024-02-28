import random

# Define a dictionary of ChatGPT-related questions and their answers
chatgpt_faqs = {
    "what is chatgpt?": "ChatGPT is a language model developed by OpenAI that is designed for natural language conversation. It can answer questions, generate text, and have interactive discussions with users.",
    "how does chatgpt work?": "ChatGPT is powered by a deep learning model called GPT (Generative Pre-trained Transformer). It's trained on a large corpus of text from the internet and uses that knowledge to generate human-like text based on input.",
    "what can i do with chatgpt?": "You can use ChatGPT for a variety of tasks, such as answering questions, generating text, creating content, providing recommendations, and much more.",
    "is chatgpt free to use?": "OpenAI offers both free and paid access to ChatGPT. There may be usage limitations on the free tier, and you can check OpenAI's pricing for more details.",
    "what is prompt engineering?": "Prompt engineering is the process of designing specific instructions or questions to obtain desired responses from a language model like ChatGPT. It involves crafting prompts to be clear and effective in conveying your intent.",
    "Is ChatGPT capable of understanding context?": "Yes, ChatGPT is designed to understand context to a certain extent. It considers the preceding conversation or prompt when generating responses, allowing it to maintain coherence and relevance in its replies.",
    "Can ChatGPT learn from interactions?": "ChatGPT does not learn or adapt in real-time from individual interactions. However, OpenAI periodically updates and refines its models based on feedback and new training data.",
    "What are the limitations of ChatGPT?": "While ChatGPT is capable of generating human-like responses, it may sometimes produce inaccurate or nonsensical replies, especially when prompted with ambiguous or complex queries. Additionally, it may lack real-world knowledge beyond its training data cutoff date.",
    "Is ChatGPT biased?": "ChatGPT aims to minimize biases in its responses, but it may inadvertently reflect biases present in its training data. OpenAI continuously works to mitigate biases and promote fairness and inclusivity in its models.",
    "Is ChatGPT intelligent?": "ChatGPT exhibits a form of artificial intelligence that allows it to generate contextually relevant responses based on the input it receives. However, it's important to note that ChatGPT's intelligence is different from human intelligence.",
    "How accurate is ChatGPT?": "ChatGPT strives to generate accurate and coherent responses, but it may occasionally produce nonsensical or incorrect replies, especially in ambiguous or complex situations.",
    "Is ChatGPT safe to use?": "ChatGPT is generally safe to use, but it's essential to remember that it's a machine learning model and may generate unexpected or inappropriate responses. Users should exercise caution and use discretion when interacting with ChatGPT.",

}


rules = {
    "hello": ["Hi there!", "Hello!", "How can I help you today?"],
    "how are you": ["I'm just a computer program, so I don't have feelings, but thanks for asking! How can I assist you?", "I'm here to help. What can I do for you?"],
    "bye": ["Goodbye!", "Have a great day!", "See you later!"],
    "what is your name": ["I am an AI developed by OpenAI called ChatGPT. You can call me Alex. How can I assist you today?"],
    "help me": ["You can ask me questions..."],
    "got it": ["Great!", "Understood!", "Excellent!"],
    "tell me more": ["Certainly, what specifically would you like to know?", "I'd be happy to provide more details. What are you interested in?"],
    "I agree": ["I'm glad we're on the same page!", "It's good to hear we agree!", "Great minds think alike!"],
    "I want information": ["Sure!","I am here to help you!","What information do you want to know?"],
    "tell me about prompt engineering": ["I get it!!!Prompt engineering is an approach that emphasizes rapid iteration, agility, and responsiveness to feedback in engineering processes. Unlike traditional approaches, which may involve lengthy planning and development cycles, prompt engineering aims to quickly prototype, test, and iterate on solutions to address challenges and opportunities."],
    
}

def chatbot_response(user_input):
    user_input_lower = user_input.lower().strip()
    
    if user_input_lower in chatgpt_faqs:
        return chatgpt_faqs[user_input_lower]
    elif user_input_lower in rules:
        return random.choice(rules[user_input_lower])
    else:
        return "I'm not sure I understand. Can you please rephrase your question or greeting?"

# Main chat loop
print("Chatbot: Hi! I'm your friendly chatbot. You can start a conversation with me or type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
