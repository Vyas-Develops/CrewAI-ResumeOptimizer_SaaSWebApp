import re

def extract_keywords(text):
    # A naive implementation (you can replace this with Spacy or keyword lib later)
    words = re.findall(r'\b\w+\b', text.lower())
    keywords = [word for word in words if len(word) > 4]  # filter out short/common words
    return list(set(keywords))


# to extract keywords from job description text
# This can be improved with NLP libraries like Spacy or NLTK for better keyword extraction
# For now, it uses a simple regex to find words longer than 4 characters