# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry

name = input('Please enter your name? ')
age = int(input('How old are you {}? '.format(name)))

if 18 <= age < 31:
    print("Welcome to the holiday, {}!".format(name))
else:
    print("We apologise, you can not enter")


# other way to do it
if age >= 18 and age < 31:
    print("Welcome to the holiday, {}!".format(name))
else:
    print("We apologise, you can not enter")