import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#cosine similarity or Jaccard similarity

# # Initialize NLTK components
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Function to preprocess text
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    return ' '.join(tokens)

# Function to compare similarity between query and database questions
def find_similar_question(query,database_questions):
    
    # Sample questions from the database
    # database_questions = [
    #     "How do I become a data scientist?",
    #     "what is time",
    #     # "tell me the time",
    # ]

    # Preprocess database questions
    preprocessed_database_questions = [preprocess_text(question) for question in database_questions]

    # Vectorize preprocessed questions
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(preprocessed_database_questions)

    preprocessed_query = preprocess_text(query)
    query_vector = vectorizer.transform([preprocessed_query])
    
    similarities = cosine_similarity(query_vector, tfidf_matrix)
    most_similar_index = similarities.argmax()
    
    return database_questions[most_similar_index]

# Example usage
# query = "jarvis can you tell me the time"
# similar_question = find_similar_question(query)
# print("Similar question in the database:", similar_question)
