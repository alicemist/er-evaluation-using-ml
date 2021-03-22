


test_text = "Student has name, surname, number. Course contains title, er. Student takes course."



import nltk
nltk.download('wordnet')
lemma = nltk.wordnet.WordNetLemmatizer()
print(lemma.lemmatize('students'))

lemma.lemmatize('leaves')
