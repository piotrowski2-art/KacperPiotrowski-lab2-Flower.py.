def stripSpaces(myString):
    newString = ""

    for character in myString:
        if character != " ":
            newString = newString + character

    return newString

phrase = input("Enter a phrase: ")

newPhrase = stripSpaces(phrase)

print("The phrase without sapces is:", newPhrase)

    