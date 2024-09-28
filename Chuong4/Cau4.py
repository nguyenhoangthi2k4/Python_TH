#Cau 4 Tinh ti le ROI
def ROI(dt, cp):
    return (dt-cp)/cp

def GoiYDauTu(roi):
    if roi < 0.75:
        return "Khong nen dau tu"
    else:
        return "Nen dau tu"
    
cp = float(input("Chi phi dau tu: "))
dt = float(input("Doanh thu: "))
roi = ROI(dt, cp)
print("Ty le ROI: %.2f" %roi)
print("==>",GoiYDauTu(roi))