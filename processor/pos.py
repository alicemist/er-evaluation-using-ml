import nltk

##############################
#                            #
#    CALLING VALIDATORS      #
#                            #
##############################
import processor.validator as vm
import prop.messages as messages
import prop.common as properties
from core.trace import create_debug_file as create, write_debug_results as write, display


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
#          DIVIDER           #
#                            #
##############################
def divider(text):
    return nltk.tokenize.sent_tokenize(text)


##############################
#                            #
#          TAGGER            #
#                            #
##############################
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

    # Understanding which noun is object or subject.
    already_used = False

    # Looping through all details of sentence, so that
    # sentence items are stored.
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


##############################
#                            #
#          HANDLER           #
#                            #
##############################
def handler(processed_sentence):

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
        display(messages.OBTAINED_SPECIAL_VERB.format(str(verb)))

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
                display(messages.ERROR_SPECIAL_VERB_EXISTING_ENTITY)

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
                display(messages.ERROR_SPECIAL_VERB_NEW_ENTITY)
    else:
        try:
            # new relation is created by subject as from-direction,
            # verb as action and object as to-direction. Then,
            # it is added in to relation list.
            new_relation = r.relation(who=subject, action=verb, whom=object)
            relation_list.append(new_relation)

        except:
            display(messages.ERROR_AT_RELATION)

# TODO: Delete fonksiyonu eklenecek, entity adı yazılarak o ve ona bağlı diğer veriler silinecek