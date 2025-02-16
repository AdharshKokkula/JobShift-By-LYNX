import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text, top_n=10):
    words = re.findall(r'\b\w+\b', text.lower())
    common_words = set(["the", "and", "is", "to", "in", "for", "on", "with"])  # Stopwords
    filtered_words = [word for word in words if word not in common_words]
    return [word for word, _ in Counter(filtered_words).most_common(top_n)]

def compute_ats_score(resume_text, job_desc):
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_desc)
    
    match_score = len(set(resume_keywords) & set(job_keywords)) / len(set(job_keywords))
    return f"ATS Score: {match_score:.2f}"
