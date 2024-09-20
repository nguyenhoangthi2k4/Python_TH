#Cau 3: Tinh diem trung binh
toan, ly, hoa = map(float, input("Nhap diem Toan, Ly, Hoa: ").split())
print("Diem Toan =", toan)
print("Diem Ly =", ly)
print("Diem Hoa =",hoa)
dtb = (toan + ly + hoa)/3
print("Diem trung binh:", dtb)
print("Diem trung binh:", round(dtb, 2))