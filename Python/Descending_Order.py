# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.


def Descending_Order(num):
  num = str(num)  #make number into a string (integers are not iterable)
  num = sorted(num, reverse=True)  #sort digits and reverse
  num = "".join(num)  #join digits together
  num = int(num)  #turn string back into integer
  return(num)


# tests:

print(Descending_Order(0)) #0
print(Descending_Order(15)) #51
print(Descending_Order(123456789)) #987654321