from collections import defaultdict
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from get_data import  get_data
from depart_dataset import departDataSet
from flask import  Flask

from depart_dataset import parsing_text
from numpy import double
from preprocessing import remove_stop_words
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from preprocessing import  marge
from preprocessing import  remove_common_words_tok_lower
from preprocessing import  lemmtization_query
from preprocessing import stemming_query
from preprocessing import  marge_query
from cosine_similarity1 import cosine_similarity1
from cosine_similarity1 import  cosine_similarity



import sys
import os
import pandas as pd
import numpy as np
import nltk.stem as stemmer
from nltk.corpus import stopwords,words
#from nltk.corpus import words
#from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
from collections import defaultdict
import re
lemmatizer = WordNetLemmatizer()
from datetime import datetime
import nltk.tokenize as nt
from operator import itemgetter
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
IDs_marker = re.compile('\.I ')
app=Flask(__name__)
@app.route('/api/<oo>',methods=['GET'])
def routeApi(oo):
    text_index=print_hi('PyCharm')
    query_text=print_hi2(oo)
    res=cosine_similarity1(text_index,query_text)
    mylist=list(res.keys())
    ff={}
    ff['response']=mylist



    return ff

def print_hi2(oo):
    z = oo
    z=remove_common_words_tok_lower(z)
    z=stemming_query(z)
    z=lemmtization_query(z)
    query_text=marge_query(z)
    return query_text

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    corpus_data = get_data('/Users/Mazen/Desktop/cacm/cacm.all', IDs_marker)
    chunked_corpus=departDataSet(corpus_data)
    chunked_corpus=parsing_text(chunked_corpus)
    corpus_dict=remove_stop_words(chunked_corpus)
    ps = PorterStemmer()
    stemm_list = []

    for store, x in chunked_corpus.items():
        for i in corpus_dict[store]:
            stemm_list.append(ps.stem(i))
        corpus_dict[store] = stemm_list
        stemm_list = []
    lemmatizer = WordNetLemmatizer()
    lemmatize_list = []
    for store, x in chunked_corpus.items():
        for i in corpus_dict[store]:
            lemmatize_list.append(lemmatizer.lemmatize(i))
        corpus_dict[store] = lemmatize_list
        lemmatize_list = []
    text_index=marge(corpus_dict)
    return  text_index




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
