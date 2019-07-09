# TECHNIQUES USED:
# sort, conditionals, for loop, indices

def stray(arr):
    arr.sort()
    if arr[0] != arr[1]:
        return arr[0]
    else: return arr[-1]  
    
# OR WITH FOR LOOP AND CONDITIONALS:
    
# def stray(arr):
#     if (arr[0] != arr[1] and arr[1] is arr[2]):
#         return arr[0]
#     elif (arr[0] != arr[1] and arr[1] != arr[2]):
#         return arr[1]
#     else:
#         for num in arr:
#             if num is arr[0]:
#                 pass
#             else:
#                 if num is not num-1:
#                     return num

# -----

# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.
# The input array will always be valid! (odd-length >= 3)

# [7]