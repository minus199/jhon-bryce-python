# ask input from the user - must be a valiu number
# as long as the number is smaller than 100, print the index

import sys

user_input = input("Enter a valid number")
if not user_input.isnumeric():
    sys.exit()

user_input = int(user_input)
if user_input > 100:
    sys.exit()

for i in range(user_input, 100):
    print("i", i )