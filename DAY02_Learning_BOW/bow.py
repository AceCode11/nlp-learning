from sklearn.feature_extraction.text import CountVectorizer

documents = [
"Starting with NLP in Day 2",
"Hope I can be consistent"
]

vector = CountVectorizer()

x = vector.fit_transform(documents)

print("Vocabulary:", vector.get_feature_names_out())

print("bagOfWords:",x.toarray())
