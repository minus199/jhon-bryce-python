import re


# this is a custom exception
class EmailValidationException(Exception):
    def __init__(self, email):
        self.email = email


# this is another custom exception
class MaxAttemptsExceeded(EmailValidationException):
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
        num_tries += 1
        try:
            email = user_email if user_email else input(" > Please enter your email: ")
            validate_email(email.strip())
            input("You are now logged in!")
            return True  # We wont reach this line until validation is successful since it raises an exception
        except EmailValidationException as eve:
            print(f"\n ERROR:The email {eve.email} is not valid, please try again")
            if num_tries >= max_attempts:
                # notice how we can raise a different exception for the except block
                raise MaxAttemptsExceeded("Blocking further attempts to login")


if __name__ == "__main__":
    do_login()
