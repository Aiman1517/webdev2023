def power(a, b):
    x = 1
    for i in range(b):
        x *= a
    return x
a, b = input().split()
print(power(float(a), int(b)))