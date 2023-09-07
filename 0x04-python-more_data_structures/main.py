#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2


a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print(new_dict)
