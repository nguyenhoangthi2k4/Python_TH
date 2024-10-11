# Câu 10: Xử lý ma trận
"""
Nhập 2 matrix A, B.
Cộng 2 matrix
Viết hàm tính matrix hoán vị➔áp dụng để tìm cho A, B
"""
def nhapMaTran():
    n, m = map(int, input("Nhập hàng cột của ma trận: ").split())
    M = []
    for i in range(n):
        R = []
        for j in range(m):
            tmp = int(input(f"Nhập phần tử a[{i+1}][{j+1}] = "))
            R.append(tmp)
        M.append(R)
    return M

def inMaTran(Matrix):
    for row in Matrix:
        for element in row:
            print(element, end="\t")
        print()

def congMaTran(A, B):
    M = []
    if (len(A) == len(B) and len(A[0]) == len(B[0])):
        for i in range(len(A)):
            R = []
            for j in range(len(A[i])):
                tmp = A[i][j] + B[i][j]
                R.append(tmp)
            M.append(R)
    return M

def hoanVi(Matrix):
    M = []
    if(len(Matrix) == len(Matrix[0])):
        for i in range(len(Matrix)):
            R = []
            for j in range(len(Matrix[i])):
                R.append(Matrix[j][i])
            M.append(R)
    return M
               


def main():
    # Nhập 2 ma trận
    print("Nhập ma trận A")
    A = nhapMaTran()

    print("Nhập ma trận B")
    B = nhapMaTran()

    # In ma trận
    print("\nMa Trận A:")
    inMaTran(A)

    print("\nMa Trận B:")
    inMaTran(B)

    # Tổng 2 ma trận
    C = congMaTran(A, B)
    print("\nTổng 2 ma trận:")
    inMaTran(C)
    
    # Hoán vị
    print("\nHoán vị A")
    hvA = hoanVi(A)
    inMaTran(hvA)

    print("\nHoán vị B")
    hvB = hoanVi(B)
    inMaTran(hvB)

if __name__ == '__main__':
    main()
   