from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def calculate_match_score(resume_text, jd_text):
    """
    Compares resume text and job description text.
    Returns a match score out of 100.
    """
    documents = [resume_text, jd_text]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    score = round(similarity[0][0] * 100, 2)
    return score

def find_missing_keywords(resume_text, jd_text):
    """
    Finds important words that appear in the job description
    but are missing from the resume.
    """
    resume_words = set(re.findall(r'\b[a-zA-Z]{3,}\b', resume_text.lower()))
    jd_words = set(re.findall(r'\b[a-zA-Z]{3,}\b', jd_text.lower()))

    common_stopwords = {"the", "and", "for", "with", "you", "are", "our",
                         "will", "your", "this", "that", "have", "from"}

    jd_keywords = jd_words - common_stopwords
    missing = jd_keywords - resume_words

    return sorted(list(missing))[:15]  # show top 15 missing words