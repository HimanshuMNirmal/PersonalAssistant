import spacy

# Load the SpaCy English model
nlp = spacy.load("en_core_web_sm")

def find_location(question):
    # Preprocess the question (optional)
    question = question.lower()

    # Perform named entity recognition (NER)
    doc = nlp(question)

    # Extract entities labeled as "GPE" or "LOC"
    locations = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC"]]

    # Filter out non-location entities (optional)
    # Add additional validation if needed

    return locations

# Example usage:
question = "What is the capital of California?"
result = find_location(question)
print("Locations:", result)
