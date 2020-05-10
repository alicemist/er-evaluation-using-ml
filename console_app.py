import processor.pos as s
import prop.messages as messages
from core.trace import display
from ui.component import *

def main(test_text):

    # Execute all pos-methods
    for sentence in s.divider(text=test_text):
        try:
            s.handler(s.tagger(sentence))
        except:
            display(messages.ERROR_AT_LOOPING_SENTENCE.format(str(sentence)))

    # Tables
    for entity in s.entity_list:
        print(line_border())
        print(table_line(entity.get_name()))
        print(line_border())
        for attribute in entity.get_attributes():
            print(item_line(attribute.get_name()))
        print(line_border())
        print()

    # Relations
    if len(s.relation_list) > 0:
        print(line_border())
        print(table_line(messages.UI_TITLE_RELATION))
        print(line_border())
        for relation in s.relation_list:
            print(relation_line(relation.who + " -> " + relation.action + " -> " + relation.whom))
            print(line_border())

if __name__ == "__main__":

    while True:
        choice = int(input(messages.UI_CHOICE_DESCRIPTION))

        test_text = ""

        if choice == 1:
            test_text = messages.UI_SAMPLE_DATA
        elif choice == 2:
            test_text = input(messages.UI_CHOICE_TEXT)
        elif choice == 3:
            break
        else:
            print(messages.UI_CHOICE_ERROR)

        main(test_text)
