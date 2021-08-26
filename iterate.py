import sys
list = ["a", "b", "c", "d"]
dict = {
    'foo': "bar",
    "fizz": "fuzz",
    "buzz": "bizz"
}

# for index, value in enumerate(list):
#     print("Currently on index", index, value)



farms = ['Home Farm', 'Muckworthy', 'Scales End', 'Brown Rigg', 'foo']
squirls = [42, 12, 2, 0]
rabbits = [395, 68, 57, 32, 1]
moles = [12, 8, 0, 29]


for (f, s, r, m) in zip(farms, squirls, rabbits, moles):

    if f ==` "Scales End":
        sys.exit("Enough")
    print('Total for', f, ':', s, r,  m)
