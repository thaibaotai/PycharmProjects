A = int(input())
B = int(input())
C = int(input())
X = int(input())
Y = int(input())
box = sorted([A, B, C])
door = sorted([X, Y])

if box[0] <= door[0] and box[1] <= door[1]:
    print("The box can be carried")
elif box[1] <= door[0] and box[2] <= door[1]:
    print('The box can be carried')
else:
    print('The box cannot be carried')
