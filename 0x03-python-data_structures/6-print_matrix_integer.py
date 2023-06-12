#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[0])):
            print("{:d}".format(matrix[row][column]),
                    end=" " if column < len(matrix[0]) - 1 else '\n')
