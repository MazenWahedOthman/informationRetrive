import  re
from collections import defaultdict

def departDataSet(corpus_data):
    # process the text file

    corpus_chunk_title = re.compile('\.[T] ')
    corpus_chunk_txt = re.compile(' \.W ')  # not enough
    corpus_chunk_txt_pub = re.compile(' \.[W,B] ')
    corpus_chunk_publication = re.compile(' \.[B] ')
    corpus_chunk_author = re.compile(' \.[A] ', re.MULTILINE)
    corpus_chunk_author_add_cross = re.compile(' \.[A,N,X] ', re.MULTILINE)  # not enough
    corpus_chunk_add_cross = re.compile(' \.[B,N,X] ')
    corpus_chunk_add_cross1 = re.compile(' \.[N,X] ')

    # process the document data

    chunked_corpus = defaultdict(dict)

    for line in corpus_data:
        entries = re.split(corpus_chunk_title, line)
        id = entries[0].strip()  # save id
        no_id = entries[1]

        if len(re.split(corpus_chunk_txt, no_id)) == 2:  # is there text?
            no_id_entries = re.split(corpus_chunk_txt_pub, no_id)
            chunked_corpus[id]['text'] = no_id_entries[0].strip()  # save title
            chunked_corpus[id]['text'] = chunked_corpus[id]['text'] + ' ' + no_id_entries[1].strip()  # save text
            no_title_txt = no_id_entries[2]

            if len(re.split(corpus_chunk_author, no_title_txt)) == 2:  # is there an author?
                no_title_entries = re.split(corpus_chunk_author_add_cross, no_title_txt)
                chunked_corpus[id]['text'] = chunked_corpus[id]['text'] + ' ' + no_title_entries[
                    0].strip()  # save publication date
                chunked_corpus[id]['text'] = chunked_corpus[id]['text'] + ' ' + no_title_entries[
                    1].strip()  # save author
                chunked_corpus[id]['add_date'] = no_title_entries[2].strip()  # save add date
                chunked_corpus[id]['cross-references'] = no_title_entries[3].strip()  # save cross-references

            else:
                no_title_entries = re.split(corpus_chunk_add_cross1, no_title_txt)
                chunked_corpus[id]['text'] = chunked_corpus[id]['text'] + ' ' + no_title_entries[
                    0].strip()  # save publication date
                chunked_corpus[id]['author'] = ''  # save author
                chunked_corpus[id]['add_date'] = no_title_entries[1].strip()  # save add date
                chunked_corpus[id]['cross-references'] = no_title_entries[2].strip()  # save cross-references

        else:
            no_id_entries = re.split(corpus_chunk_publication, no_id, 1)
            chunked_corpus[id]['text'] = no_id_entries[0].strip()  # save title
            no_title = no_id_entries[1]

            if len(re.split(corpus_chunk_author, no_title, 1)) == 2:  # is there an author?
                no_title_entries = re.split(corpus_chunk_author_add_cross, no_title)
                chunked_corpus[id]['text'] = chunked_corpus[id]['text'] + ' ' + no_title_entries[
                    0].strip()  # save publication date
                chunked_corpus[id]['text'] = chunked_corpus[id]['text'] + ' ' + no_title_entries[
                    1].strip()  # save author
                chunked_corpus[id]['add_date'] = no_title_entries[2].strip()  # save add date
                chunked_corpus[id]['cross-references'] = no_title_entries[3].strip()  # save cross-references

            else:
                no_title_entries = re.split(corpus_chunk_add_cross1, no_title)
                chunked_corpus[id]['text'] = chunked_corpus[id]['text'] + ' ' + no_title_entries[
                    0].strip()  # save publication date
                chunked_corpus[id]['author'] = ''  # save author
                chunked_corpus[id]['add_date'] = no_title_entries[1].strip()  # save add date
                chunked_corpus[id]['cross-references'] = no_title_entries[2].strip()  # save cross-references
    return chunked_corpus

def parsing_text(chunked_corpus):
    dictionary = {
        "u.s": "united states",
        "u.s.a": "united states",
        "u.n": "united nations",
        "i.e": "example",
        "e.g.": "for example",
        "m.p": "member of the house of lords",
        "IBM": "International Business Machines Corporation",
        "TSS": "Time Sharing System",
    }
    for store, x in chunked_corpus.items():
        text = x['text']
        for key in dictionary.keys():
            # print(dictionary[key])
            text = text.replace(key, dictionary[key])
            x['text'] = text
    return chunked_corpus