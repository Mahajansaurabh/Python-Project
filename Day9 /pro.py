import os
from datetime import date
import shutil
import re



myFile=os.open("/Users/mrmahajan/Downloads/Project+Day+9",os.O_RDONLY)


search_date = date.today()

def directory(file):
    pattern = r'^N\w{3}[-]\d{5}'
    check = re.search(pattern,file)

