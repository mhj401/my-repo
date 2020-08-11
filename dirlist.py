import os

def dir_list(param_string):
    with os.scandir(param_string) as entries:
        for entry in entries:
            print(entry.name)


dir_list('my_directory/')