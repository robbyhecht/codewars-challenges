# TECHNIQUES USED:
# multiple arguments, ratios

'''
find the total remaining blue and divide by the total remaining marbles
'''
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    blue = blue_start - blue_pulled
    red = red_start - red_pulled
    total = blue + red
    return blue/total


# You have a bunch of red and blue marbles. To start the game you grab a handful of marbles of each color and put them into the bag, keeping track of how many of each color go in. You take turns reaching into the bag, guessing a color, and then pulling one marble out. You get a point if you guessed correctly. The trick is you only have three seconds to make your guess, so you have to think quickly.

# You've decided to write a function, guessBlue() to help automatically calculate whether you should guess "blue" or "red". The function should take four arguments:

# the number of blue marbles you put in the bag to start
# the number of red marbles you put in the bag to start
# the number of blue marbles pulled out so far, and
# the number of red marbles pulled out so far.