done = False
items = []
while not done:
    print("Enter a to-do item, press 'enter' when done:")
    item = input()
    if item == "":
        done = True
    else:
        items.append(item)

print("Do-TO LIST:")
print("-----------")
for item in items:
    print(item)