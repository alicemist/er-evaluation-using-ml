# Define relation with from-action-to
class relation:

    def __init__(self, who, action, whom):
        self.who = who
        self.action = action
        self.whom = whom

    def get_action(self):
        return str(self.action)