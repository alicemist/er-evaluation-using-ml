from config import settings
from prop import messages as message

def create_debug_file(param):

    if settings.DEBUG:
        try:
            file_name = str(param).lstrip().rstrip()
            file_name = file_name + '.txt'
            file = open(settings.DEBUG_PATH + file_name, 'w')
        except:
            print(message.FILE_ALREADY_EXISTS)
        finally:
            file.close()
    else:
        print(message.ERROR_AT_CREATING_FILE)

def write_debug_results(file_name, text):
    file_name = str(file_name) + '.txt'

    if settings.DEBUG:
        try:
            with open(settings.DEBUG_PATH + str(file_name), "r+") as log_file:
                lines_in_log_file = log_file.read()
                log_file.seek(0)
                log_file.write(str(text) + "\n" + str(lines_in_log_file))
        except:
            with open(settings.DEBUG_PATH + str(file_name), "a") as log_file:
                log_file.write(str(text) + "\n")
        finally:
            log_file.close()
    else:
        print(message.DEBUG_IS_CLOSED)

def display(text):
    file_name = "log.txt"

    if settings.LOG:
        try:
            with open(settings.LOG_PATH + str(file_name), "r+") as log_file:
                lines_in_log_file = log_file.read()
                log_file.seek(0)
                log_file.write(str(text) + "\n" + str(lines_in_log_file))
        except:
            with open(settings.LOG_PATH + str(file_name), "a") as log_file:
                log_file.write(str(text) + "\n")
        finally:
            log_file.close()
    else:
        print(message.LOG_IS_CLOSED)
