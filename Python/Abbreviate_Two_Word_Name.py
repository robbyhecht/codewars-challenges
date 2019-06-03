# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot seperating them.
# It should look like this:
# Sam Harris => S.H  Patrick Feeney => P.F


def abbrevName(name):
    name = name.upper() #capitalize
    initialF = name[0] #initial 1
    spaceIndex = name.index(" ") #find index of space
    initialL = name[spaceIndex + 1] #initial 2
    return initialF + "." + initialL


print(abbrevName("Sam Harris")); #"S.H"
print(abbrevName("patrick Feenan")); #"P.F"
print(abbrevName("Evan cole")); #"E.C"
print(abbrevName("P Favuzzi")); #"P.F"
print(abbrevName("david mendieta")); #D.M"