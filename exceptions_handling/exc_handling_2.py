import sys


def print_to_stderr():
    try:
        f = open("foo")
        f.close()
    except IOError as err:
        # this is how we can print to stderr instead of the default stdout
        print(err, file=sys.stderr)
    else:
        print("Everything is OK")
    finally:
        print("Finally block")


try:
    print_to_stderr()
except EnvironmentError:
    print("An env error occurred", file=sys.stderr)
print('-' * 100)
try:
    print_to_stderr()
except EnvironmentError:  # we dont have to keep the exception into a variable
    pass  # We could also ignore the error

print('-' * 100)

# `with` in python is called a `context manager` - will try to open a file, and always close it with us having to call close
with open("../hello.py") as fh2:
    print(fh2.readlines())

print('-' * 100)


#  We can disable all asserts by either:
#  - Running the script with -O flag: python -O my_script.py
#  - Setting the env var PYTHONOPTIMIZE to 0
def assert_all_is_true(*arguments):
    assert all(arguments), "False argument in myfunc"
    return True


try:
    assert_all_is_true('Tom', '', 42)
except AssertionError as e:
    print("Assertion failed", e)

print('-' * 100)


# how to raise the same exception again
def validate_email(email):
    try:
        raise Exception(email)
    except Exception:
        # we know the exception happened, we can do intermediate handling, and raise the same exception again..
        # We can also raise new exceptions from here if we need
        print("Re throwing the same exception")
        raise  # re-throws the same exception we caught.

    # We can also throw again the same exception like so
    # try:
    #     raise Exception("Email not valid")
    # except Exception as e:
    #     print(" intermediate handling")
    #     raise e # re-throws the same exception we caught.


try:
    validate_email("invalid email address")
except Exception as e:
    print(e)
