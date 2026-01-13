from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I am Krishna Desai",
    "Learning TFIDFvectorizer"
]

vector = TfidfVectorizer()

x = vector.fit_transform(documents)

print("Voculabory:",vector.get_feature_names_out())
print("TF-IDf matrix:",x.toarray())