# Cau 9 Tinh can bac 2 long nhau
from math import sqrt
def TinhCan2(n):
    if n == 1:
        return sqrt(2)
    if n > 1:
        return sqrt(2 + TinhCan2(n-1))

n = int(input("Nhap so nguyen n: "))
if n > 0:
    print("S({}) = {}".format(n, TinhCan2(n)))
else:
    print("Nhap khong hop le")