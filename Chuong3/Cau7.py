def ktNamNhuan(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

def ktHopLe(day, month, year):
    if month > 12:
        return False
    if month in (1, 3, 5, 7, 8, 10, 12) and day > 31:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if month == 2 and (not ktNamNhuan(year) and day > 28) or (ktNamNhuan(year) and day > 29):
        return False
    return True

def ngayHomSau(day, month, year):
    if month in (1, 3, 5, 7, 8, 10) and day > 31:
        day = 1
        month += 1
    elif month in (4, 6, 9, 11) and day > 30:
        day = 1
        month += 1
    elif month == 2 and (not ktNamNhuan(year) and day > 28) or (ktNamNhuan(year) and day > 29):
        day = 1
        month += 1
    elif month == 12 and day == 31: #Ngay 31/12/year
        day = 1
        month = 1
        year += 1
    else:
        day += 1
        
    result = "{}/{}/{}".format(day, month, year)
    return result

day, month, year = map(int, input("Nhap ngay thang nam: ").split())
if(ktHopLe(day, month, year)):
    print("Ngay hom sau la: ", ngayHomSau(day, month, year))
else:
    print("Nhap ngay khong hop le")

