from pos import divider, tagger

# 1. Get all requirement text
requirements = input("Enter your requirements: ")

# 2. Divide requirement text into sentences
sentences_in_requirements = divider(requirements)

# 3. Call tagger for each sentence in requirement text
for sentence in sentences_in_requirements:
    tagger(sentence)



