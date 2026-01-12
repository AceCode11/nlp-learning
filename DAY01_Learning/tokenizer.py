import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
text = 'I am learning NLP by my own'
tokens =  word_tokenize(text)

print(tokens)