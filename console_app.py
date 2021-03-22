import processor.pos as s
import prop.messages as messages
import logging
logging.basicConfig(filename='app.log',format='%(levelname)s:%(message)s', level=logging.DEBUG)

while True:
    choice = int(input(messages.UI_CHOICE_DESCRIPTION))

    test_text = ""

    if choice == 1:
        test_text = "Student has unique name, surname, number. Course contains title, number. Student takes course"
        s.run(test=test_text)
    elif choice == 2:
        test_text = input("Enter your text : ")
        s.run(test=test_text)
    elif choice == 4:
        s.makePrimaryKey("student", "surname")
    elif choice == 3:
        break
    else:
        print(messages.UI_CHOICE_ERROR)

