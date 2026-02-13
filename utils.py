import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
import nltk

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words and len(w) > 2]
    return " ".join(words)

def analyze_resume(resume, jd):
    resume_clean = preprocess(resume)
    jd_clean = preprocess(jd)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_clean, jd_clean])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    score = similarity[0][0]
    match_percentage = round(score * 100, 2)

    jd_words = set(jd_clean.split())
    resume_words = set(resume_clean.split())

    common_keywords = list(jd_words.intersection(resume_words))
    missing_keywords = list(jd_words - resume_words)

    return {
        "match_score": match_percentage,
        "common_keywords": common_keywords[:10],
        "missing_keywords": missing_keywords[:10]
    }
