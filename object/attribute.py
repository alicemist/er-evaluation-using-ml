# Define attribute with name
class attribute:

    def __init__(self, name, primaryKey):
        self.name = name
        self.primaryKey = primaryKey

    def getName(self):
        return str(self.name)

    def setName(self, name):
        self.name = name

    def isPrimaryKey(self):
        return bool(self.primaryKey)

    def setPrimaryKey(self, primaryKey):
        self.primaryKey = primaryKey

# multi_valued - composite
# has many locations, has many numbers
# has locations ozne tekil, nesne cogul.
