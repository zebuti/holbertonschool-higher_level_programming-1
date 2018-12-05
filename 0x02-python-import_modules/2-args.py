#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_count = len(argv)
    if argv_count < 1:
        print("{:d} argument.".format(argv_count))
    else:
        print("{:d} arguments:".format(argv_count))
        index = 1
        while index <= argv_count:
            print("{:d}: {:s}".format(index, sys.argv[index]))
            index += 1
