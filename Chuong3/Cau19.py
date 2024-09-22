# Cau 19: Tinh day so
x = int(input("Nhap gia tri x: "))
n = int(input("Nhap gia tri n: "))
s = 0
for i in range (n+1):
    tu = x ** (2*i+1)
    mau = 1
    for j in range(1,(2*i+1)+1):
        mau *= j
    s += 1.0*tu/mau
print("S({0},{1}) = {2:.2f}".format(x, n, s))