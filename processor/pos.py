'''''''''''''''''''''''''''''''''''
###################################
###################################
###                             ###
###          IMPORTS            ###
###                             ###
###################################
###################################
'''''''''''''''''''''''''''''''''''
import processor.validator as vm
import nltk
import logging
from nltk.stem import *
import prop.messages as messages
import prop.common as properties
from core.trace import create_debug_file as create, write_debug_results as write, display
from config.settings import DEBUG as isDebugging
from config.settings import LOG as isTracing
from ui.component import *

'''''''''''''''''''''''''''''''''''
###################################
###################################
###                             ###
###          OBJECTS            ###
###                             ###
###################################
###################################
'''''''''''''''''''''''''''''''''''
from object import sentence as s
from object import entity as e
from object import relation as r
from object import attribute as a


'''''''''''''''''''''''''''''''''''
###################################
###################################
###                             ###
###            RUN              ###
###                             ###
###################################
###################################
'''''''''''''''''''''''''''''''''''
def run(test):
    setup()

    for sentence in segmentation(text=test):
        try:
            parser(chunking(posTagging(tokenization(sentence))))
        except:
            display(messages.ERROR_AT_LOOPING_SENTENCE.format(str(sentence)))

    maker()


'''''''''''''''''''''''''''''''''''
###################################
###################################
###                             ###
###             SETUP           ###
###                             ###
###################################
###################################
'''''''''''''''''''''''''''''''''''
def setup():
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    logging.basicConfig(filename='app.log', format='%(levelname)s:%(message)s', level=logging.DEBUG)


'''''''''''''''''''''''''''''''''''
###################################
###################################
###                             ###
###        GLOBAL LISTS         ###
###                             ###
###################################
###################################
'''''''''''''''''''''''''''''''''''
entityList = []
attributeList = []
relationList = []
uniqueWordList = []


'''''''''''''''''''''''''''''''''''
###################################
###################################
###                             ###
###       ERD COMPONENTS        ###
###                             ###
###################################
###################################
'''''''''''''''''''''''''''''''''''

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
    sentences = nltk.tokenize.sent_tokenize(text)
    if isTracing:
        logging.info("Segmentation : " + str(sentences))
    return sentences


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
    words = nltk.word_tokenize(sentence)
    if isTracing:
        logging.info("Tokenization : " + str(words))
    return words


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
def posTagging(words):
    posPairs = nltk.pos_tag(words)
    if isTracing:
        logging.info("Pos tags : " + str(posPairs))
    return posPairs


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
def chunking(wtPair):
    if isTracing:
        logging.info("Chunking : " + str(wtPair))
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
    uniqueness = False

    # Looping through all details of sentence, so that
    # sentence items are stored.
    for word, tag in wtPair:

        if not already_used and tag in properties.nouns:
            instance.setSubject(word)
            already_used = True

        elif tag in properties.verbs:
            instance.setVerb(word)

        elif already_used and tag in properties.nouns:
            if uniqueness:
                uniqueWordList.append(word)
                uniqueness = False
            instance.setObject(word)

        elif (tag and word) in properties.pk_candidate_list:
            uniqueness = True

        else:
            continue

    if isTracing:
        logging.info(" > sentence : " + instance.getSentence())
        logging.info(" > subject : " + instance.getSubject())
        logging.info(" > verb : " + instance.getVerb())
        logging.info(" > object : " + instance.getObject())
        logging.info(" > candidate for primary key : " + str(uniqueWordList))
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
    subject = processed_sentence.getSubject()
    verb = processed_sentence.getVerb()
    object = processed_sentence.getObject()

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
    if verb in properties.specialVerbs:
        if isTracing:
            logging.info(messages.OBTAINED_SPECIAL_VERB.format(str(verb)))
        if subject in vm.getEntities(entity_list=entityList):
            try:
                insertAttribute(subject=subject, object=object)
            except:
                if isDebugging:
                    logging.error(messages.ERROR_SPECIAL_VERB_EXISTING_ENTITY)
        else:
            try:
                makeEntity(subject=subject, object=object)
            except:
                if isDebugging:
                    logging.error(messages.ERROR_SPECIAL_VERB_NEW_ENTITY)
    else:
        try:
            makeRelation(subject=subject, verb=verb, object=object)
        except:
            if isDebugging:
                logging.error(messages.ERROR_AT_RELATION)


###################################
###################################
###                             ###
###           MAKER             ###
###                             ###
###################################
###################################
def maker():
    for entity in entityList:
        print(line_border())
        print(table_line(entity.getName()))
        print(line_border())
        for attribute in entity.getAttributes():
            attribute_line = attribute.getName()
            if attribute.isPrimaryKey():
                attribute_line = 'PK : ' + attribute.getName()
            print(item_line(attribute_line))
        print(line_border())
        print()

    if len(relationList) > 0:
        print(line_border())
        print(table_line(messages.UI_TITLE_RELATION))
        print(line_border())
        for relation in relationList:
            print(relation_line(" (" + relation.getMultiplictyOne() + ") " + relation.who + " -> " + relation.action + " -> (" + relation.getMultiplictyTwo() + ") " + relation.whom))
            print(line_border())


