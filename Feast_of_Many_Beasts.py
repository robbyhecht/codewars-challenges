# TECHNIQUES USED:
# multiple arguments, conditionals, list indices

def feast(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False


# TESTS:
print(feast("great blue heron", "garlic naan")) #True
print(feast("chickadee", "chocolate cake")) #True
print(feast("brown bear", "bear claw")) #False
print(feast("2el2", "2")) #True


# All of the animals are having a feast! Each animal is bringing one dish. There is just one rule: the dish must start and end with the same letters as the animal's name.
# Write a function feast that takes the animal's name and dish as arguments and returns true or false to indicate whether the beast is allowed to bring the dish to the feast.