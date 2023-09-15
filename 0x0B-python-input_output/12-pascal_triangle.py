#!/usr/bin/python3
"""
technical question
"""
def pascal_triangle(n):
    """function creating a pascal triangle"""
    if n <= 0:
        return [[]]
    if n == 1:
        return [[1]]
    all = [[1]]
    def triangle(n):
        if n == 2:
            return [1, 1]       
        def create(prev):
            all.append(prev)
            el = [1]
            for i in range(1, len(prev)):
                el.append(prev[i - 1] + prev[i])
            el.append(1)
            return el
        return create(triangle(n-1))
    fin = triangle(n)
    all.append(fin)
    return all
