import math
n = int(input())
i = 1
while(i <= n):
    x = int(math.sqrt(i))
    if i == x*x :
        print(i)
    i += 1