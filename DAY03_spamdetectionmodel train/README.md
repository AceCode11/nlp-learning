SMS Spam Detection using NLP & Streamlit
Overview

This project is an end-to-end Natural Language Processing (NLP) application that classifies SMS messages as Spam or Ham  using TF-IDF vectorization and a Naive Bayes classifier, with a Streamlit web interface for real-time predictions.

####Problem Statement####

To build a machine learning system that can automatically detect spam SMS messages using text-based features.

Dataset

Name: SMS Spam Collection Dataset

Source: UCI Machine Learning Repository / Kaggle

Size: ~5,500 SMS messages

Columns:

label → spam / ham

text → message content

*****Issue Faced & Solution*****

Issue: UnicodeDecodeError while reading the dataset due to non-UTF-8 encoding
Solution: Resolved by explicitly specifying encoding="latin-1" while loading the CSV file using pandas




-------Learning Outcomes------------

Understood real-world text preprocessing challenges

Learned how TF-IDF improves over Bag of Words

Gained hands-on experience with text classification

Built an end-to-end NLP application with a web interface



----Author---

Krishna Desai
Aspiring Data Analyst / Data Scientist
Learning NLP, Machine Learning, and Data Analytics step by step