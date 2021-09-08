import nested_modules

__doc__ = """
    usage: This is help for my module
"""

print(nested_modules.fuzz)


def do_more_stuff():
    print("more stuff")


def do_stuff_with_person(person):
    foo = "bar"
    print(__name__, 'This is ', person, nested_modules.fuzz, foo, person)


def main():
    print("Is main", __name__)


if __name__ == "__main__":
    main()
