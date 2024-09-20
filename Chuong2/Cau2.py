# Cau 2: Tinh gio phut giay
t = int(input("Nhap so giay: "))
if t >= 0:
    hour = t // 3600
    minute = (t % 3600) // 60
    second = (t % 3600) % 60
    print(hour, minute, second, sep=":")
else: 
    print("Nhap sai roi!")