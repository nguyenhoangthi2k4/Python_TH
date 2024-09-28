#Cau 7 Tinh do dai canh AB
from math import sqrt
def KhoangCach(xa, ya, xb, yb):
    return sqrt((xb - xa)**2 + (yb - ya)**2)

xa, ya = map(int, input("Nhap toa do A: ").split())
xb, yb = map(int, input("Nhap toa do B: ").split())
print("Khoang cach AB = %.2f" %KhoangCach(xa, ya, xb, yb))