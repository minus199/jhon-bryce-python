# simple_error_handling
def get_file_contents(filename):
    try:
        print("Trying to open file", filename)
        fh = open(filename, "r")  # we try to open a file that does not exist
        print("File is open")
        try:
            return fh.readlines()
        finally:  # we can use finally without except
            fh.close()
    except IOError as e:  # we except only exception that are IOError on inherits from the class IOError
        print(e)  # no such file exists
        return None
    except (TypeError, ValueError) as e:  # except multiple types of exceptions
        print("Invalid filename", e)
        return None
    except Exception as e:
        print(f"Unexpected error has occurred - {e}")
        return None
    finally:
        print(f"Always happens")
        # return "Finally return value"


contents = get_file_contents("./foo")  # exception but handled
contents2 = get_file_contents("./hello.py")  # ok
