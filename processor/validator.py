from core.trace import create_debug_file as create, write_debug_results as write, display
import prop.messages as messages

# Included objects here.
from object import attribute as a
from object import entity as e
from object import relation as r
import prop.common as properties

def get_divided_attributes(object):
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
                new_attribute = a.attribute(current_element)
                attribute_list.append(new_attribute)

        # If the object contains one element certainly,
        # we must just create an attribute.
        else:
            new_attribute = a.attribute(object)
            attribute_list.append(new_attribute)

        # Returns attributes as list.
        return attribute_list

    except:
        display(messages.ERROR_AT_DIVIDING_ATTRIBUTES)


def get_entity_by_name(entity_name, entity_list):
    try:
        for entity in entity_list:
            if entity.get_name() == entity_name:
                return entity
        return properties.nothing

    except:
        display(messages.ERROR_AT_SEARCHING_ENTITY_BY_NAME)


def get_entity_names(entity_list):
    list_for_entity_names = []

    try:
        for entity in entity_list:
            current = entity.get_name()
            list_for_entity_names.append(current)

        return list_for_entity_names

    except:
        display(messages.ERROR_AT_CREATING_LIST)