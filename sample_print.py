# user_input = input("Choose a number")
# user_input = int(user_input)
my_multiline_string = '''
asd
zxc
            gfd
hfg
jhg
khjk

'''

range()



my_list = ["xxxxxxxxxxxxxx", 'a', 'b']
my_list_copy = ["xxxxxxxxxxxxxx", 'a', 'b']
my_list2 = my_list


print(my_list is my_list_copy)
print(my_list is my_list2)

if len(my_list) >= 4:
    print("Big")


number = "30"
distance = 41
if 0 < number < 42 < distance:
    print("OK")
else:
    print("Not OK")


i = 1; j = 120
while i < 42:
    i = i * 2
    if i > j:
        break
    else:
        print("Loop expired: ",i)
