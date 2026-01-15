import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report,accuracy_score

data = pd.read_csv(r'spam.csv',encoding="latin-1")
print(data.head())

data = data[['v1', 'v2']]
data.columns = ['label', 'text']

x = data['text']
y = data['label']

vectorizer = TfidfVectorizer(stop_words='english',max_features=3000)
x_tfidf = vectorizer.fit_transform(x)

x_train,x_test,y_train,y_test  = train_test_split(x_tfidf,y,test_size=0.3,random_state=42)

model =  MultinomialNB()
model.fit(x_train,y_train)

y_pred  = model.predict(x_test)

print("accuracy is:",accuracy_score(y_test,y_pred))
print("classification report",classification_report(y_test,y_pred))

import pickle
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model and vectorizer saved successfully.")