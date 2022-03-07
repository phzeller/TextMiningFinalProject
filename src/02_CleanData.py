import pandas as pd
import nltk
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

minutes = pd.read_pickle('../data/FOMC/minutes.pickle')

# Data cleaning:
# Tokenization, cleaning, normalization, stemming, stop-word removal, lemmatization

def preprocessing(text):
    # 1. Tokenization: text preprocessing step, which assumes splitting text into tokens
    ret = nltk.word_tokenize(text) # TODO: discuss if tokenizing on sentence level also makes sense
    # 2. Cleaning: remove punctuation
    ret = [t for t in ret if t not in string.punctuation]
    # 3. Stop words removal
    stop_words = set(nltk.corpus.stopwords.words('english'))
    ret = [t for t in ret if t.lower() not in stop_words]
    # 4. Lemmatization
    lemmatizer = nltk.stem.WordNetLemmatizer()
    ret = [lemmatizer.lemmatize(t) for t in ret]
    return ret


minutes['cleaned content'] = minutes['contents'].map(lambda x: preprocessing(x))

minutes.to_csv('../data/minutes.csv', index=False)