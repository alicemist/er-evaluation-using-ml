
from pos import tagger, divider, handler


from object import attribute

from object import entity as e


example = "Student takes courses courses"

# Check "divider" under pos.py
#print(divider(text=example))

# Check handler under pos.py
handler(tagger(example))
#handler(tagger("course belongs to a department"))
#handler(tagger("a course has title and department"))
#handler(tagger("course has prefix"))
#handler(tagger("course has prefix"))
#handler(tagger("course has prefix"))


#print(tagger(example).get_sentence())

example1 = "Student includes numbers"

handler(tagger(example1))