#Cau 2 Tro choi doan so
from random import randrange

def game():
    while True:
        somay  = randrange(1, 101)
        solan = 1
        win = False
        while solan <= 7:
            doan = int(input("\nMay doan tu [1, 100], moi ban doan: "))
            print("Ban doan la thu",solan)
            if doan == somay:
                print("Chuc mung ban da doan dung, so may la:",somay)
                print("\a")
                win = True
                break
            elif doan < somay:
                print("Ban doan sai, so may > so ban")
            else:
                print("Ban doan sai, so may < so doan")
            solan += 1
        if win == False:
            print("-->Game over, so may la:",somay)
            print("\a")
        hoi = input("Tiep tuc: ")
        if hoi == 'k':
            print("Thanhks")
            break
game()