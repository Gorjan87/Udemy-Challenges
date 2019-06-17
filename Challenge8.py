# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

text = input("Please enter your text here: ")

consonants = set()  # using a set here will disable double entries of characters

for char in text:
    if char not in "AEIOUaeiou":  # we could add an empty space character to this so its not added to a set
        consonants.add(char)

print(sorted(consonants))


# other way to do it
text2 = set(input("Please enter your text here"))

vowels2 = frozenset("AEIOUaeiou")
# vowels2 = {"a", "e", "i", "o", "u"}
consonantsSet = set(text2).difference(vowels2)  # by taking frozen set out of text2 variable, we remove all vowels

print(sorted(consonantsSet))
