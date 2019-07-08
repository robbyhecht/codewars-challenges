# TECHNIQUES USED:
# math.sqrt, multiple arguments, geometry

import math

def other_angle(a, b):
    c = 180 - a - b
    return c

print(other_angle(20, 90))

def other_side(a, b): # prints hypotenuse if given sides
    c = math.sqrt(a*a + b*b)
    return c

print(other_side(7, 3))


# You are given two angles (in degrees) of a triangle.
# Write a function to return the 3rd.
# Note: only positive integers will be tested.
#BONUS: do the same when given triangle legs