from collections import namedtuple

person = namedtuple('person', ['name', 'height','weight'])
michael = person('Michael', 1.76, 79)
print(michael[2])
