# https://www.python.org/dev/peps/pep-3101/ - search in page for "Standard Format Specifiers"
# more examples - https://pyformat.info/
import os

flt = 22 / 7
first = 'Gengis'
second = 'Khan'
file = ".gitignore"
country = "the Mongol Empire"
mood = "happy"

template = "Hello, my name is {1} {1} {1} and i'm from {0}. I'm feeling {2} | {3}"
print(template.format(country, first, mood, second))
print(template.format("asaf", "israel", mood, second))
print("Hello, my name is {name} and i'm from {country}. I'm feeling {mood}".format(name=first, country=country, mood=mood))

planets = {'Mercury': 57.91858483,
           'Venus': 108.2122,
           'Earth': 149.597870,
           'Mars': 227.944356}

for i, key in enumerate(planets.keys(), 1):
    print(" - {0:4d} {1:.<100s} {2:08.4f} Gm".format(i, key, planets[key]))

# input("Hit enter to continue")

print("Float: {0:11.8f}, sci: {0:e}".format(flt))
print("Name: {:<20s} {:<10s}".format(first, second))
fred = '{:#x}'.format(3735928559)

perms = '0{:o}'.format((os.stat(file).st_mode) & 0o7777)


print("Float format: %11.8f, scientific: %e" % (flt, flt))
print("***Name: %40s %-10s!" % (first, second))


text = 'hello'
print(text.capitalize())
print(text.upper())
print('<' + text.center(12) + '>')
print('<' + text.ljust(12) + '>')
print('<' + text.rjust(12) + '>')
print('<' + text.zfill(12) + '>')
