
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

class Sentence:

    # Construct any instance
    def __init__(self, noun, verb, adjective, adverb, preposition, conjuction, pronoun, interjection):
        self.noun = noun
        self.verb = verb
        self.adjective = adjective
        self.adverb = adverb
        self.preposition = preposition
        self.conjuction = conjuction
        self.pronoun = pronoun
        self.interjection = interjection

    # Get any variable
    @property
    def get_noun(self):
        return str(self.noun)

    @property
    def get_verb(self):
        return str(self.verb)

    @property
    def get_adjective(self):
        return str(self.adjective)

    @property
    def get_adverb(self):
        return str(self.adverb)

    @property
    def get_preposition(self):
        return str(self.preposition)

    @property
    def get_conjuction(self):
        return str(self.conjuction)

    @property
    def get_pronoun(self):
        return str(self.pronoun)

    @property
    def get_interjection(self):
        return str(self.interjection)

    # Set any variable
    @property
    def set_noun(self, noun):
        self.noun = str(noun).lower()

    @property
    def set_verb(self, verb):
        self.verb = str(verb).lower()

    @property
    def set_adjective(self, adjective):
        self.adjective = str(adjective).lower()

    @property
    def set_adverb(self, adverb):
        self.adverb = str(adverb).lower()

    @property
    def set_preposition(self, preposition):
        self.preposition = str(preposition).lower()

    @property
    def set_conjunction(self, conjunction):
        self.conjunction = str(conjunction).lower()

    @property
    def set_pronoun(self, pronoun):
        self.pronoun = str(pronoun).lower()

    @property
    def set_interjection(self, interjection):
        self.interjection = str(interjection).lower()

