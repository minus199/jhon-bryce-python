import sys
import traceback

from custom_exceptions import validate_email, EmailValidationException, MaxAttemptsExceeded


def check_if_user_exists(user_email=""):
    return validate_email(user_email)


def do_login(user_email=""):
    print("step 1")
    result = check_if_user_exists(user_email)
    print("step 2")
    return result

if __name__ == '__main__':
    "We can access and print the stacktrace to where the exception happened"

    try:
        do_login("foo#bar.com")
        print("...")
    except (EmailValidationException, MaxAttemptsExceeded) as e:
        print("Printing exception stack trace")
        # this is how we can print the stacktrace of the exception. Meaning, all the places in code it passed before getting here
        traceback.print_exc(file=sys.stdout)

        print('-' * 10)

        # Exception Class, Exception instance and traceback
        tipe, val, tb = sys.exc_info()
        print("Exception finished @ line number", tb.tb_lineno)

        next_frame = tb.tb_next.tb_frame
        print("Previous line was", next_frame.f_code.co_filename, next_frame.f_lineno)

        # we can also use the debugger to see the stacktrace with Python Exception Breakpoints

    print("\n\nErrors bubbles up until something handles them, or they crash the app")
    input("Hit enter")
    # this will crash the app
    do_login("invalid email")

    print("This will not be printed since we had an exception that crashed the app")
