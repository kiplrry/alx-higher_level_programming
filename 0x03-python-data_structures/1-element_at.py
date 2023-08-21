#!/usr/bin/python3
def element_at(my_list, idx):
    '''Returns the element at index idx'''
    if (idx > len(my_list)) | (idx < 0):
        return None
    return my_list[idx]
