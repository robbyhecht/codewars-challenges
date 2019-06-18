def find_2nd_largest(arr):
    newArr = [] # make an empty list
    for num in arr:
        if type(num) != int: continue
        else: newArr.append(num) # append all integers to the new list
    if len(newArr) < 2: return None # return none if there are not 2 numbers to compare
    largest = max(newArr[0], newArr[1])
    sec_larg = min(newArr[0], newArr[1]) # establish a second largest integer
    for i in range(2, len(newArr)):
        if newArr[i] > largest: # if new number is larger than largest, largest becomes sec_larg
            sec_larg = largest
            largest = newArr[i]
        else:
            if newArr[i] > sec_larg: # new sec_larg if it's in between sec_larg and largest
                sec_larg = newArr[i]
    if largest == sec_larg: # eliminate lists of all equal numbers
        return None
    else: 
        return sec_larg


print(find_2nd_largest([1, 'm', 78, 6, 4, 46, 89, 102, 5, 'test'])) #90

# **Could also use the sorted method.


# Find the 2nd largest integer in array If the array has no 2nd largest integer then return nil. Reject all non integers elements and then find the 2nd largest integer in array
# find_2nd_largest([1,2,3]) => 2
# find_2nd_largest([1,1,1,1,1]) => nil because all elements are same. Largest no. is 1. and there is no 2nd largest no.
# find_2nd_largest([1,'a','2',3,3,4,5,'b']) => 4 as after rejecting non integers array will be [1,3,3,4,5] Largest no. is 5. and 2nd largest is 4.
# Return nil if there is no 2nd largest integer. Take care of big numbers as well