'''''''''''''''''''''''''''''''''''
###################################
###################################
###                             ###
###            RULES            ###
###                             ###
###################################
###################################
'''''''''''''''''''''''''''''''''''
def makeRelation(subject, verb, object):

    # We should get singular form of each item
    # in the sentence to compare with originals.
    processedSubject = getSingularNoun(subject)
    processedVerb = getSingularVerb(verb)
    processedObject = getSingularNoun(object)

    # m1 represents multiplicty value in entity one,
    # m2 represents multiplicty value in entity two.
    m1 = ''
    m2 = ''

    # i.e. Student takes courses
    if processedSubject.__eq__(subject) and not processedObject.__eq__(object):
        m1 = '1'
        m2 = 'N'

    # i.e. Student takes course
    if processedSubject.__eq__(subject) and processedObject.__eq__(object):
        m1 = '1'
        m2 = '1'

    # i.e. Students take course
    if not processedSubject.__eq__(subject) and not processedObject.__eq__(object):
        print()


    # new relation is created by subject as from-direction,
    # verb as action and object as to-direction. Then,
    # it is added in to relation list.
    new_relation = r.relation(who=processedSubject,
                              action=processedVerb,
                              whom=processedObject)
    new_relation.setMultiplictyOne(m1)
    new_relation.setMultiplictyTwo(m2)
    relationList.append(new_relation)


def makeEntity(subject, object):
    # In this case, verb is in special verb list,
    # and subject is not in entity list. So, it means
    # a new entity has to be created, and attributes
    # have to be stored inside of it.
    attributes = getDividedAttributes(object=object)
    uniqueWordList.clear()

    newEntity = e.entity(name=getSingularNoun(subject), attributes=attributes)
    entityList.append(newEntity)


def insertAttribute(subject, object):
    # Retrieved attributes in a list that has been divided through comma.
    attributes = getDividedAttributes(object=object)
    uniqueWordList.clear()

    # Retrieved entity with reference point through entity name.
    # Calling method requires entity name (in this case subject),
    # and entity list (in this case entity list) to return.
    entity = getEntity(entityName=subject)

    # Set new attributes onto existing entity.
    e.entity.setAttributes(entity, attributes)


'''''''''''''''''''''''''''''''''''
###################################
###################################
###                             ###
###           HELPERS           ###
###                             ###
###################################
###################################
'''''''''''''''''''''''''''''''''''
def getDividedAttributes(object):
    try:
        # Eventually, it will collect attribute.
        attributes = []

        # The object might include more than one elements
        # that is seperated with comma. Thus, we must divide it
        # into seperated elements in a list.
        if object.split(","):
            items = object.split(",")

            # We must obtain elements which will be stored.
            # Therefore, we must run a loop through divided
            # elements list. Each iteration is a potentially
            # attribute. Thus, new attribute object must be created
            # with currently iteration, and then it should be added
            # into stored list.
            for item in items:
                isPrimaryKey = False
                if item in uniqueWordList:
                    isPrimaryKey = True
                newAttribute = a.attribute(getSingularNoun(item), isPrimaryKey)
                attributes.append(newAttribute)

        # If the object contains one element certainly,
        # we must just create an attribute.
        else:
            isPrimaryKey = False
            if object in uniqueWordList:
                isPrimaryKey = True
            newAttribute = a.attribute(getSingularNoun(object), isPrimaryKey)
            attributes.append(newAttribute)

        # Returns attributes as list.
        logging.info("Attributes : " + str(attributes))
        return attributes

    except:
        logging.error(messages.ERROR_AT_DIVIDING_ATTRIBUTES)


def getEntity(entityName):
    try:
        for entity in entityList:
            if entity.getName() == entityName:
                return entity
    except:
        if isDebugging:
            logging.error(messages.ERROR_AT_SEARCHING_ENTITY_BY_NAME)


def getEntities():
    entityNames = []

    try:
        for entity in entityList:
            entityNames.append(entity.getName())

        if isTracing:
            logging.info("Entities : " + str(entityNames))

        return entityNames

    except:
        if isDebugging:
            logging.error(messages.ERROR_AT_CREATING_LIST)


def getSingularNoun(word):
    lemma = nltk.wordnet.WordNetLemmatizer()
    return lemma.lemmatize(word)


def getSingularVerb(word):
    stemmer = SnowballStemmer("english")
    return stemmer.stem(word)


def makePrimaryKey(entityName, attributeName):
    try:
        isChanged = False
        entity = getEntity(str(entityName).lower())
        attributes = entity.getAttributes()

        for attribute in attributes:
            if attribute.getName() == attributeName:
                attribute.setPrimaryKey(True)
                isChanged = True
                if isChanged:
                    logging.info(attributeName + " is made primary key in " + entityName)

        if not isTracing:
            if isChanged:
                logging.info(attributeName + " is not made primary key in " + entityName)

        maker()

    except:
        if isDebugging:
            logging.error("makePrimaryKey is not run properly")
