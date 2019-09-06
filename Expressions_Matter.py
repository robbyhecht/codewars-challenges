# TECHNIQUES USED:
# conditionals, algorithms
# **could have listed and used max method rather than conditionals

def expressions_matter(a, b, c):

    if a != 1 and b != 1 and c != 1:
        return a*b*c
    elif a==1 and c==1:
        return a+b+c
    elif a > c :
        return a * (b+c)
    else: return (a+b) * c


# Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ().

# Notes:
# The numbers are always positive.
# The numbers are in the range (1  ≤  a, b, c  ≤  10).
# You can use the same operation more than once.
# It's not necessary to place all the signs and brackets.
# Repetition in numbers may occur .
# You cannot swap the operands. For instance, in the example of 1, 2, 3 you cannot get expression (1 + 3) * 2 = 8.