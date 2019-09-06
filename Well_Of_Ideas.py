# TECHNIQUES USED:
# for loop, conditionals
# * could also use 'count' method

def well(x):
  count = 0
  for word in x:
    if word is "good":
      count += 1
  if count == 0:
    return "Fail!"
  elif count <= 2:
    return "Publish!"
  else: return "I smell a series!"


# You need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.