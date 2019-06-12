# add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as we did in lines 5-13

menu = [["egg", "spam", "bacon"], ["egg", "sausage", "bacon"], ["egg", "carrot"], ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"], ["spam", "bacon", "sausage", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"], ["spam", "egg", "sausage", "spam"]]

# print(menu)

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)

print("=" * 50)

# more informative way
avoid = "spam"
ingredientNo = 1

for meal in menu:
    if avoid not in meal:
        print("Meal #{} on the menu doesn't contain {}.".format(menu.index(meal)+1, avoid, meal))
        ingredientNo = 1
        for ingredient in meal:
            print("Ingredient #{} is {}.".format(ingredientNo, ingredient))
            ingredientNo += 1

