# Câu 8: Viết chương trình nhập vào một dãy n số thực M[0], M[1],..., M[n-1], sắp xếp
# dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp
def taoMang(lst):
    n = int(input("Nhập số phần tử n = "))
    for i in range(n):
        tmp = float(input(f"Nhập phần tử a[{i+1}] = "))
        lst.append(tmp)
    
def inMangSX(lst):
    lst.sort(reverse = True)
    print("List được sắp xếp giảm:", lst)



def main():
    lst = []
    taoMang(lst)
    inMangSX(lst)

if __name__ == '__main__':
    main()