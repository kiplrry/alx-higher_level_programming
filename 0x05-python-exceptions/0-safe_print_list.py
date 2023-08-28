#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for ind in range(x):
            print("{}".format(my_list[ind]), end='')
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
