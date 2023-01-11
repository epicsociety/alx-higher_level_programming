#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [found if found != search else replace for found in my_list]
