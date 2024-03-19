# Module 4 Homework: Exercise 2
#

from pathlib import Path
from pprint import pprint


def get_cats_info(path) -> list:
    file_path = Path(path)  # create Path object for file

    try:  # check for errors with path/file
        with open(file_path, 'r', encoding='utf-8') as file:
            cat_list = []
            for line in file:  # process each line in the file

                try:  # check for errors with entries in the file
                    id_, name, age = line.split(',')
                    cat = {
                        'id': id_.strip(),
                        'name': name.strip(),
                        'age': age.strip()
                    }
                    cat_list.append(cat)

                except ValueError:  # skip lines where there are no valid entries
                    continue

            if cat_list:
                return cat_list  # return a list with a dictionary for each cat
            else:
                print('There are no valid entries in the file.')
                return cat_list  # return empty list

    except Exception as expt:  # output file access exception and return an empty list
        print('Exception: ', expt)
        return []


cats_info = get_cats_info("01/cats_file.txt")
pprint(cats_info)

