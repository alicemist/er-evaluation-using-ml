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


EID = 0  # entity id
AID = 0  # attribute id
RID = 0  # relation id

from object import entity as e
from object import attribute as a
from object import relation as r

# We will add entity object into entity list,
# attribute object into attribute list,
# relation object into relation list.

stu = e.entity("student", "")
entity_list = [stu]
attribute_list = []
relation_list = []

# We are focusing on verb to selection algorithm.
# Therefore, we have to define special verbs into this list.
special_verbs_list = ["takes", "contains", "have", "has", "includes"]

# @warning
def get_entity_names():
    list_for_entity_names = []

    for entity in entity_list:
        current = entity.get_name()
        list_for_entity_names.append(current)

    return list_for_entity_names

# @warning
def get_entity_by_name(name):

    for entity in entity_list:
        if entity.get_name() == name:
            return entity



def handler(processed_sentence):
    subject = processed_sentence.get_subject()
    verb = processed_sentence.get_verb()
    object = processed_sentence.get_object()

    # We are focusing on verb element of sentence.
    # If it is in special verbs list, object is an attribute.
    # Otherwise, there is a relation between subject and object.
    if verb in special_verbs_list:

        # While verb is in special verbs list, we must
        # check subject is in entity, or not. If the "subject"
        # is in entity, we must store object as attributes.
        if subject in get_entity_names():

            '''
            Starts repeated code lines
            '''
            # Eventually, it will collect attribute.
            attribute_list = []

            # The object might include more than one elements
            # that is seperated with comma. Thus, we must divide it
            # into seperated elements in a list.
            if object.split(","):
                divided_elements = object.split(",")

                # We must obtain elements which will be stored.
                # Therefore, we must run a loop through divided
                # elements list. Each iteration is a potentially
                # attribute. Thus, new attribute object must be created
                # with currently iteration, and then it should be added
                # into stored list.
                for current_element in divided_elements:
                    new_attribute = a.attribute(current_element)
                    attribute_list.append(new_attribute)

            # If the object contains one element certainly,
            # we must just create an attribute.
            else:
                new_attribute = a.attribute(object)
                attribute_list.append(new_attribute)
            '''
            Finishes repeated code lines
            '''

            # The subject already exists.
            # Find it, and stores attributes inside of it.
            reference_of_entity = get_entity_by_name(subject)

            e.entity.set_attributes(reference_of_entity, attribute_list)

        # Otherwise, we must create an entity using "subject"
        # and store "the object" as attributes.
        else:
            # In this case, verb is in special verb list,
            # and subject is not in entity list. So, it means
            # a new entity has to be created, and attributes
            # have to be stored inside of it.
            new_entity = e.entity(subject, "")
            '''
            Starts repeated code lines
            '''
            # Eventually, it will collect attribute.
            attribute_list = []

            # The object might include more than one elements
            # that is seperated with comma. Thus, we must divide it
            # into seperated elements in a list.
            if object.split(","):
                divided_elements = object.split(",")

                # We must obtain elements which will be stored.
                # Therefore, we must run a loop through divided
                # elements list. Each iteration is a potentially
                # attribute. Thus, new attribute object must be created
                # with currently iteration, and then it should be added
                # into stored list.
                for current_element in divided_elements:
                    new_attribute = a.attribute(current_element)
                    attribute_list.append(new_attribute)

            # If the object contains one element certainly,
            # we must just create an attribute.
            else:
                new_attribute = a.attribute(object)
                attribute_list.append(new_attribute)
            '''
            Finishes repeated code lines
            '''
            new_entity = e.entity(subject, attribute_list)

    else:
        # will be implemented relation state.
        new_relation = r.relation(subject, verb, object)
        relation_list.append(new_relation)
