
from core.trace import create_debug_file as create, write_debug_results as write, display
import datetime

# Define a sentence with subject, verb, object
class sentence:

    def __init__(self, subject, verb, object):
        self.id = str(datetime.datetime.now())
        self.subject = subject
        self.verb = verb
        self.object = object
        self.log_file = create("ser-" + self.id)

    def get_id(self):
        return str(self.id)

    def getSubject(self):
        return str(self.subject)

    def setSubject(self, subject):
        try:
            if self.getSubject():
                already_added = self.getSubject()
                recently_added = str(subject).lower()
                self.subject = already_added + ',' + recently_added
            else:
                self.subject = str(subject).lower()
        except:
            write(self.id, self.log_file("An error occurred in set subject method."))

    def getVerb(self):
        return str(self.verb)

    def setVerb(self, verb):
        try:
            if self.getVerb():
                already_added = self.getVerb()
                recently_added = str(verb).lower()
                self.verb = already_added + ',' + recently_added
            else:
                self.verb = str(verb).lower()
        except:
            write(self.id, self.log_file("An error occurred in set verb method."))

    def getObject(self):
        return str(self.object)

    def setObject(self, object):
        try:
            if self.getObject():
                already_added = self.getObject()
                recently_added = str(object).lower()
                self.object = already_added + ',' + recently_added
            else:
                self.object = str(object).lower()
        except:
            write(self.id, self.log_file("An error occurred in set object method."))

    def getSentence(self):
        return "{} {} {}".format(self.getSubject(), self.getVerb(), self.getObject())

