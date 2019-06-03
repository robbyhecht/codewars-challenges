# Given a non-empty array of integers, return the result of multiplying the values together in order.
# Example: [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24


def grow(arr):
    allMult = 1 # 1 is neutral in multiplication
    for num in arr:
        allMult = allMult * num # apply recursive loop
    return allMult