# TECHNIQUES USED:
# multiple arguments, sum, len, ternary

def better_than_average(class_points, your_points):
    avg = (sum(class_points) + your_points) / (len(class_points) + 1)
    return True if your_points > avg else False


# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You got an array with your colleges' points. Now calculate the average to your points!
# Return True if you're better, else False!

# [8]