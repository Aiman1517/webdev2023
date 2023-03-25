a = int(input())
b = int(input())
if a % 2 == 1:
    a += 1
b += 1
for i in range(a, b, 2):
    print(i, end=' ')