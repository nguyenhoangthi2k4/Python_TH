#Cau 6: Trich loc so am
def NegativeNumberToString(str):
    for i in range(len(str)):
        if str[i] == '-' and str[i+1].isdigit() :
            num = '-'
            i+=1
            while(str[i].isdigit()):
                num += str[i]
                i += 1
                if i >= len(str):
                    break
            print(num)

def main():
    s = str(input("Nhap vao mot chuoi: "))
    NegativeNumberToString(s)

if __name__ == '__main__':
    main()