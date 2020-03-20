
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
            if self.get_subject():
                already_added = self.get_subject()
                recently_added = str(subject).lower()
                self.subject = already_added + ',' + recently_added
            else:
                self.subject = str(subject).lower()
        except:
            write(self.id, self.log_file("An error occurred in set subject method."))

    def get_verb(self):
        return str(self.verb)

    def set_verb(self, verb):
        try:
            if self.get_verb():
                already_added = self.get_verb()
                recently_added = str(verb).lower()
                self.verb = already_added + ',' + recently_added
            else:
                self.verb = str(verb).lower()
        except:
            write(self.id, self.log_file("An error occurred in set verb method."))

    def get_object(self):
        return str(self.object)

    def set_object(self, object):
        try:
            if self.get_object():
                already_added = self.get_object()
                recently_added = str(object).lower()
                self.object = already_added + ',' + recently_added
            else:
                self.object = str(object).lower()
        except:
            write(self.id, self.log_file("An error occurred in set object method."))

    def get_sentence(self):
        return "{} {} {}".format(self.get_subject(), self.get_verb(), self.get_object())

