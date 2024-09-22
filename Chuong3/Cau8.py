# Cau 8: Nhap vao 2 gia tri a, b va phep toan +, -, *, /. Xuat ket qua
a, b = map(int, input("Nhap 2 gia tri a, b: ").split())
c = input("Nhap phep toan (+, -, *,/): ")
match c:
    case '+': 
        print("{} + {} = {}".format(a, b, a+b))
    case '-': 
        print("{} - {} = {}".format(a, b, a-b))
    case '*': 
        print("{} * {} = {}".format(a, b, a*b))
    case '/': 
        print("{} / {} = {}".format(a, b, a/b))
    case __:
        print("Nhap khong hop le")