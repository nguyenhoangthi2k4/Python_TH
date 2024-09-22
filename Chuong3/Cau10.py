#Cau 10: Tinh day so
x = int(input("Nhap gia tri x: "))
n = int(input("Nhap gia tri n: "))
s = 0
for i in range(1, n+1):
    tu = x ** i
    mau = 1
    for j in range(1, i+1):
        mau *= j
    s += 1.0*tu/mau
print("S({0}, {1}) = {2:.2f}".format(x,n,s))