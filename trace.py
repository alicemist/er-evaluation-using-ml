from config.settings import is_tracing

'''
    This definition is to create trace files initially.
    Takes an input file name as string. 
    Stripped from left and right.
    
    :parameter - param is file name in string format.
    :returns - nothing.
'''
def create(param):
    file_name = str(param).lstrip().rstrip()
    file_name = file_name + '.txt'

    file = open(file_name, 'w')
    file.close()

'''
...
'''
def write(statement, text):
    # Combines with .txt
    statement = str(statement) + '.txt'

    # Verify to trace is on/off
    if (is_tracing == True):

        try:
            with open(str(statement), "r+") as log_file:
                lines_in_log_file = log_file.read()
                log_file.seek(0)
                log_file.write(str(text) + "\n" + str(lines_in_log_file))

        except:
            with open(str(statement), "a") as log_file:
                log_file.write(str(text) + "\n")

        finally:
            log_file.close()

    else:
        print("Logging is impossible to write.")

