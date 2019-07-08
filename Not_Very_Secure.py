# TECHNIQUES USED:
# conditionals, isalpha, isdigit, isalnum, for loop

def alphanumeric(string):
    """
    Checks each character to see if it's either a letter or number
    If so, continues to next char
    If all qualify, returns True
    """
    for char in string:
        if char.isalpha() or char.isdigit():
            continue
        else:
            return False
    return True

#another solution:
# return string.isalnum()


# tests:
print(alphanumeric("hello_world")) #False
print(alphanumeric("PassW0rd")) #True
print(alphanumeric("     ")) #False
print(alphanumeric("a")) #True




# In this example you have to validate if a user input string is alphanumeric. The given string is not nil, so you don't have to check that.
# The string has the following conditions to be alphanumeric:
  # At least one character ("" is not valid)
  # Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
  # No whitespaces/underscore