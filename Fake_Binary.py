# TECHNIQUES USED:
# append, int, join, str, conditionals, for loop

def fake_bin(x):
    newNum = []
    for num in x:
        num = int(num)
        if num < 5:
            num = 0
        else: num = 1
        num = str(num)
        newNum.append(num)
    return "".join(newNum)

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# [8]