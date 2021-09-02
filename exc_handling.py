import sys
import warnings
import time

def warning_handling():
    warnings.simplefilter('default')
    warnings.filterwarnings('error','.*')
    time.accept2dyear = True
    time.asctime((11, 1, 1, 12, 34, 56, 4, 1, 0))


    warnings.warn("Something seems a bit off")
    print("Success")
    sys.stderr.write("Some error occured")
    print("Success 2")

    my_dict = {}

    my_dict['foo'] = "bar"

    print("my val", my_dict['fo'])

    print("Finished")


try:
    open("foo")
except IOError as e:
    print(e)
except (TypeError, ValueError):
    print("Invalid filename")