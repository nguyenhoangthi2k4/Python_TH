# Cau 14. In ra bao nhieu dau *
a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a+b) % 2 == 0:
            print("*",end="")
        b += 1
    a += 1
print()

# In ra 2000 dau *. Do moi lan lap se in ra 20 dau *, ma co 100 lan lap => in ra 2000 dau *