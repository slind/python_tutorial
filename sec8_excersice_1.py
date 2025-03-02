def print_dictionary(dict):
    for key, value in dict.items():
        print("{0}: {1}".format(key, value))

people = {"Jeff":"Is affraid of clowns","Peter":"Can fly an airplane.", "John":"Is very tall"}

print_dictionary(people)

print()
people["Jeff"] = "Is affraid of hights"
people["Jill"] = "Is a great dancer."
print_dictionary(people)
