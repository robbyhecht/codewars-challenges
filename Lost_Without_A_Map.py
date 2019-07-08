# TECHNIQUES USED:
# map, list comprehension, for loop, append

def maps(a):
    return list(map(lambda x: x*2, a))    

## or with comprehension--
def maps2(a):
    return [(num * 2) for num in a]
    
## or with for loop--
def maps3(a):
    newList = list()
    for num in a:
        newList.append(num*2)
    return newList


# Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]

# [8]