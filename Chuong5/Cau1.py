#Cau 1 Kiem tra chuoi doi xung
def checkDoiXung(s):
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i] :
            return False
    return True

def main():
    s = input("Nhap 1 chuoi: ")
    if checkDoiXung(s):
        print(f"{s} la chuoi doi xung")
    else:
        print("{} khong la chuoi doi xung".format(s))

if __name__ == "__main__":
    while True:
        main()
        choose = input("Tiep tuc khong (c/k): ")
        if choose == 'k':
            break