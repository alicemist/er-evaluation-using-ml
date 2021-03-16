
import processor.pos as s
import prop.messages as messages
from core.trace import display
import prop.common as properties
from ui.component import *

test_text = "Student has name, surname, number. Course contains title, er. Student takes course."

for sentence in s.sentence_segmentation(text=test_text):
    try:
        s.chunking(s.tokenization(sentence))
        print(s.chunking(s.tokenization(sentence)))
    except:
        display(messages.ERROR_AT_LOOPING_SENTENCE.format(str(sentence)))




for entity in s.entity_list:
    print(line_border())
    print(table_line(entity.get_name()))
    print(line_border())
    for attribute in entity.get_attributes():
        print(item_line(attribute.get_name()))
    print(line_border())
    print()






