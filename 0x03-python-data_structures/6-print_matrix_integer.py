#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for i in matrix:
        for j in i:
            if i.index(j) == len(i) - 1:
                print(f"{j}")
            else:
                print(j, end=" ")
