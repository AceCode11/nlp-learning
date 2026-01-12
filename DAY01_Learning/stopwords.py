import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


nltk.download('stopwords')
text = "I am learning about stopwords so it will be easy i guess"
tokens = word_tokenize(text)

stop_word= set(stopwords.words('english'))
filter_tokens = [word for word in tokens if word.lower() not in stop_word]

print('Before:',tokens)
print('After:',filter_tokens)