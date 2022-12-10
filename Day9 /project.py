import shutil
import re
import time
import datetime
import os
from pathlib import Path
import math


start = time.time()

path = '/Users/mrmahajan/Downloads/Project+Day+9/My_Big_Directory'
my_pattern = r'^N\w{3}[-]\d{5}'
search_date = datetime.date.today()
numbers_found = []
files_found = []

def find_number(file,pattern):
    this_file = open(file,'r')
    text = this_file.read()
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''

def create_lists():
    for folder,subfolder,file in os.walk(path):
        for a in file:
            result = find_number(Path(folder,a),my_pattern)
            if result != '':
                numbers_found.append(result.group())
                files_found.append(a.title())


def show_all():
    index = 0
    print('-' * 50)
    print(f'Date of search: {search_date.month}/{search_date.day}/{search_date.year}')
    print('\n')
    print('File\t\t\tSERIAL NUMBER')
    print('----\t\t\t-------------')
    for a in files_found:
        print(f'{a}\t{numbers_found[index]}')
        index += 1
    print('\n')
    print(f'Numbers found: {len(numbers_found)}')
    end = time.time()
    duration = end - start
    print(f'Duration of the search: {math.ceil(duration)} seconds')
    print('-' * 50)

create_lists()
show_all()