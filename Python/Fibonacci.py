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