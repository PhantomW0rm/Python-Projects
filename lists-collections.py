# [] square brackets
# () parenthesis
# {} curly brackets
# <> angle brackets
# < bra > ket in greek

# Creates a list and then prints a specific item from the list
listvar1 = ["meat", "veg", "cake", "beer for the weekend", 20]
#               0   1       2       3                       4
#               -4  -3      -2      -1                      0

listvar1.append("pies")
listvar1.insert(1, "pies")
listvar1.remove("veg")
listvar1.count("veg")
#counts how many things are in the list be careful with the count function
print(len(listvar1))
print(listvar1)


cool_cows = ["Winnie the moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

cool_animals = [cool_cows, cool_sheep, cool_pigs]

print(cool_animals[1][1])

listvar1.append("pies")
