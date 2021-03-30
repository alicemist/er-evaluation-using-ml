# Define attribute with name
class attribute:

    def __init__(self, name, primaryKey, multiValued):
        self.name = name
        self.primaryKey = primaryKey
        self.multiValued = str(multiValued)

    def getName(self):
        return str(self.name)

    def setName(self, name):
        self.name = name

    def isPrimaryKey(self):
        return bool(self.primaryKey)

    def setPrimaryKey(self, primaryKey):
        self.primaryKey = primaryKey

    def isMultiValued(self):
        return str(self.multiValued)

    def setMultiValued(self, multiValued):
        self.multiValued = multiValued


# composite attribtue?

# multi_valued attribute?
# has many locations, has many numbers
# has locations ozne tekil, nesne cogul.
