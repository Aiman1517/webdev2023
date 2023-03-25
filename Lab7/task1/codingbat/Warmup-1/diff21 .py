
def diff21(n):
    d = 21 - n
    if n  > 21:
       print( abs(d)*2)
    else:
        return abs(d)


# Official Solution:
# def diff21(n):
#   if n <= 21:
#     return 21 - n
#   else:
#     return (n - 21) * 2