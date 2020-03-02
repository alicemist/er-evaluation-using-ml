import nltk
import sentence as generate
from config import settings
from trace import create, write


# Download some specifications from remote repository
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# sentence divider
def divider(text):
    return nltk.tokenize.sent_tokenize(text)


def tagger(sentence):
    # This statement gives us tokenized words and
    # pos tags. We are using nltk to obtain pos tags.
    # nltk has own pos tag method that uses tokenized
    # words, then obtains pos tag for each word in
    # input sentence.
    words_and_tags = nltk.pos_tag(nltk.word_tokenize(sentence))

    # Beginning from this statement (except create
    # statement), we generate an instance from
    # sentence class. Looping through words_and_tags
    # array, we check any tag is in related lists.
    # The lists contains heuristic variables.
    # Then, sentence instance is updated with
    # current word.
    instance = generate.sentence('', '', '')

    # This statement creates a log file that
    # is named instance's unique identifier.
    log_file = "wtp-" + instance.get_id()
    create(log_file)

    already_used = False

    for word, tag in words_and_tags:

        write(log_file, "Word: {} - Tag: {}".format(word, tag))

        if already_used == False and tag in settings.NOUN:
            instance.set_subject(word)
            already_used = True

        elif tag in settings.VERB:
            instance.set_verb(word)

        elif already_used == True and tag in settings.NOUN:
            instance.set_object(word)

        else:
            continue

    return instance

EID = 0 # entity id
AID = 0 # attribute id
RID = 0 # relation id

def handler(processed_sentence):

    entity = []
    attribute = []
    relation = []
    special_verbs = ["contains", "have", "has"]

    subject = processed_sentence.get_subject()
    verb = processed_sentence.get_verb()
    object = processed_sentence.get_object()

    if subject in entity:
        print("")
        
    else:
        print("")














