import math


# Quadratic equation, ax**2 + bx + c = 0
# r = (-b +/- sqrt(b**2 - 4ac)) / 2a

a = input("Enter a:")
a = int(a)
b = input("Enter b:")
b = int(b)
c = input("Enter c:")
c = int(c)


sq = b**2 - 4 * a * c

if sq > 0:
    r1 = (-b + math.sqrt(sq)) / (2*a)
    r2 = (-b - math.sqrt(sq)) / (2*a)
elif sq == 0:
    # do something
    pass 
else:
    print(sq)
    re = -b / (2*a)
    im = math.sqrt(-sq) / (2*a)
    print (f"*****({re} + {im}j, {re} - {im}j)")
    r1 = complex(re, im)
    r2 = complex(re, -im)

print (f"The roots are ({r1}, {r2})")
