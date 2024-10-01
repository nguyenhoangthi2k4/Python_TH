def dem(str_input):
    inHoa = inThuong = chuSo = kyTuDB = khoangTrang = nAm = pAm = 0
    for i in str_input:
        if i.isalpha():
            if i.isupper():
                inHoa += 1
            else:
                inThuong += 1
            if i in ('a', 'e', 'i', 'o', 'u'):
                nAm += 1
            else:
                pAm += 1
        elif i.isdigit():
            chuSo += 1
        elif i.isspace():
            khoangTrang += 1
        else:
            kyTuDB += 1  
    print(f"Co {inHoa} in hoa") 
    print(f"Co {inThuong} in thuong") 
    print(f"Co {chuSo} chu so") 
    print(f"Co {kyTuDB} ky tu dac biet") 
    print(f"Co {khoangTrang} khoang trang") 
    print(f"Co {nAm} in hoa") 
    print(f"Co {pAm} in hoa") 

str_input = input("Nhap 1 chuoi: ")
dem(str_input)

