# Define entity with name, attributes
class entity:

    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
# primary key burada olacak.
# weak entity.

    def getName(self):
        return str(self.name)

    def getAttributes(self):
        return self.attributes

    def setName(self, name):
        self.name = str(name).lower()

    def setAttributes(self, attributes):
        if attributes == "":
            self.attributes = attributes
        self.attributes = str(self.attributes) + ' ' + str(attributes)

    def find(self, name):
        if self.name == name:
            return self
