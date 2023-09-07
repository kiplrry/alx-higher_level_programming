#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = dict([(x, a_dictionary[x]) for x in sorted(a_dictionary)])
    for k, v in dic.items():
        print("{}: {}".format(k, v))
