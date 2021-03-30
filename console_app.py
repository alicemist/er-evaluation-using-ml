import processor.pos as s
import prop.messages as messages
from config.settings import DEBUG, LOG

while True:
    choice = int(input(messages.UI_CHOICE_DESCRIPTION))

    test_text = ""

    if choice == 1:
        test_text = "A university contains many faculties. Faculty has unique id and name. Each department belongs to a faculty. A department includes many programs"
        s.run(test=test_text)
    elif choice == 2:
        test_text = input("Enter your text : ")
        s.run(test=test_text)
    elif choice == 3:
        entityName = input("Enter entity name : ")
        attributeName = input("Enter attribute name : ")
        s.makePrimaryKey(entityName=entityName, attributeName=attributeName)
    elif choice == 4:
        break
    else:
        print(messages.UI_CHOICE_ERROR)

