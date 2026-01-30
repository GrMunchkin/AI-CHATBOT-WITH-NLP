# AI-CHATBOT-WITH-NLP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: Fardin Islam

*INTERN ID*: CTIS3236

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*: This Python program implements a simple retrieval-based chatbot using basic Natural Language Processing (NLP) techniques, specifically TF-IDF vectorization and cosine similarity. The chatbot is designed to respond to user queries by selecting the most relevant answer from a predefined set of responses rather than generating new text. This approach makes the chatbot efficient, predictable, and suitable for introductory NLP applications.

The program begins by importing several important libraries. The nltk library is used for basic NLP tasks, while string helps with text preprocessing by removing punctuation. From the scikit-learn library, TfidfVectorizer is imported to convert text into numerical vectors, and cosine_similarity is used to measure similarity between text vectors. These tools are commonly used in text-based machine learning and information retrieval systems.

The program downloads the NLTK tokenizer data using nltk.download('punkt'). Although advanced tokenization is not explicitly used later in the code, this step ensures that the required NLP resources are available and demonstrates standard setup practices when working with NLTK.

A dictionary called responses_dict is then defined to store chatbot knowledge. This dictionary maps keywords or phrases to corresponding responses. The responses cover basic topics such as artificial intelligence, natural language processing, Python, chatbots, machine learning, tokenization, and TF-IDF. This structure allows the chatbot to retrieve answers based on user input content rather than fixed command formats.

To simplify further processing, the keys and values of the dictionary are separated into two lists: one for keywords and one for responses. This separation is useful when applying vectorization and similarity comparison, as it allows easier indexing and retrieval of the most relevant response.

The program defines a preprocess function to normalize text input. This function converts text to lowercase and removes punctuation marks. Text preprocessing is a critical step in NLP because it reduces variability in input text and improves matching accuracy. For example, it ensures that “AI”, “ai”, and “AI?” are treated as the same input.

All chatbot responses are preprocessed in advance and stored in a list called processed_responses. This avoids repeated preprocessing during runtime and improves efficiency when handling user queries.

The core chatbot logic is implemented in the chatbot function. When a user enters a query, the input is first preprocessed using the same function applied to stored responses. The chatbot then attempts exact keyword matching by checking whether any predefined keyword exists within the user’s input. If a match is found, the corresponding response is immediately returned. This step ensures fast and accurate responses for common or clearly defined questions.

If no exact keyword match is detected, the chatbot switches to a TF-IDF–based similarity approach. The processed responses and the user input are combined into a single corpus. TF-IDF vectorization is applied to convert text into numerical vectors that represent the importance of words relative to the entire corpus. Cosine similarity is then used to calculate how closely the user input matches each stored response.

The response with the highest similarity score is selected as the best match. A similarity threshold is applied to prevent irrelevant answers. If the similarity score is too low, the chatbot returns a fallback message informing the user that the topic is not supported and suggests related topics instead. This improves user experience and avoids misleading responses.

Debug messages are included to display which keyword or TF-IDF match was selected. These messages are helpful during development and testing, as they provide insight into the chatbot’s decision-making process.

Finally, the program runs in an infinite loop that allows continuous interaction with the user. It greets the user, accepts input, processes queries, and prints chatbot responses. The loop terminates only when the user types “exit”, ensuring controlled and user-friendly interaction.

*OUTPUT*:
<img width="1134" height="636" alt="Image" src="https://github.com/user-attachments/assets/e90a445d-803c-4031-841a-89734953cef0" />
