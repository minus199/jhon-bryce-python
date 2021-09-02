import glob
import os


def infinite_gen(start_val=1):
    while True:
        yield start_val
        start_val += 1

# for num in infinite_gen(10):
#     print(num)


def get_dir(path):
    pattern = path + '/*'
    for file in glob.iglob(pattern):
        if os.path.isdir(file):
            yield file


dir_gen = get_dir('./')
as_list = list(dir_gen)

as_list_comph = [file.upper() for file in get_dir('./')]

for dir in get_dir('./'):
    print(dir)


def get_dir(path):
    while True:
        pattern = (path if path else '') + '/*'
        path = None
        for file in glob.iglob(pattern):
            if os.path.isdir(file):
                path = yield file
                if path: break
                if not path: break


gen = get_dir('./')
print("!!", next(gen))
print("!!", next(gen))
print(gen.send('/tmp'))
print("!!", next(gen))
