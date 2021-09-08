import sys
sys.path.append("./modules")
import modules

# modules.nested_modules.module_b

# modules.new_variable
"""
This is some description

    >>> x = "fooo"
    >>> print(x)
"""
if __name__ == "__main__":
    # uncomment the following lines to run the doctest string
    # import doctest
    # doctest.testmod()

    person = modules.new_person("fred", 20)
    modules.stuff_doer.do_stuff_with_person(person)
