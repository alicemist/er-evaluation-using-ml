'''

Most POS are divided into sub-classes. POS Tagging simply
means labeling words with their appropriate Part-Of-Speech.

POS tagging is a supervised learning solution that uses features
like the previous word, next word, is first letter capitalized etc.
NLTK has a function to get pos tags and it works after
tokenization process.

'''

import nltk
import sentence as sntnc

'''
:returns Sentence object
'''

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "My name is Jocelyn. Roger Stone was sentenced to three years and four months in prison on Thursday for lying to Congress and other crimes, after a tumultuous two weeks in which the government trial lawyers withdrew and President Trump repeatedly criticized the handling of the case."
#token = nltk.word_tokenize(sentence)
#tagged = nltk.pos_tag(nltk.word_tokenize(sentence))

'''
    ----------------
    | POS tag list |
    ----------------

    * CC	 :     coordinating conjunction
    * CD	 :     cardinal digit
    * DT	 :     determiner
    * EX	 :     existential there (like: "there is" ... think of it like "there exists")
    * FW	 :     foreign word
    * IN	 :     preposition/subordinating conjunction
    * JJ	 :     adjective	'big'
    * JJR	 :     adjective, comparative	'bigger'
    * JJS	 :     adjective, superlative	'biggest'
    * LS	 :     list marker	1)
    * MD	 :     modal	could, will
    * NN	 :     noun, singular 'desk'
    * NNS	 :     noun plural	'desks'
    * NNP	 :     proper noun, singular	'Harrison'
    * NNPS	 :     proper noun, plural	'Americans'
    * PDT	 :     predeterminer	'all the kids'
    * POS	 :     possessive ending	parent\'s
    * PRP	 :     personal pronoun	I, he, she
    * PRP$	 :     possessive pronoun my, his, hers
    * RB	 :     adverb	very, silently,
    * RBR	 :     adverb, comparative	better
    * RBS	 :     adverb, superlative	best
    * RP	 :     particle	give up
    * TO	 :     to	go 'to' the store.
    * UH	 :     interjection	errrrrrrrm
    * VB	 :     verb, base form	take
    * VBD	 :     verb, past tense	took
    * VBG	 :     verb, gerund/present participle	taking
    * VBN	 :     verb, past participle	taken
    * VBP	 :     verb, sing. present, non-3d	take
    * VBZ	 :     verb, 3rd person sing. present	takes
    * WDT	 :     wh-determiner	which
    * WP	 :     wh-pronoun	who, what
    * WP$	 :     possessive wh-pronoun	whose
    * WRB	 :     wh-abverb where, when
    
'''

# Statement for combining related part-of-speech together

# Create a new sentence-object instance
sentence = sntnc.Sentence('', '', '', '', '', '', '', '')