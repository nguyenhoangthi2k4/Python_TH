# Câu 6 Nhập vào 1 list ngẫu nhiên không trùng nhau
from random import randrange
def taoMang(lst):
    n = int(input("Nhập số phần tử n = "))
    i = 0
    while(i<n):
        tmp = randrange(100)
        if tmp not in lst: 
            lst.append(tmp)
            i += 1

def inMang(lst):
    for i in lst:
        print(i, end=" ")

def main():
    lst = []
    print('List các phần tử ngẫu nhiên không trùng nha')
    taoMang(lst)
    inMang(lst)
    
if __name__ == "__main__":
    main()

