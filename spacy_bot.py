import spacy
#nlp = spacy.load("es_dep_news_trf")
nlp = spacy.load("en_core_web_sm")

def spacy_info(text):
    doc = nlp(text)
    print([(w.text, w.pos_) for w in doc])
    return doc
