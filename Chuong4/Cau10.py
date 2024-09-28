# Cau 10 Ve hinh dung Sleep
import time
def Hinh1(n):
    mid = n//2
    for i in range(n):
        for j in range(n):
            if i <= mid:
                if (mid <= j and j <= mid+i) or i == mid:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            else:
                if j < n-i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()
                
def Hinh2(n):
    mid = n//2
    for i in range(n):
        for j in range(n):
            if i <= mid:
                if j == mid or j == mid+i or i == mid:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            else:
                if j == 0 or j == (n-1) - i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()

def Hinh3(n):
    mid = n // 2
    for i in range(n):
        for j in range(n):
            if i <= mid:
                if j >= mid and j < n-i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            else:
                if j <= mid and j >= (n-i)-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()

def Hinh4(n):
    mid = n // 2
    for i in range(n):
        for j in range(n):
            if (i+j == n-1) or j == mid or (i==0 and j>mid) or (i==n-1 and j<mid):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

n = int(input("Nhap so nguyen n: "))
Hinh1(n)
print()
time.sleep(5)

Hinh2(n)
print()
time.sleep(5)

Hinh3(n)
print()
time.sleep(5)

Hinh4(n)


