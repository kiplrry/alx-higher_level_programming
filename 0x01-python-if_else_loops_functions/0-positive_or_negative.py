#!/usr/bin/python3
import random
number = random.randint(-10, 10)
match number:
    case num if num > 0:
        print(f"{number} is positive")
    case num if num == 0:
        print(f"{number} is positive")
    case num if num < 0:
        print(f"{number} is negative")
