# // TECHNIQUES USED:
# // while loop, memoization, multiple arguments, recursion

def fib(a, b, n):
    """
    This fibonacci function allows the user to input:
    first two numbers (a, b)
    total number of terms (n)
    """
    count = 0
    while count < n - 1:
        sum = a + b  #save the sum before changing the a value
        a = b  #now change a to b value
        b = sum  #now change b to the sum defined by nth
        count += 1
    return a



print(fib(0, 1, 10)) #34
print(fib(3, 5, 3)) #8
print(fib(0, 1, 1000))#26863810024485359386146727202142923967616609318986952340123175997617981700247881689338369654483356564191827856161443356312976673642210350324634850410377680367334151172899169723197082763985615764450078474174626