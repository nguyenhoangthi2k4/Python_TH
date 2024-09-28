#Cau 1 Viet ham tinh dien tich tam giac
from math import *

def ktHopLe(a, b, c):
    if (a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a):
        return False
    return True

def tinhDT(a, b, c):
    p = (a + b + c) / 2
    dt = sqrt(p * (p-a) * (p-b) * (p-c))
    return dt

a, b, c = map(int, input("Nhap do dai 3 canh: ").split())
if(ktHopLe(a, b, c)):
    dt = tinhDT(a, b, c)
    print("Dien tich hinh tam giac = %.2f" %dt)
else:
    print("Nhap do dai khong hop le")