import streamlit as st 
import pickle
import os

st.set_page_config(page_title='Spam detection')


st.title('Spam detection web')

st.markdown("""
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

if not os.path.exists("model.pkl") or not os.path.exists("vectorizer.pkl"):
    st.error("Model files not found. Please train the model first.")
    st.stop()

model = pickle.load(open('model.pkl','rb'))
vectorizer = pickle.load(open('vectorizer.pkl','rb'))


st.write('Enter a message to check whether it is a spam or ham')

user_input =  st.text_area('Enter SMS text here')

if st.button('Predict'):
     if user_input.strip() == "":
        st.warning("Please enter some text.")
     else:
        text_vector = vectorizer.transform([user_input])
        prediction = model.predict(text_vector)[0]

        if prediction == "spam":
            st.error("This message is **SPAM**")
        else:
            st.success("This message is **NOT SPAM**")