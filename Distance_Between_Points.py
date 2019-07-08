# TECHNIQUES USED:
# math.sqrt, multiple arguments, round

import math

def distance(x1, y1, x2, y2):
    # Your code here
    run = x2 - x1
    rise = y2 - y1
    dist = round(math.sqrt(run ** 2 + rise ** 2), 2)
    return dist


print(distance(1, 1, 0, 0)) #1.41

# Given two ordered pairs calculate the distance between them. Round to two decimal places.
