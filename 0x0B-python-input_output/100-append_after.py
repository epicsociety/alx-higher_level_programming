#!/usr/bin/python3
"""module has one function"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    args:
    @filename: filename
    @search_string: string
    @new_string: new
    """
    with open(filename, 'r', encoding='utf-8') as f:
        current_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            current_list.append(line)
            if search_string in line:
                current_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(current_list)
