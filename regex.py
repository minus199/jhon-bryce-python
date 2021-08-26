import os
import re
import sys
str='/dev/sd3d 135398 69683 52176 57% /home/stuff'

result = re.findall(r'\b\d+\b', str)

str = 'copyright 2005 - 2006'
# result = re.search(r'((19|20)[0-9]{2}) - ((19|20)[0-9]{3})', str)
print(re.sub(r'((19|20)[0-9]{2}) - ((19|20)[0-9]{2})', r'\1 - 2021', str))

line = ':foo $$$$bar'
res = re.search(r'([:;,]+)(\s*)(\w+)', line)

txt = 'range Stranger in a strangeland'
m = re.search(r'range\B', txt)
print(m.start())

name = """
foo
bar

jOhnny

fizz
fuzz


"""

m = re.search(r'^john', name, re.IGNORECASE | re.MULTILINE | re.ASCII)

name, old, new = sys.argv[1:]
new_name = name
dyn_pattern = r'\.' + old + '$'
new_name = re.sub(
    dyn_pattern,
    '.' + new,
    new_name
)

print("Renaming", name, "to", new_name)
os.rename(name, new_name)
sys.exit(0)

result = re.subn(r"\d", "*", "aaaaa")

pattern = r"^The (quick|slow)(.*)(fox|camel)"
pattern = re.compile(pattern)

testy = 'The quick brown pink yellow orange camel jumps over the lazy dog'

results = pattern.replace()

results = re.search(pattern, testy)
print()
