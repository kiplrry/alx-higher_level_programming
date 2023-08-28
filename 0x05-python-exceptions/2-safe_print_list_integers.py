#!/usr/bin/python3
def safe_print_list_integers(my_list=[], y=0):
    count = 0
    for ind in range(y):
        try:
            print("{:d}".format(int(my_list[ind])), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print('')
    return count
