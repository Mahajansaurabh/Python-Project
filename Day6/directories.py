from pathlib import Path

folder = Path('/Users/mrmahajan/Downloads/Python Course with Notes 2/0. Introduction')
file = folder / '0. Introduction'

my_file = open(file)
print(my_file.read())