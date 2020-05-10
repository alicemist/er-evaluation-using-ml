
# "Verb list" and "noun list" are simply used in tagger
# in Part-of-Speech (POS) module. They are defined heuristically.
# Lists might be expanded with another rules, or tags.
verb_list = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
noun_list = ['NN', 'NNS', 'NNP', 'NNPS']

# We are focusing on verb to selection algorithm.
# Therefore, we have to define special verbs into this list.
special_verb_list = ["contains", "have", "has", "includes"]

# If there is no returning value.
nothing = ""