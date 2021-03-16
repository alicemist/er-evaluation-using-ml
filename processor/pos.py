import nltk
import logging

##############################
#                            #
#    CALLING VALIDATORS      #
#                            #
##############################
import processor.validator as vm
import prop.messages as messages
import prop.common as properties
from core.trace import create_debug_file as create, write_debug_results as write, display
from config.settings import DEBUG as is_debugging
from config.settings import LOG as is_tracing

##############################
#                            #
#    OBJECT DEFINITION       #
#                            #
##############################
from object import sentence as s
from object import entity as e
from object import relation as r
from object import attribute as a

##############################
#                            #
#      NLTK MANAGEMENT       #
#                            #
##############################
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

##############################
#                            #
#        GLOBAL LISTS        #
#                            #
##############################
entity_list = []
attribute_list = []
relation_list = []

##############################
#                            #
#     LOG FILE SETTINGS      #
#                            #
##############################
logging.basicConfig(filename='app.log',format='%(levelname)s:%(message)s', level=logging.DEBUG)


###################################
###################################
###                             ###
###         SEGMENTATION        ###
###                             ###
###################################
###################################

# Segmentation is a method which divides a
# full-text into individual sentences. A sentence
# is a set of words that is complete in itself,
# typically containing a subject and predicate,
# conveying a statement, question, exclamation,
# or command, and consisting of a main clause
# and sometimes one or more subordinate clauses.
def segmentation(text):
    sentences_of_text = nltk.tokenize.sent_tokenize(text)
    if is_tracing:
        logging.info("Segmentation : " + str(sentences_of_text))
    return sentences_of_text

###################################
###################################
###                             ###
###         TOKENIZATION        ###
###                             ###
###################################
###################################

# Tokenization is a way of separating a piece, or
# a sentence, of text into smaller units that are
# called tokens. Tokens can be either words,
# characters, or subwords. Hence, tokenization
# can be classified into 3 types – word, character,
# and subword tokenization.
def tokenization(sentence):
    words_of_sentence = nltk.word_tokenize(sentence)
    if is_tracing:
        logging.info("Tokenization : " + str(words_of_sentence))
    return words_of_sentence

###################################
###################################
###                             ###
###          POS TAGGING        ###
###                             ###
###################################
###################################

# Tagging is a kind of classification that may be
# defined as the automatic assignment of description
# to the tokens. POS tagger divides a sentence
# into word:tag pair.
def pog_tagging(words_of_sentence):
    words_and_tags = nltk.pos_tag(words_of_sentence)
    if is_tracing:
        logging.info("Pos tags : " + str(words_and_tags))
    return words_and_tags

###################################
###################################
###                             ###
###           CHUNKING          ###
###                             ###
###################################
###################################

# We have taken a full-text as an input, it has
# been divided into separate sentences in segmentation
# feature, then each individual sentence is tokenized
# in tokeniza- tion feature, then POS tagging feature
# run for each separate sentence. So far, three
# features of six has been launched. Chunking is the
# forth feature in queue. Chunking is a method that
# makes decisions using pos tag.
def chunking(words_and_tags):
    if is_tracing:
        logging.info("Chunking : " + str(words_and_tags))
    # Beginning from this statement (except create
    # statement), we generate an instance from
    # sentence class. Looping through words_and_tags
    # array, we check any tag is in related lists.
    # The lists contains heuristic variables.
    # Then, sentence instance is updated with
    # current word.
    instance = s.sentence('', '', '')

    # Understanding which noun is object or subject.
    already_used = False

    # Looping through all details of sentence, so that
    # sentence items are stored.
    for word, tag in words_and_tags:

        if not already_used and tag in properties.noun_list:
            instance.set_subject(word)
            already_used = True

        elif tag in properties.verb_list:
            instance.set_verb(word)

        elif already_used and tag in properties.noun_list:
            instance.set_object(word)

        else:
            continue

    if is_tracing:
        logging.info(" > sentence : " + instance.get_sentence())
        logging.info(" > subject : " + instance.get_subject())
        logging.info(" > verb : " + instance.get_verb())
        logging.info(" > object : " + instance.get_object())
    return instance

###################################
###################################
###                             ###
###            PARSER           ###
###                             ###
###################################
###################################

# Before entity-relationship diagram is created, parser
# runs. Parser is a method which makes rule-based
# decisions. Parser feature uses our heuristics we
# defined before in Chapter 3. NLP has multiple possible
# analysis due to its ambiguous grammar. Parsing determines
# parse tree of a given sentence where in a group of words
# is transformed into structures. This may be inapplicable
# for our heuristic
def parser(processed_sentence):

    # Getting subject, verb and object from processed sentence.
    subject = processed_sentence.get_subject()
    verb = processed_sentence.get_verb()
    object = processed_sentence.get_object()

    ####################################################################################################
    # The execution design is given (copy of execution schema under doc):                              #
    #                                                                                                  #
    #                               Focusing on verb                                                   #
    #                                      |                                                           #
    #                       +--------------+--------------+                                            #
    #                       |                             |                                            #
    #                   Special verb               Not special verb                                    #
    #                       |                             |                                            #
    #           +-----------+--------------+              +--------------                              #
    #           |                          |                            |                              #
    #     Subject exists            Does not exists         > create new relation, then store          #
    #           |                          |                                                           #
    # > determine attribute list           |                                                           #
    # > find existing entity               +------------------+                                        #
    # > append new attributes onto                            |                                        #
    # ...existing entity                         > determine attribute list                            #
    #                                            > create new entity, then store                       #
    ####################################################################################################

    # We are focusing on verb element of sentence.
    # If it is in special verbs list, object is an attribute.
    # Otherwise, there is a relation between subject and object.
    if verb in properties.special_verb_list:
        if is_tracing:
            logging.info(messages.OBTAINED_SPECIAL_VERB.format(str(verb)))
        # While verb is in special verbs list, we must
        # check subject is in entity, or not. If the "subject"
        # is in entity, we must store object as attributes.
        if subject in vm.get_entity_names(entity_list=entity_list):
            try:
                # Retrieved attributes in a list that has been divided through comma.
                attribute_list = vm.get_divided_attributes(object=object)

                # Retrieved entity with reference point through entity name.
                # Calling method requires entity name (in this case subject),
                # and entity list (in this case entity list) to return.
                reference_of_entity = vm.get_entity_by_name(entity_name=subject, entity_list=entity_list)

                # Set new attributes onto existing entity.
                e.entity.set_attributes(reference_of_entity, attribute_list)
            except:
                if is_debugging:
                    logging.error(messages.ERROR_SPECIAL_VERB_EXISTING_ENTITY)
        # Otherwise, we must create an entity using "subject"
        # and store "the object" as attributes.
        else:
            try:
                # In this case, verb is in special verb list,
                # and subject is not in entity list. So, it means
                # a new entity has to be created, and attributes
                # have to be stored inside of it.
                attribute_list = vm.get_divided_attributes(object=object)
                new_entity = e.entity(name=subject, attributes=attribute_list)
                entity_list.append(new_entity)
            except:
                if is_debugging:
                    logging.error(messages.ERROR_SPECIAL_VERB_NEW_ENTITY)
    else:
        try:
            # new relation is created by subject as from-direction,
            # verb as action and object as to-direction. Then,
            # it is added in to relation list.
            new_relation = r.relation(who=subject, action=verb, whom=object)
            relation_list.append(new_relation)

        except:
            if is_debugging:
                logging.error(messages.ERROR_AT_RELATION)

