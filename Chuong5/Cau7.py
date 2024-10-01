#Cau 7: Toi uu chuoi
def ToiUuChuoi(s):
    s2=s
    s2=s2.strip()
    arr=s2.split(' ')
    s2=""
    for x in arr:
        word=x
        if len(word.strip())!=0:
            s2=s2+word+" "
    return s2.strip()

def main(): 
    s = "     TRần duY thAnH     "
    print(s,"=>",len(s))
    s=ToiUuChuoi(s).title()
    print(s,"=>",len(s))

if __name__ == "__main__":
    main()