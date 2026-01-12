import nltk
from nltk.stem import PorterStemmer,WordNetLemmatizer

nltk.download('wordnet')

stemmer = PorterStemmer()
lemmitizer = WordNetLemmatizer()

words = ['studies','playing','roaming']

for word in words:
    print(f"{word} Stem: {stemmer.stem(word)} | Lemma: {lemmitizer.lemmatize(word)}")