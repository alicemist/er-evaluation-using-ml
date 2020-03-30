import nltk

# Included all helpers here.
import processor.validator as vm
import prop.messages as messages
import prop.common as properties
from core.trace import create_debug_file as create, write_debug_results as write, display

# Included objects here.
from object import sentence as s
from object import entity as e
from object import relation as r
from object import attribute as a



#####################
#      Statics      #
#####################

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

entity_list = []
attribute_list = []
relation_list = []

#####################
#      Divider      #
#####################

def divider(text):
    return nltk.tokenize.sent_tokenize(text)



#####################
#      Tagger      #
#####################

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
    instance = s.sentence('', '', '')

    # This statement creates a log file that
    # is named instance's unique identifier.
    log_file = "wtp-" + instance.get_id()
    create(log_file)

    already_used = False

    for word, tag in words_and_tags:

        write(file_name=log_file, text="Word: {} - Tag: {}".format(word, tag))

        if not already_used and tag in properties.noun_list:
            instance.set_subject(word)
            already_used = True

        elif tag in properties.verb_list:
            instance.set_verb(word)

        elif already_used and tag in properties.noun_list:
            instance.set_object(word)

        else:
            continue

    return instance



#####################
#      Handler      #
#####################

def handler(processed_sentence):
    subject = processed_sentence.get_subject()
    verb = processed_sentence.get_verb()
    object = processed_sentence.get_object()

    # We are focusing on verb element of sentence.
    # If it is in special verbs list, object is an attribute.
    # Otherwise, there is a relation between subject and object.
    if verb in properties.special_verb_list:

        # While verb is in special verbs list, we must
        # check subject is in entity, or not. If the "subject"
        # is in entity, we must store object as attributes.
        if subject in vm.get_entity_names(entity_list=entity_list):

            attribute_list = vm.get_divided_attributes(object=object)

            # The subject already exists.
            # Find it, and stores attributes inside of it.
            reference_of_entity = vm.get_entity_by_name(entity_name=subject, entity_list=entity_list)

            '''
            burası yapılması lazım!?!!?!?
            '''
            print()
            # attr çekip, combine leyip setlesek??
            e.entity.set_attributes(reference_of_entity, attribute_list)

            t = reference_of_entity.get_attributes()

            print()
        # Otherwise, we must create an entity using "subject"
        # and store "the object" as attributes.
        else:
            # In this case, verb is in special verb list,
            # and subject is not in entity list. So, it means
            # a new entity has to be created, and attributes
            # have to be stored inside of it.

            attribute_list = vm.get_divided_attributes(object=object)

            new_entity = e.entity(name=subject, attributes=attribute_list)

    else:
        try:
            # new relation is created by subject as from-direction,
            # verb as action and object as to-direction. Then,
            # it is added in to relation list.
            new_relation = r.relation(subject, verb, object)
            relation_list.append(new_relation)
        except:
            display(messages.ERROR_AT_RELATION)
