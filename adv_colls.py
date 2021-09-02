import glob
import os

pattern = './**/*'
my_files_glob = glob.iglob(pattern)
output = list(filter(lambda fname: fname.endswith(".pdf") and os.path.isfile(fname), my_files_glob))

for fname in my_files_glob:
    print(fname)

for fname in (filter(os.path.isfile, my_files_glob)):
    print(fname)

my_numbers = range(1, 100)

output = [num * num for num in my_numbers]
output = [num * num for num in my_numbers if num % 2 == 0]

# sizes = []
# for fname in glob.iglob(pattern):
#     if os.path.isfile(fname):
#         sizes.append((fname, os.path.getsize(fname)))
#
sizes = [(fname, os.path.getsize(fname)) for fname in glob.iglob(pattern) if os.path.isfile(fname)]
print()

my_numbers = [1, 1, 1, 2, 3, 2, 3, 2, 3, 4, 4, 4, 4, 4]
output = {num * num for num in my_numbers} # set without filter
output = {num * num for num in my_numbers if num % 2 == 0} # set with filter
output = {f'index-{num}': num * num for num in my_numbers if num % 2 == 0} # dict with filter
print()


my_numbers = range(1, 100)
mapped = map(lambda num: num * num, my_numbers)
print()
