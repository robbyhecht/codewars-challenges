# TECHNIQUES USED:
# math.sqrt, int, range, for loop, conditionals, algorithms

import math
  
def is_prime(num):
    if num > 1:
        # Reduce loop range by finding sqrt of num. The +1 ensures including the root in the range.
        sqn = int(math.sqrt(num))+1
        for n in range(2, sqn):
            if num % n is 0:
                return False
        return True
    else: return False

# Define a function that takes an integer argument and returns logical value true or false depending on if the integer is a prime.

# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
# Try to find a solution which does not loop all the way up to n.

# [6]