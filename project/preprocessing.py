import  re
from nltk.tokenize import sent_tokenize, word_tokenize

def remove_stop_words(chunked_corpus):
    from nltk.corpus import stopwords
    import string
    from nltk.tokenize import word_tokenize
    corpus_dict = {}
    file = open("/Users/Mazen/Desktop/cacm/common_words", "r")
    fileData = file.read()
    file.close()
    stopwords = re.findall("\S+", fileData)
    for store, x in chunked_corpus.items():
        tokens = word_tokenize(x['text'])
        tokens = [w.lower() for w in tokens]
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
        stop_words = set(stopwords)
        words = [w for w in stripped if not w in stop_words]
        corpus_dict[store] = words
    return corpus_dict

def marge(corpus_dict):
    txt_doc = ''
    txt_index = []
    txt_index.append(''.join(corpus_dict))
    # for store, x in corpus_dict.items():
    #     for i in x:
    #         txt_doc = txt_doc + i + ' '
    #     txt_index.append(txt_doc)
    #     txt_doc = ''
    return  txt_index
def remove_common_words_tok_lower(query):
    filtered= []
    file = open("/Users/Mazen/Desktop/cacm/common_words", "r")
    fileData = file.read()
    file.close()
    stopwords = re.findall("\S+", fileData)
    for w in word_tokenize(query.lower()):
        if w not in stopwords:
            filtered.append(w)
    return filtered
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

def lemmtization_query(query):
    lemmatized_string= [lemmatizer.lemmatize(words) for words in query]
    return lemmatized_string
from nltk.stem import PorterStemmer
ps = PorterStemmer()

def stemming_query(query):
    stemm =[ps.stem(words) for words in query]
    return stemm
def marge_query(z):
    query_text = []
    query_text.append(''.join(z))
    # string1 = ''
    # for i in z:
    #     string1 = string1 + str(i) + ' '
    # query_text.append(string1)
    return query_text






