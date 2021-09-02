import sys
sys.path.append("./my_modules")
import my_modules

# my_modules.nested_modules.module_b

# my_modules.new_variable
"""
This is some description

    >>> x = "fooo"
    >>> print(x)
"""
if __name__ == "__main__":
    # uncomment the following lines to run the doctest string
    # import doctest
    # doctest.testmod()

    person = my_modules.new_person("fred", 20)
    my_modules.stuff_doer.do_stuff_with_person(person)
