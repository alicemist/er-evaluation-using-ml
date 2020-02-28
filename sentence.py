
'''
The part of speech explains how a word is used in a sentence. There are
eight main parts of speech - nouns, pronouns, adjectives, verbs, adverbs,
prepositions, conjunctions and interjections.

   * Noun (N)- Daniel, London, table, dog, teacher, pen, city, happiness, hope
   * Verb (V)- go, speak, run, eat, play, live, walk, have, like, are, is
   * Adjective(ADJ)- big, happy, green, young, fun, crazy, three
   * Adverb(ADV)- slowly, quietly, very, always, never, too, well, tomorrow
   * Preposition (P)- at, on, in, from, with, near, between, about, under
   * Conjunction (CON)- and, or, but, because, so, yet, unless, since, if
   * Pronoun(PRO)- I, you, we, they, he, she, it, me, us, them, him, her, this
   * Interjection (INT)- Ouch! Wow! Great! Help! Oh! Hey! Hi!
'''

class sentence:

    # Construct any instance
    def __init__(self, subject, verb, object):
        self.subject = subject
        self.verb = verb
        self.object = object
        # trace.create()

    # Get any property
    def get_subject(self):
        return str(self.subject)

    def set_subject(self, subject):
        try:
            already_added = self.get_subject()
            recently_added = str(subject).lower()
            self.subject = already_added + '$' + recently_added
        except:
            print("hey")

    def get_verb(self):
        return str(self.verb)

    def set_verb(self, verb):
        try:
            already_added = self.get_verb()
            recently_added = str(verb).lower()
            self.verb = already_added + '$' + recently_added
        except:
            print("hey")

    def get_object(self):
        return str(self.object)

    def set_object(self, object):
        try:
            already_added = self.get_object()
            recently_added = str(object).lower()
            self.object = already_added + '$' + recently_added
        except:
            print("hey")

