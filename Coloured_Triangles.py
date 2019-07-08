# TECHNIQUES USED:
# len, conditional, range, append

def triangle(row):
    if len(row) == 1:
        return row  #satisfy the situation of having only one letter
    elif len(row) > 1:
        def newLetter(l1, l2): #define new letter creation
            if l1 == "G" and l2 == "B" or l1 == "B" and l2 == "G":
                return "R"
            elif l1 == "G" and l2 == "R" or l1 == "R" and l2 == "G":
                return "B"
            elif l1 == "B" and l2 == "R" or l1 == "R" and l2 == "B":
                return "G"
            else: return l1
        resultingRow = [] #make empty list for next row of letters
        for i in range(len(row)-1): #loop through letters by index and append created letters to next row
            resultingLetter = newLetter(row[i], row[i+1])
            resultingRow.append(resultingLetter)
        # print(resultingRow)
        answer = triangle(resultingRow) #repeat working through rows until only one letter remains
        return answer[0]


# TESTS
print(triangle('GB')) #'R'
print(triangle('RRR')) #'R'
print(triangle('RGBG')) #'B'
print(triangle('RBRGBRB')) #'G'
print(triangle('RBRGBRBGGRRRBGBBBGG')) #'G'
print(triangle('B')) #'B'


# A coloured triangle is created from a row of colours, each of which is red, green or blue. Successive rows, each containing one fewer colour than the last, are generated by considering the two touching colours in the previous row. If these colours are identical, the same colour is used in the new row. If they are different, the missing colour is used in the new row. This is continued until the final row, with only a single colour, is generated.

# The different possibilities are:

# Colour here:        G G        B G        R G        B R
# Becomes colour:      G          R          B          G
# With a bigger example:

# R R G B R G B B
#  R B R G B R B
#   G G B R G G
#    G R G B G
#     B B R R
#      B G R
#       R B
#        G
# You will be given the first row of the triangle as a string and its your job to return the final colour which would appear in the bottom row as a string. In the case of the example above, you would the given RRGBRGBB you should return G.

# The input string will only contain the uppercase letters R, G, B and there will be at least one letter so you do not have to test for invalid input.
# If you are only given one colour as the input, return that colour.