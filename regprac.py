import re

p = re.compile("[a-zA-Z]+")
m = p.search("3pythonisNojam")
print(m)
