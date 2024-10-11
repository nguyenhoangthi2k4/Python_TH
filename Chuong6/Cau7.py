# Câu 7: Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai
# quy cách thì yêu cầu nhập lại. In dãy số sau khi đã nhập xong
def taoMang(lst):
    n = int(input("Nhập số phần tử n = "))
    tmp = int(input("Nhập phần tử a[1] = "))
    lst.append(tmp)
    i = 1
    while i < n:
        tmp = int(input(f"Nhập phần tử a[{i+1}] = "))
        if tmp >= lst[i-1]:
            lst.append(tmp)
            i += 1

def inMang(lst):
    print("Mảng vừa nhập:",lst)

def main():
    lst = []
    taoMang(lst)
    inMang(lst)

if __name__ == "__main__":
    main()