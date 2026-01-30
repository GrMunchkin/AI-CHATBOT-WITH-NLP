# Simple Retrieval-Based Chatbot using TF-IDF and Cosine Similarity
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Downloads tokenizers
nltk.download('punkt')

# Organized responses by keywords
responses_dict = {
    "what is ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "ai": "AI enables machines to perform tasks that typically require human intelligence.",
    "artificial intelligence": "AI is widely used in healthcare, finance, and education.",
    "what is nlp": "Natural Language Processing enables computers to understand human language.",
    "nlp": "NLP is a subfield of artificial intelligence.",
    "natural language processing": "NLP deals with text and speech data.",
    "what is python": "Python is a popular programming language.",
    "python": "Python is widely used in AI and data science.",
    "what is chatbot": "Chatbots simulate human conversation.",
    "chatbot": "Chatbots are commonly used in customer support.",
    "chatbots": "Retrieval-based chatbots select responses from stored data.",
    "machine learning": "Machine learning allows systems to learn from data.",
    "tokenization": "Tokenization is the process of splitting text into smaller units.",
    "tfidf": "TF-IDF is a technique used to convert text into numerical form.",
}

# Flatten to lists
responses_keys = list(responses_dict.keys())
responses_values = list(responses_dict.values())

# Text preprocessing
def preprocess(text):
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))

processed_responses = [preprocess(r) for r in responses_values]

def chatbot(user_input):
    user_input_processed = preprocess(user_input)
    
    # First, try exact keyword matching
    for key, response in responses_dict.items():
        if key in user_input_processed:
            print(f"[Debug] Matched keyword: {key}")
            return response
    
    # If no exact match, use TF-IDF
    corpus = processed_responses + [user_input_processed]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(corpus)
    similarity = cosine_similarity(tfidf[-1], tfidf[:-1])
    best_match = similarity.argsort()[0][-1]
    similarity_score = similarity[0][best_match]
    print(f"[Debug] TF-IDF match: {responses_keys[best_match]}, Similarity: {similarity_score:.4f}")
    
    if similarity_score < 0.1:
        return "Sorry, I don't have information on that topic. Try asking about AI, NLP, Python, or chatbots."
    else:
        return responses_values[best_match]

print("Hello! I'm a chatbot. How can I assist you today? (Type 'exit' to quit.)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot(user_input)
    print("Chatbot:", response)
