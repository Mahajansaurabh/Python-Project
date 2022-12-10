from pathlib import Path

folder = Path('/Users/mrmahajan/Downloads/Python Course with Notes 2/0. Introduction')

if not folder.exists():
 print("This file doesn't exist" )
else:
    print("Yes.It exists")


