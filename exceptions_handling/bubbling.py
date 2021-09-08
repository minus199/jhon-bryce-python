import sys
import traceback

from custom_exceptions import validate_email, EmailValidationException, MaxAttemptsExceeded


def check_if_user_exists(user_email=""):
    return validate_email(user_email)


def do_login(user_email=""):
    return check_if_user_exists(user_email)


if __name__ == '__main__':
    print("We can access and print the stacktrace to where the exception happened")
    input("Hit enter")

    try:
        do_login("invalid email")
    except (EmailValidationException, MaxAttemptsExceeded) as e:
        print("Printing exception stack trace")
        # this is how we can print the stacktrace of the exception. Meaning, all the places in code it passed before getting here
        traceback.print_exc(file=sys.stdout)
        tipe, val, tb = sys.exc_info()
        print("Exception line number", tb.tb_lineno)

    print("\n\nErrors bubbles up until something handles them, or they crash the app")
    input("Hit enter")
    # this will crash the app
    do_login("invalid email")

    print("This will not be printed since we had an exception that crashed the app")
