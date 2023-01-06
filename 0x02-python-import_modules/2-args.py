#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = sys.argv
    if len(x) == 1:
        print("{} arguments.".format(len(x) - 1))
    elif len(x) == 2:
        print("{} argument:".format(len(x) - 1))
    else:
        print("{} arguments:".format(len(x) - 1))
    for args in range(len(x)):
        if args == 0:
            continue
        print("{:d}: {:s}".format(args, x[args]))
