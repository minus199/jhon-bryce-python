import sys
import time


def report_error(text, error, message):
    '''
    this function reports error and prints to the screen
    '''
    now = time.localtime(time.time())
    print(time.asctime(now), text, 'Error:', error, message)


filename = "./some_file"
try:
    oops = open(filename)
except IOError as err:
    report_error('Failed to open ' + filename, err.args[1])
count = 0

while (oops.readline):
    count = count + 1
    print(filename, 'has', count, 'lines')
