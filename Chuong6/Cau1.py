# Câu 1: Xử lý list
import random
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def main():
    # Khởi tạo list
    print("Khởi tạo list")
    n = int(input("Nhập chiều dài list n = "))
    ls = [0]*n
    for i in range(n):
        ls[i] = random.randrange(-100, 100)
    print("List ngẫu nhiên:", ls)

    # Nhập thêm phần tử mới
    x = int(input("Nhập thêm phần tử mới = "))
    ls.append(x)
    
    # Đếm phần tử k trong list
    dem = 0
    k = int(input("Phần tử muốn tìm k = "))
    print(f"Co {ls.count(k)} phần tử '{k}' trong list")
    
    # Tính tổng các số nguyên tố
    sum = 0
    for i in ls:
        if isPrime(i):
            sum += i
    print("Tổng các số nguyên tố trong list = ", sum)

    # Sắp xếp
    ls.sort()
    print("List sau sắp xếp: ", ls)

    # Xóa list
    ls.clear()
    print("List sau khi xóa: ",ls)

if __name__ == "__main__":
    main()