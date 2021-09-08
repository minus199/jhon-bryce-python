import re
import sys
import traceback


# this is a custom exception
class EmailValidationException(Exception):
    def __init__(self, email):
        self.email = email


# this is another custom exception
class MaxAttemptsExceeded(Exception):
    pass


# let us use regex to check the pattern of a string. in this case, we test whether or not the string matches the pattern of an email
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")


def validate_email(email):
    if email_regex.match(email):
        return True

    raise EmailValidationException(email)


def do_login(user_email="", max_attempts=3):
    num_tries = 0
    while True:
        try:
            user_email = user_email if user_email else input(" > Please enter your email: ")
            validate_email(user_email.strip())
            print("You are now logged in!")
            return True  # We wont reach this line until validation is successful since it raises an exception
        except EmailValidationException as eve:
            print(f"\n ERROR:The email {eve.email} is not valid, please try again")
            if num_tries >= max_attempts:
                raise MaxAttemptsExceeded()  # notice how we can raise a different exception for the except block


do_login()
input("Press enter to continue")


def check_if_user_exists(user_email=""):
    return validate_email(user_email)


def do_login2(user_email=""):
    return check_if_user_exists(user_email)


print("\n\nErrors bubbles up until something handles them, or they crash the app")

try:
    do_login2("invalid email")
except (EmailValidationException, MaxAttemptsExceeded) as e:
    print("Printing exception stack trace")
    # this is how we can print the stacktrace of the exception. Meaning, all the places in code it passed before getting here
    traceback.print_exc(file=sys.stdout)
    tipe, val, tb = sys.exc_info()
    print("Exception line number", tb.tb_lineno)

print('-' * 100)
# this will crash the app
do_login2("invalid email")
