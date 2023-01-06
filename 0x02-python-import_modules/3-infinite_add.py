#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = sys.argv
    sum = 0
    for args in range(1, len(x)):
        sum += int(x[args])
    print("{}".format(sum))
