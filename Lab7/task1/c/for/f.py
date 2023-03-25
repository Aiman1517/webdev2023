a = input()
was = False
for i in range(len(a)-1, -1, -1):
    if a[i] != '0' or was:
        print(a[i], end='')
        was = True
