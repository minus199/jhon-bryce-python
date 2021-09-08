import sys
import time
import warnings


def warning_handling():
    warnings.simplefilter('default')
    warnings.filterwarnings('error', '.*')
    time.accept2dyear = True
    time.asctime((11, 1, 1, 12, 34, 56, 4, 1, 0))

    warnings.warn("Something seems a bit off")
    print("Success")
    sys.stderr.write("Some error occured")
    print("Finished")


if __name__ == '__main__':
    warning_handling()