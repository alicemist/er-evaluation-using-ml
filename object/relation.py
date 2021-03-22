# Define relation with from-action-to
class relation:

    def __init__(self, who, action, whom):
        self.who = who
        self.multiplicity_one = 1
        self.action = action
        self.whom = whom
        self.multiplicity_two = 2

    def get_action(self):
        return str(self.action)

    def getMultiplictyOne(self):
        return str(self.multiplicity_one)

    def setMultiplictyOne(self, val):
        self.multiplicity_one = val

    def getMultiplictyTwo(self):
        return str(self.multiplicity_two)

    def setMultiplictyTwo(self, val):
        self.multiplicity_two = val

