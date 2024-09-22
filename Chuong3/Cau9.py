#Cau 9. Nhap vao 1 thang xuat ra thang do thuoc quy nao
month = int(input("Nhap vao 1 thang: "))
if month > 0 and month <= 12:
    if month <= 3:
        print("Thang",month,"thuoc quy I")
    elif month > 3 and month <= 6:
        print("Thang",month,"thuoc quy II")
    elif month > 6 and month <= 9:
        print("Thang",month,"thuoc quy III")
    elif month > 9 and month <= 12:
        print("Thang",month,"thuoc quy IV")
else:
    print("Nhap khong hop le")
        