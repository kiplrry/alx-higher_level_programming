#!/usr/bin/python3
if __name__ == "__main__":
    def print_matrix_integer(matrix=[[]]):
        if matrix == [[]]:
            print("$")
        for i in matrix:
            for j in i:
                if i.index(j) == len(i) - 1:
                    print(f"{j}$")
                else:
                    print(j, end=" ")
        
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)
    print("uuuu")
    print_matrix_integer()
