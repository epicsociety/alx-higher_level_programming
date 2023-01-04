#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord(char) in range(97, 123):
            result += chr(ord(char) - 32)
        else:
            result += chr(ord(char))
    print("{}".format(result))
