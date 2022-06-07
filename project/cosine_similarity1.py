import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from pandas import DataFrame
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from operator import itemgetter

def cosine_similarity1(txt_index,query_text):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix_train = tfidf_vectorizer.fit_transform(txt_index)
    tfidf_matrix_test = tfidf_vectorizer.transform(query_text)
    cos = cosine_similarity(tfidf_matrix_train, tfidf_matrix_test)
    s = {}
    h = 1
    for i in cos:
        for j in i:
            s[h] = j
        h = h + 1
    res = dict(sorted(s.items(), key=itemgetter(1), reverse=True)[:10])
    return res




