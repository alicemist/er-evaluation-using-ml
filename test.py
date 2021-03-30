


test_text = "Student takes many course."



import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')

word = ["Mark", "works", "in", "JPMC", "in", "London", "every day"]
posPairs = nltk.pos_tag(word)





# parse tree cizdirmece:
ne = nltk.ne_chunk(posPairs)
# print(ne)
#ne.draw()

chunked = nltk.ne_chunk_sents(posPairs, binary=True)
# print(chunked)

# IN = nltk.re.compile(r'.*\bin\b(?!\b.+ing)')

#LOCATION’, ‘ORGANIZATION’, ‘PERSON’, ‘DURATION’, ‘DATE’, ‘CARDINAL’, ‘PERCENT’, ‘MONEY’, ‘MEASURE’)
# for rel in nltk.sem.extract_rels('PERSON', 'ORGANIZATION', ne, corpus='ace', pattern=IN):
    # print(nltk.sem.rtuple(rel))


#print("selamlar")

import nltk
gram = ("NP: {<DT>?<NN>}")
sent = "last night i saw a black dog barking at a kid"

#chunking = nltk.RegexpParser(gram)

#print(chunking)
#sent_token = nltk.word_tokenize(sent)
#print(sent_token)

#tagging = nltk.pos_tag(sent_token)
#print(tagging)

#tree = chunking.parse(tagging)

# print(tree)


'''
import nltk
with open('sample.txt', 'r') as f:
    sample = f.read()


sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

entity_names = []
for tree in chunked_sentences:
    # Print results per sentence
    # print extract_entity_names(tree)

    entity_names.extend(extract_entity_names(tree))

# Print all entity names
#print entity_names

# Print unique entity names
print (set(entity_names))
'''