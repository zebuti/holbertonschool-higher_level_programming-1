#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print()
    else:
        for row in matrix:
            for item in row:
                print("{:d}".format(item), end=' ')
            print()
