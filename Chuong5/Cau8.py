#Cau 8: Tach ten bai hat
def TachChamMp3(link):
    ten = link.split("\\")[-1]
    return ten

def TachTen(link):
    ten = link.split("\\")[-1].split(".")[0]
    return ten


def main():
    link = input("Nhan duong dan: ")
    print("Ten bai hat:", TachTen(link))
    print("Ten bai hat.mp3:", TachChamMp3(link))


if __name__ == "__main__":
    main()