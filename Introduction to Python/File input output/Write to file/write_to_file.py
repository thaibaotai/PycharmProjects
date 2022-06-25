zoo = ["lion", "elephant", "monkey"]
number = 15

with open("output.txt", 'a') as f:
    # On a new line in  "output.txt", add all elements from the zoo list, joined by " and "
    # Add the number to the output as well
    f.write('\n' + ' and '.join(zoo))
    f.write('\n' + str(number))

