#Cau 13 Kiem tra so hoan thien, so thinh vuong
def TongUoc(n):
    s_uoc = 0
    for i in range(1, (n//2)+1):
        if n%i == 0:
           s_uoc += i
    return s_uoc
# Kiem tra so hoan hao (Tong cac uoc bang chinh no)
def IsPerfectNumber(sum, n):
    if sum == n:
        return True
    else:
        return False
    
# Kiem tra so thinh vuong (Tong cac uoc lon hon no)
def IsAbundantNumber(sum, n):
    if sum > n:
        return True
    else:
        return False
    
def main():
    while True:
        n = int(input("Nhap so nguyen n: "))
        if n > 0: 
            break

    sum = TongUoc(n)
    if IsPerfectNumber(sum, n) :
        print(f"{n} la so hoan thien")
    else:
        print(f"{n} khong la so hoan thien")

    if IsAbundantNumber(sum, n) :
        print(f"{n} la so thinh vuong")
    else:
        print(f"{n} khong la so thinh vuong")

main()
