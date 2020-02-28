'''

Most POS are divided into sub-classes. POS Tagging simply
means labeling words with their appropriate Part-Of-Speech.

POS tagging is a supervised learning solution that uses features
like the previous word, next word, is first letter capitalized etc.
NLTK has a function to get pos tags and it works after
tokenization process.

'''

import nltk
import sentence as generate
from config import settings


# Download some specifications from remote repository
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def tagger(sentence):
    words_and_tags = nltk.pos_tag(nltk.word_tokenize(sentence))

    instance = generate.sentence('', '', '')

    already_used = False

    for word, tag in words_and_tags:

        if already_used == False \
                and tag in settings.NOUN:
            instance.set_subject(word)
            already_used = True

        elif tag in settings.VERB:
            instance.set_verb(word)

        elif already_used == True \
                and tag in settings.NOUN:
            instance.set_object(word)

        else:
            print("else düstüm")
