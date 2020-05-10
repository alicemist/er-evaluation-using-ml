from config import settings
from prop import messages as message

#############################
#                           #
#     CREATE DEBUG FILE     #
#                           #
#############################

# Create a debug file if it does not exists, otherwise it means already exists
def create_debug_file(param):

    # If debug is true
    if settings.DEBUG:

        # Determine file name with txt extension, then open it
        try:
            file_name = str(param).lstrip().rstrip()
            file_name = file_name + '.txt'
            file = open(settings.DEBUG_PATH + file_name, 'w')

        # File already exists
        except:
            print(message.FILE_ALREADY_EXISTS)

        # Finally it must be closed
        finally:
            file.close()

    # Unless debug is true
    else:
        print(message.ERROR_AT_CREATING_FILE)
        print(message.DEBUG_IS_CLOSED)


##############################
#                            #
#     WRITE DEBUG RESULT     #
#                            #
##############################

# Write given text onto existing a file unless debug is closed
def write_debug_results(file_name, text):

    # Determine file name with txt extension
    file_name = str(file_name) + '.txt'

    # If debug is true
    if settings.DEBUG:

        # Create a file, then write the given text
        try:
            with open(settings.DEBUG_PATH + str(file_name), "r+") as log_file:
                lines_in_log_file = log_file.read()
                log_file.seek(0)
                log_file.write(str(text) + "\n" + str(lines_in_log_file))

        # Write given text, if the file already exists
        except:
            with open(settings.DEBUG_PATH + str(file_name), "a") as log_file:
                log_file.write(str(text) + "\n")

        # Finally it must be closed
        finally:
            log_file.close()

    # Unless debug is true
    else:
        print(message.DEBUG_IS_CLOSED)


##############################
#                            #
#     COLLECT LOG RESULT     #
#                            #
##############################

# Display logs in a spesific file unless log is closed
def display(text):
    file_name = "log.txt"

    # If log is true
    if settings.LOG:

        # If file does not exists, open and write the given text
        try:
            with open(settings.LOG_PATH + str(file_name), "r+") as log_file:
                lines_in_log_file = log_file.read()
                log_file.seek(0)
                log_file.write(str(text) + "\n" + str(lines_in_log_file))

        # Otherwise, write the given text
        except:
            with open(settings.LOG_PATH + str(file_name), "a") as log_file:
                log_file.write(str(text) + "\n")

        # Finally it must be closed
        finally:
            log_file.close()

    # Unless log is true
    else:
        print(message.LOG_IS_CLOSED)