#Cau 8 Viet chuong trinh tinh loga(x)
import math
print("Chuong trinh tinh loga(x)")
a = x = 0
while True:
    a = float(input("Nhap co so a(a>1): "))
    x = float(input("Nhap x (x>0): "))
    if a <= 1 or x <= 0:
        print("Nhap khong chinh xac\n")
    else:
        break
print("Gia tri log{}({}) = {:.2f}".format(a, x, math.log(x,a)))
