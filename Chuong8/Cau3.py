from tkinter import *
import ctypes

def center_window(root, width, height):
    srceen_width = root.winfo_screenwidth()
    srceen_height = root.winfo_screenheight()
    x = srceen_width//2 - width//2
    y = srceen_height//2 - height//2
    root.geometry(f"{width}x{height}+{x}+{y}")

def congAction():
    a = float(soA.get())
    b = float(soB.get())
    ketQua.set(f"{a} + {b} = {a+b}")

def truAction():
    a = float(soA.get())
    b = float(soB.get())
    ketQua.set(f"{a} - {b} = {a-b}")

def nhanAction():
    a = float(soA.get())
    b = float(soB.get())
    ketQua.set(f"{a} * {b} = {a*b}")

def chiaAction():
    a = float(soA.get())
    b = float(soB.get())
    ketQua.set(f"{a} / {b} = {a/b:.2f}")

if __name__ == "__main__":
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    root = Tk()
    root.title("Cộng trừ nhân chia")
    center_window(root, 800, 400)

    soA = StringVar()
    soB = StringVar()
    ketQua = StringVar()

    Label(root, text="CỘNG TRỪ NHÂN CHIA", font=("",15), justify=CENTER, fg="blue").grid(row=0, columnspan=2)

    btnFrame = Frame(root)
    Button(btnFrame, text="Cộng",command=congAction, fg = "red", width=10, relief="sunken", font=("",13), anchor="center").pack(side=TOP, pady=10)
    Button(btnFrame, text="Trừ",command=truAction, fg = "red", width=10, relief="sunken", font=("",13), anchor="center").pack(side=TOP, pady=10)
    Button(btnFrame, text="Nhân",command=nhanAction, fg = "red", width=10, relief="sunken", font=("",13), anchor="center").pack(side=TOP, pady=10)
    Button(btnFrame, text="Chia",command=chiaAction, fg = "red", width=10, relief="sunken", font=("",13), anchor="center").pack(side=TOP, pady=10)
    btnFrame.grid(rowspan=4, column=0)

    Label(root, text="Hệ số a:").grid(row=1, column=2)
    Entry(root, textvariable=soA).grid(row=1, column=3)

    Label(root, text="Hệ số b:").grid(row=2, column=2)
    Entry(root, textvariable=soB).grid(row=2, column=3)

    Label(root, text="Kết quả:").grid(row=3, column=2)
    Entry(root, textvariable=ketQua).grid(row=3, column=3)

    Button(root, text="Thoát", fg = "red", width=10, relief="sunken", font=("",13), anchor="center", command=exit).grid(row=4, column=3, sticky="e")

    root.mainloop()