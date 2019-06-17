# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of the locations and the values being
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code.
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a mall brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house, for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}  # this is a dictionary

# exits = [{"Q": 0},
#          {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          {"N": 5, "Q": 0},
#          {"W": 1, "Q": 0},
#          {"N": 1, "W": 2, "Q": 0},
#          {"W": 2, "S": 1, "Q": 0}]  # this is a list of dictionaries, doesn't suit a large scale usage

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}  # this is a dictionary of dictionaries

namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "WEST": "W",
              "EAST": "E"}  # used to expand accepted inputs from the player

# print(locations[0].split())
# # print(locations[3].split(","))
# # print(' '.join(locations[0].split()))  # using split to segment data, and then reconstructing it

loc = 1
while True:

    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "  # not a good idea to do it this way

    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    # Parse user input using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than one letter, so check vocabulary
        # for word in vocabulary:  # does it contain a word we know?
        #     if word in direction:
        #         direction = vocabulary[word]  # this is how it would be done without split function
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")
