# Tinh phuong trinh bac 2
from math import *
a, b, c = map(int, input("Nhap a, b, c: ").split())

if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh co vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co nghiem:", -c/b)
else:
    detal = b*b - 4*a*c
    if detal > 0:
        print("x1 =", (-b-sqrt(detal))/(2*a))
        print("x2 =", (-b+sqrt(detal))/(2*a))
    elif detal == 0:
        print("x =", -b/(2*a))
    else:
        print("Phuong trinh vo nghiem")