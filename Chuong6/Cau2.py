# Cau 2 Xử lí list nhập ngẫu nhiên
from random import randrange

def checkDoiXung(lst):
    for i in range(len(lst)):
        if lst[i] != lst[len(lst)-1-i]:
            return False
    return True

def main():
    n = int(input("Nhập số phần tử n = "))
    lst = []
    for i in range(n):
        lst.append(randrange(-100, 100))

    print("List = ",lst)

    k = int(input("Nhập giá trị k cần xóa: "))
    while lst.count(k) > 0:
        lst.remove(k)

    print(f"List sau xóa {k} = ", lst)

    if checkDoiXung(lst):
        print("List đối xứng")
    else:
        print("List không đối xứng")

if __name__ == "__main__":
    main()
