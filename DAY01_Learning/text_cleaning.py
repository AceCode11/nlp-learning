import re 

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]','',text)   #keep letters only

    text = re.sub(r'\s+','',text)   #remove space

    return text.strip()

sample_text = "I am Krishna Desai,currently running NLP"
print("Original:",sample_text)
print("after",clean_text(sample_text))