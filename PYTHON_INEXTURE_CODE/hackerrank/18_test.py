#!/bin/python3

# import math
# import os
# import random
import re
# import sys
pattern = r"^(?!\d)"

def solve(s):
    capitalized_words = []
    for x in s.split():
        if re.match(pattern, x):
            capitalized_words.append(x.capitalize())
        if not re.match(pattern, x):
            capitalized_words.append(x)
    return " ".join(capitalized_words)
        
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

s = input()
result = solve(s)
print(result)

    # fptr.write(result + '\n')

    # fptr.close()
