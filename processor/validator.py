from core.trace import create_debug_file as create, write_debug_results as write, display
import prop.messages as messages
import logging
import nltk
from nltk.stem import *

##############################
#                            #
#    OBJECT DEFINITIONS      #
#                            #
##############################
from object import attribute as a
from object import entity as e
from object import relation as r
import prop.common as properties

##############################
#                            #
#     LOG FILE SETTINGS      #
#                            #
##############################
logging.basicConfig(filename='validator.log',format='%(levelname)s:%(message)s', level=logging.DEBUG)

nltk.download('wordnet')

##############################
#                            #
#        VALIDATORS          #
#                            #
##############################

# Get divided attributes using object
def getDividedAttributes(object, uniqueness_list):
    try:
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
                primary_key = False
                if current_element in uniqueness_list:
                    primary_key = True
                new_attribute = a.attribute(current_element, primary_key)
                attribute_list.append(new_attribute)

        # If the object contains one element certainly,
        # we must just create an attribute.
        else:
            primary_key = False
            if object in uniqueness_list:
                primary_key = True
            new_attribute = a.attribute(object, primary_key)
            attribute_list.append(new_attribute)

        # Returns attributes as list.
        logging.info("Attributes : " + str(attribute_list))
        return attribute_list

    except:
        logging.error(messages.ERROR_AT_DIVIDING_ATTRIBUTES)

# Get the reference of entity using name and entity list
def getEntityByName(entity_name, entity_list):
    try:
        for entity in entity_list:
            if entity.getName() == entity_name:
                return entity
        return properties.nothing

    except:
        logging.error(messages.ERROR_AT_SEARCHING_ENTITY_BY_NAME)

# Get entity names using entity list
def getEntities(entity_list):
    list_for_entity_names = []

    try:
        for entity in entity_list:
            current = entity.getName()
            list_for_entity_names.append(current)

        logging.info("Entities : " + str(list_for_entity_names))
        return list_for_entity_names

    except:
        logging.error(messages.ERROR_AT_CREATING_LIST)


def getFirstForm(word, is_verb):
    stemmer = SnowballStemmer("english")
    lemma = nltk.wordnet.WordNetLemmatizer()
    if is_verb:
        return stemmer.stem(word)
    return lemma.lemmatize(word)




def make_primary_key(entity_name, attribute_name, entity_list):

    # entity'yi getir
    # entity icerisindeki attribute lari cek
    # uygun bir tane var ise pk yap
    entity = getEntityByName(str(entity_name).lower(), entity_list)
    attributes = entity.getAttributes()

    for attribute in attributes:
        if attribute.getName() == attribute_name:
            attribute.setPrimaryKey(True)

    return None
