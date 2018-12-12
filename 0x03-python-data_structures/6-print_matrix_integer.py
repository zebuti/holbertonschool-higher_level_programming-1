#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print()
    else:
        for row in range(len(matrix)):
            print("{:d} {:d} {:d}".format(*matrix[row]))
