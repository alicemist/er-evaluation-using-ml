
from pos import tagger, divider, handler


from object import attribute


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
'''
try:
    if subject:
        try:
            if subject not in entity:
                entity.append(subject)
                print("basari 1")
        except:
            print("patladık 1")

    if verb:
        try:
            if verb not in relation:
                relation.append(verb)
                print("basari 2")
        except:
            print("patladık 2")
    if object:
        try:
            if object not in attribute:
                attribute.append(object)
                print("basari 3")

        except:
            print("patladık 3 ")

except:
    print("toptan patladık")
'''