# TECHNIQUES USED:
# math.floor, len, range

import math

def odd_count(n):
    return math.floor(len(range(n)) / 2)


# Given a number n, return the number of positive odd numbers below n, EASY!
# Tests:
print(odd_count(7)) #=> 3, i.e [1, 3, 5]
print(odd_count(15)) #=> 7, i.e [1, 3, 5, 7, 9, 11, 13]

# [8]