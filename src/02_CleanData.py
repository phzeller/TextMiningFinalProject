import pandas as pd
import nltk
import string
import os
from tqdm import tqdm

tqdm.pandas()

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


# Data cleaning:
# Tokenization, cleaning, normalization, stemming, stop-word removal, lemmatization
def preprocessing(text):
    # 1. Tokenization: text preprocessing step, which assumes splitting text into tokens
    ret = nltk.word_tokenize(text)  # TODO: discuss if tokenizing on sentence level also makes sense
    # 2. Cleaning: remove punctuation
    ret = [t for t in ret if t not in string.punctuation]
    # 3. Stop words removal
    stop_words = set(nltk.corpus.stopwords.words('english'))
    ret = [t for t in ret if t.lower() not in stop_words]
    # 4. Lemmatization
    lemmatizer = nltk.stem.WordNetLemmatizer()
    ret = [lemmatizer.lemmatize(t) for t in ret]
    return ret


script_dir = os.path.dirname(__file__)
rel_path_CLEANED = "../data/cleaned_data"
rel_path_FOMC = "../data/FOMC"
files = os.listdir(os.path.join(script_dir, rel_path_FOMC))
if not os.path.exists(os.path.join(script_dir, rel_path_CLEANED)):
    os.makedirs(os.path.join(script_dir, rel_path_CLEANED))

for file in files:
    print('Currently preprocessing: {filetitle}'.format(filetitle=file))
    df = pd.read_csv(os.path.join(script_dir, rel_path_FOMC + '/' + file))
    df['cleaned content'] = df['contents'].progress_map(lambda x: preprocessing(x))
    file_name = file.split(".")[0] + '_cleaned.csv'
    df.to_csv(os.path.join(script_dir, rel_path_CLEANED + '/' + file_name), index=False)
