"""
Cau17: Nhap lai code chuyen bien done sang dung break
Code mau:
done = False
n, m = 0, 100
while not done and n != m:
    n = int(input())
    if n < 0:
        done = True
    print("n = ", n)
"""
n, m = 0, 100
while n != m:
    n = int(input())
    if n < 0:
        break
    print("n = ", n)