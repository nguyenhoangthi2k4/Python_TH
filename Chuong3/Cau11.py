#Cau 11: Kiem tra so nguyen to
import math

while True:
    n = int(input("Nhap so nguyen n: "))
    dem = 0
    # Kiem tra so nguyen to
    for i in range(1, n+1):
        if n % i == 0:
            dem += 1
    if dem == 2:
        print(n,"la so nguyen to")
    else:
        print(n,"khong la so nguyen to")
    
    choose = input("Tiep tuc c/k: ")
    if choose == 'k':
        break