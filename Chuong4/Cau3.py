#Cau3 Ham tinh BMI
def BMI(weight, height):
    return 1.0*weight/(height**2)

def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gay"
    elif bmi <= 24.9:
        return "Binh thuong"
    elif bmi <= 29.9:
        return "Hoi beo"
    elif bmi <= 34.9:
        return "Beo phi cap do 1"
    elif bmi <= 39.9:
        return "Beo phi cap do 2"
    else:
        return "Beo phi cap do 3"

def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Thap"
    elif bmi <= 24.9:
        return "Trung binh"
    elif bmi <= 29.9:
        return "Cao"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 39.9:
        return "Rat cao"
    else:
        return "Nguy hiem"
    
weight = float(input("Nhap can nang cua ban(kg): "))
height = float(input("Nhap chieu cao cua ban(m): "))
bmi = BMI(weight, height)
print("Chi so BMI: {0:.2f}, Phan loai: {1}, Nguy co benh: {2}".format(bmi, PhanLoai(bmi), NguyCoBenh(bmi)))