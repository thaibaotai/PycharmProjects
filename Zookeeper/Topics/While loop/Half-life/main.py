ini = int(input())
final = int(input())
count = 0

while ini > final:
    count += 1
    ini //= 2

print(count * 12)