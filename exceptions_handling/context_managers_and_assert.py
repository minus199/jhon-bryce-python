# `with` in python is called a `context manager` - will try to open a file, and always close it with us having to call close
# __enter__, __exit__
if __name__ == '__main__':
    with open("../hello.py") as fh2:
        print(f'fh is closed? {fh2.closed}')
        print(fh2.readlines())

    print(f'fh is closed? {fh2.closed}')
    input("\nHit enter\n")


#  We can disable all asserts by either:
#  - Running the script with -O flag: python -O my_script.py
#  - Setting the env var PYTHONOPTIMIZE to 0
def assert_all_is_true(*arguments):
    assert all(arguments), f"False argument in assert_all_is_true - {arguments}"
    return True


if __name__ == '__main__':
    assert_all_is_true('Tom', '', 42)

    try:
        assert_all_is_true('Tom', '', 42)
    except AssertionError as e:
        print("Assertion failed", e)

    input("Hit enter")
    try:
        assert_all_is_true('Tom', 'Banana', 42)
        print("Assertion success! all data is valid")
    except AssertionError as e:
        print("Assertion failed", e)
