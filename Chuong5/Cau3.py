#Cau 3: Xuat chuoi theo yeu cau
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def main():
    s = '5;7;8;-2;8;11;13;9;10'
    # s = input() Nhap vao moi chuoi

    sochan = snt = soam = sum = 0
    arr = s.split(';')
    for x in arr:
        num = int(x)
        print(num)
        if isPrime(num) : snt += 1
        if num % 2 == 0 : sochan += 1
        if num < 0 : soam += 1
        sum += num
    print(f"Co {sochan} so chan")
    print(f"Co {soam} so am")
    print(f"Co {snt} so nguyen to")
    print(f"Gia tri trung binh = {sum/len(arr):.2f}")
            
if __name__ == "__main__":
    main()