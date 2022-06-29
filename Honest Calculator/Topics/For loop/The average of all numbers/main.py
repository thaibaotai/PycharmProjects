# put your python code here
a = int(input())
b = int(input()) + 1

lst = [x for x in range(a, b) if x % 3 == 0]

print(sum(lst) / len(lst))
