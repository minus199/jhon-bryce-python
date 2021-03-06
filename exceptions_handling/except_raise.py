# simple_error_handling
import sys
from io import UnsupportedOperation


def get_file_contents(filename):
    try:
        print("Trying to open file", filename)
        fh = open(filename, "w")  # we try to open a file that does not exist
        # fh = open(filename + '_' + 1, "r")  # we try to open a file that does not exist
        print("File is open")
        try:
            return fh.readlines()
        finally:  # we can use finally without except
            fh.close()
    except UnsupportedOperation:
        print("File mode is probably incorrect", file=sys.stderr)
        raise
    except IOError as e:  # we except only exception that are IOError on inherits from the class IOError
        # this is how we can print to stderr instead of the default stdout
        # try running it like this - python exceptions_handling/except_raise.py >/dev/null
        print(e, file=sys.stderr)  # no such file exists
        return None
    except (TypeError, ValueError) as e:  # except multiple types of exceptions
        print("Invalid filename", e, file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error has occurred - {e}", file=sys.stderr)
        # we know the exception happened, we can do intermediate handling, and raise the same exception again.
        # We can also raise new exceptions from here if we need
        print("Re throwing the same exception")
        raise  # We dont have to store the exception into a variable to raise it again

        # we can also raise the exception again like this
        # raise e
    else:
        print("This code is unreachable since we have a return statement in the `try`")
    finally:
        print(filename, "Always happens")
        # see what happens when we put a return in the finally
        # return "Finally return value"


if __name__ == '__main__':
    # contents = get_file_contents("./foo")  # exception but handled
    # print(contents)

    try:
        contents2 = get_file_contents("./hello.py")  # ok
        print(contents2)
    except UnsupportedOperation as uoe:
        print("Unable to process file", uoe)

    print("All done")