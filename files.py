import fileinput
import glob
import re
import sys

def test1():
    fh = open("./data.txt", "r")
    first_line = fh.readline()
    print(first_line)
    first_second = fh.readline()
    print(first_second)
    for i, line in enumerate(fh):
        if i > 1:
            break
        print("___", line.strip().title())


    my_data = fh.readlines()
    fh.close()




def test_file():
    fh = open("data.txt", "r")
    for line in fh:
        print(line)
    fh.close()


strings = ["aaa\n", "bbb\n", "ccc\n", "dddd\n"]

output = open('monitoring', 'r+')
output.writelines(strings)
# output.flush()
# fl = output.readline()

output.close()




append = open('logging', 'a')


pattern = sys.argv.pop(1)
if sys.platform == "win32":
    sys.argv[1:] = glob.glob(sys.argv[1])
more_files = len(sys.argv[1:])
for line in fileinput.input():
    m = re.search(pattern, line)
    if m:
        if more_files > 1:
            print(fileinput.filename(), ": ", end='')
        print(line)



