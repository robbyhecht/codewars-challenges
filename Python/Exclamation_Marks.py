# TECHNIQUES USED:
# for in loop, conditionals, append, join

def remove(s, n): # s is a list, n is a counter
    result = []
    for char in s:
        if char is not "!":
            result.append(char) # add non "!" to new list
        if char is "!":
            if n is 0:
                result.append(char) # only add "!" to list if n is 0
            else:
                n = n-1 # until n is 0, don't add "!" to list but reduce n by 1
                
    answerString = ""
    answerString = answerString.join(result) # convert result list to string for return
    return answerString


# TESTS
print(remove("Hi!!", 1)) #Hi!
print(remove("!!Hi!!!", 4)) #Hi!
print(remove("!Hi!!", 1)) #Hi!!
print(remove("!!!!!Hi hi hi! hi!", 7)) #Hi hi hi hi
print(remove("Hi!!", 2)) #Hi

# Remove n exclamation marks in the sentence from left to right. n is positive integer.