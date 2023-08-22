#!/usr/bin/python3
def no_c(my_string):
    unw = ['c', 'C']
    new_str = my_string
    new_str = ''.join(ind for ind in new_str if ind not in unw)
    return (new_str)
