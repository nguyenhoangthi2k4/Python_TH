# Tinh chu vi, dien tich hinh tron
from math import *

try:
    r = float(input("Nhap ban kinh r: "))

    if r < 0: 
        raise Exception
    
    cv = 2 * pi * r
    dt = pi * r * r
    print("Chu vi: %.2f" %cv, "Dien tich: %.2f" %dt)
except :
    print("Nhap sai gia tri r")