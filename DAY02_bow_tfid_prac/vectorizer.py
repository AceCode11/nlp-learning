from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer

with open('sample3.txt','r',encoding='utf-8') as file:
    documents = file.read().splitlines()


print('documents',documents)

bow   = CountVectorizer()
bowmatrix = bow.fit_transform(documents)

print("bagofwords vocabulary")
print(bow.get_feature_names_out())
print("bow matrix:",bowmatrix.toarray())



vector   = TfidfVectorizer()
vectormatrix = vector.fit_transform(documents)

print("tfidf vocabulary")
print(bow.get_feature_names_out())
print("tfidfmatrix:",vectormatrix.toarray())