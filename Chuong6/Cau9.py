# Câu 9: Xử lý mảng
'''
Viết chương trình nhập vào một mảng số tự nhiên. Hãy xuất ra màn hình:
- Dòng 1 : gồm các số lẻ, tổng cộng có bao nhiêu số lẻ.
- Dòng 2 : gồm các số chẵn, tổng cộng có bao nhiêu số chẵn.
- Dòng 3 : gồm các số nguyên tố.
- Dòng 4 : gồm các số không phải là số nguyên tố.
'''

def taoMang(lst):
    n = int(input("Nhập số phần tử n = "))
    for i in range(n):
        tmp = int(input(f"Nhập phần tử a[{i+1}] = "))
        lst.append(tmp)

def soLe(lst):
    ls = [x for x in lst if(x%2==1)]
    return ls

def soChan(lst):
    ls = [x for x in lst if(x%2==0)]
    return ls

def ktSoNT(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def soNguyenTo(lst):
    ls = [x for x in lst if ktSoNT(x)]
    return ls

def koSoNguyenTo(lst):
    ls = [x for x in lst if ktSoNT(x)==False]
    return ls
    
def main():
    lst = []
    taoMang(lst)
    print(soLe(lst),"--> Gồm có:",len(soLe(lst)))
    print(soChan(lst),"--> Gồm có:",len(soChan(lst)))
    print(soNguyenTo(lst),"--> Gồm có:",len(soNguyenTo(lst)))
    print(koSoNguyenTo(lst),"--> Gồm có:",len(koSoNguyenTo(lst)))

if __name__ == '__main__':
    main()
