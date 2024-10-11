# Cau 3 Tạo ma trận ngẫu nhiên
from random import randrange

def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))
        D.append(row)
    return D

def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element, end='\t')
        print()

def InCot(D, col):
    C = []
    for i in range(len(D)):
        C.append(D[i][col])
    return C

def MAX(D):
    max = D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if max < D[i][j]:
                max = D[i][j]
    return max


def main():
    m, n = map(int, input("Nhập m, n = ").split())
    matrix = TaoMaTran(m, n)
    
    print("Xuất ma trận: ")
    XuatMaTran(matrix)
    
    row = int(input("\nNhập dòng muốn xuất hiện row = "))
    if row-1 < m:
        print(f"Dòng {row} = ", matrix[row-1])
    else:
        print("Row không hợp lệ!")
    
    column = int(input("\nNhập cột muốn xuất hiện column = "))
    if column-1 < n:
        print(f"Cột {column} = ", InCot(matrix, column - 1))
    else:
        print("Row không hợp lệ!")

    print("\nMax = ", MAX(matrix))


if __name__ == "__main__":
    main()