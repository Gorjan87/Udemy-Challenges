# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

# creating an empty list and adding items in it with append function, one by one
randomNumbers = []

randomNumbers.append(2)
randomNumbers.append(66)
randomNumbers.append(24)
randomNumbers.append(44)
randomNumbers.append(73)
randomNumbers.append(12)
randomNumbers.append(21)
randomNumbers.append(99)


# sorted list of numbers
print(sorted(randomNumbers))
print('=' * 32)


# for loop going through unsorted list of numbers, using iter function
for number in iter(randomNumbers):
    print(number)
print('===============================')


# here, variable is the last member of the list itself
print(number)
print('===============================')


# challenge 4
myIterator = iter(randomNumbers)

for number in range(len(randomNumbers)):
    print(next(myIterator))
print('===============================')

# here, variable represents list maximum index, which goes from 0 to 7 in this case.
print(number)
