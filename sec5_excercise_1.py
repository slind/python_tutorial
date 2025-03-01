print("How would you like to travel in kilometers?")
distance = int(input());
if distance < 5:
    print("I suggest walking to your destination.")
elif distance < 500:
    print("I suggest driving to your destination.")
else:
    print("I suggest flying to your destination.")