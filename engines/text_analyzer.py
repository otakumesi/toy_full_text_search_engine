import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


STEMMER = SnowballStemmer('english')
STOP_WORDS = set(stopwords.words('english'))


def analyze(text):
    tokens = tokenize(text)
    tokens = lower_case_filter(tokens)
    tokens = stop_word_filter(tokens)
    tokens = stemmer_filter(tokens)
    return tokens

def tokenize(text):
    return word_tokenize(text)

def lower_case_filter(tokens):
    return [token.lower() for token in tokens]

def stop_word_filter(tokens):
    return [token for token in tokens if token not in STOP_WORDS]

def stemmer_filter(tokens):
    return [STEMMER.stem(token) for token in tokens]
