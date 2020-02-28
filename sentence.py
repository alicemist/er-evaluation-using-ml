
from trace import create,write
import datetime

class sentence:

    def __init__(self, subject, verb, object):
        self.id = str(datetime.datetime.now())
        self.subject = subject
        self.verb = verb
        self.object = object
        self.log_file = create("ser-" + self.id)

    def get_id(self):
        return str(self.id)

    def get_subject(self):
        return str(self.subject)

    def set_subject(self, subject):
        try:
            already_added = self.get_subject()
            recently_added = str(subject).lower()
            self.subject = already_added + '$' + recently_added
        except:
            write(self.id, self.log_file("An error occured in set subject method."))

    def get_verb(self):
        return str(self.verb)

    def set_verb(self, verb):
        try:
            already_added = self.get_verb()
            recently_added = str(verb).lower()
            self.verb = already_added + '$' + recently_added
        except:
            write(self.id, self.log_file("An error occured in set verb method."))

    def get_object(self):
        return str(self.object)

    def set_object(self, object):
        try:
            already_added = self.get_object()
            recently_added = str(object).lower()
            self.object = already_added + '$' + recently_added
        except:
            write(self.id, self.log_file("An error occured in set object method."))

    def get_sentence(self):
        return str(self.subject) + ' ' + str(self.verb) + ' ' + str(self.object)

