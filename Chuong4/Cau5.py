# Cau 5 Tinh day Fibonacci
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def DayFibo(n):
    print("Day fibonacci tu [1, %d]" %n)
    for i in range(1, n+1):
        print(fibonacci(i), end=" ")

n = int(input("Nhap so nguyen n: "))
print("So fibonacci thu %d la %d" %(n, fibonacci(n)))
DayFibo(n)