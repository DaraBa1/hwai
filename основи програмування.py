a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
D = b**2 - 4*a*c
print("D =", D)
if D > 0:
    print("2 корені")
elif D == 0:
    print("1 корінь")
else:
    print("Коренів немає")