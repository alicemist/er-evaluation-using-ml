class entity:

    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def get_name(self):
        return str(self.name)

    def get_attributes(self):
        return self.attributes

    def set_name(self, name):
        self.name = str(name).lower()

    def set_attributes(self, attributes):
        self.attributes = attributes