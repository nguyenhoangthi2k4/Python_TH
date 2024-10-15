from tkinter import *
from math import sqrt
import ctypes

def giaiAction():
    a = float(entry_A.get())
    b = float(entry_B.get())
    c = float(entry_C.get())

    if a == 0:
        if b == 0 and c == 0:
            entry_KQ.insert(0, "Vô số nghiệm")
        elif b == 0 and c != 0:
            entry_KQ.insert(0, "Vô nghiệm")
        else:
                entry_KQ.insert(0, "Có nghiệm x = {0}".format(-c/b))
    else:
        dt = b*b - 4*a*c
        if dt > 0:
            x1 = (-b-sqrt(dt))/(2*a)
            x2 = (-b+sqrt(dt))/(2*a)
            entry_KQ.insert(0, f"{x1=}; {x2=}")
        elif dt == 0:
            x = -b/(2*a)
            entry_KQ.insert(0, f"{x=}")
        else:
            entry_KQ.insert(0, "Vô nghiệm")

        

def tiepAction():
    entry_A.delete(0, END)
    entry_B.delete(0, END)
    entry_C.delete(0, END)
    entry_KQ.delete(0, END)
    entry_A.focus()


def center_window(root, width, height):
    scr_width = root.winfo_screenwidth()
    scr_height = root.winfo_screenheight()
    x = scr_width//2 - width//2
    y = scr_height//2 - height//2
    root.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

    root = Tk()
    root.title("Phương trình bậc 1")
    center_window(root, 500, 300)

    Label(root, text="Giải phương trình bậc 1", font=("tohama", 16), fg="red", justify=CENTER).grid(row=0, column=1)

    Label(root, text="Hệ số a:").grid(row=1, column=0)
    entry_A = Entry(root, width=30)
    entry_A.grid(row=1, column=1)

    Label(root, text="Hệ số b:").grid(row=2, column=0)
    entry_B = Entry(root, width=30)
    entry_B.grid(row=2, column=1)

    Label(root, text="Hệ số c:").grid(row=3, column=0)
    entry_C = Entry(root, width=30)
    entry_C.grid(row=3, column=1)

    btnFrame = Frame(root)
    btnGiai = Button(btnFrame, text="Giải", command=giaiAction).grid(row=0, column=0, padx = 10)
    btnTiep = Button(btnFrame, text="Tiếp", command=tiepAction).grid(row=0, column=1)
    btnThoat = Button(btnFrame, text="Thoát", command=exit).grid(row=0, column=2, padx = 10)
    btnFrame.grid(row=4, column=1, pady=10)

    Label(root, text="Kết quả").grid(row=5, column=0)
    entry_KQ = Entry(root, width=30)
    entry_KQ.grid(row=5, column=1)

    root.mainloop()

 