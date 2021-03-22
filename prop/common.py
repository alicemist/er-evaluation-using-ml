
# "Verb list" and "noun list" are simply used in tagger
# in Part-of-Speech (POS) module. They are defined heuristically.
# Lists might be expanded with another rules, or tags.
verbs = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
nouns = ['NN', 'NNS', 'NNP', 'NNPS']

pk_candidate_list = ['JJ', 'unique']
# We are focusing on verb to selection algorithm.
# Therefore, we have to define special verbs into this list.
specialVerbs = ["contains", "have", "has", "includes"]

# If there is no returning value.
nothing = ""