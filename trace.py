
from config import settings


def create(param):
    try:
        try:
            file_name = str(param).lstrip().rstrip()
            file_name = file_name + '.txt'
            file = open(settings.PATH_FOR_OUTPUTS + file_name, 'w')
        except:
            print("File could not be created, there might be two reason. One "
                  "is file name is wrong, second is open method could not run.")
        finally:
            file.close()
    except:
        raise ("File could not be created, because it is already existing.")


def write(file_name, text):
    file_name = str(file_name) + '.txt'

    if (settings.DEBUG == True):
        try:
            with open(settings.PATH_FOR_OUTPUTS + str(file_name), "r+") as log_file:
                lines_in_log_file = log_file.read()
                log_file.seek(0)
                log_file.write(str(text) + "\n" + str(lines_in_log_file))
        except:
            with open(settings.PATH_FOR_OUTPUTS + str(file_name), "a") as log_file:
                log_file.write(str(text) + "\n")
        finally:
            log_file.close()
    else:
        print("Logging is impossible to write.")

