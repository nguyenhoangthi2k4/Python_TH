# Nhap mot so n co toi da 2 chu so. Hay doc ra dang chu.
def display(n):
    if n < 0 or n > 99:
        return None
    dict_num = {1: "mot",
                2: "hai", 
                3: "ba",
                4: "bon",
                5: "nam",
                6: "sau",
                7: "bay",
                8: "tam",
                9: "chin"}
    result = dict_num[n%10]
    if n//10 > 1 :
        result = dict_num[n//10] + " muoi " + result
    elif n//10 == 1 :
        result = "Muoi " + result
    
    return result.capitalize()
    
n = int(input("Nhap so n co 2 chu so: "))
print(n , display(n), sep = " --> ")
