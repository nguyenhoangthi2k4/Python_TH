#Cau 12
def Display():
    n = 3
    tmp = " "
    for i in range(-3, 5):
        tmp = tmp + str(i) + " " + str(n) + " "
        n -= 1
        
    return tmp
        
       

def main():
    print(Display())

if __name__ == "__main__":
    main()