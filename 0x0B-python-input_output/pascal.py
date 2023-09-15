#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    def create(all, prev):
        el = [1]
        for i in range(1, len(prev)):
            el.append(prev[i - 1] + prev[i])
        el.append[1]
        all.append(el)
        return prev
    create(all, pascal_triangle(n-1))
    return all


pascal_triangle(5)

