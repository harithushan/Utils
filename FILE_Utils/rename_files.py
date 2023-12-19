from pprint import pprint
import os

source_folder ='D:/Documents/path'

search_pattern = "*.*"
files = os.listdir(source_folder)
counter = 1
for file in files:
    file_name = os.path.splitext(file)[0]
    file_extension = os.path.splitext(file)[1]
    new_file_name = "" + str(counter) + file_extension

    old_file_path = os.path.join(source_folder, file)
    new_file_path = os.path.join(source_folder, new_file_name)
    os.rename(old_file_path, new_file_path)
    pprint(f'file `{old_file_path}` renamed to {new_file_path}')
    counter += 1
