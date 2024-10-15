from tkinter import *

def giaiAction():
    a = float(entry_A.get())
    b = float(entry_B.get())

    if a == 0:
        if b == 0:
            entry_KQ.insert(0, "Vô số nghiệm")
        else:
            entry_KQ.insert(0, "Vô nghiệm")
    else:
        entry_KQ.insert(0, "Có nghiệm x = {0}".format(-b/a))

def tiepAction():
    entry_A.delete(0, END)
    entry_B.delete(0, END)
    entry_KQ.delete(0, END)
    entry_A.focus()


def center_window(root, width, height):
    scr_width = root.winfo_screenwidth()
    scr_height = root.winfo_screenheight()
    x = scr_width//2 - width//2
    y = scr_height//2 - height//2
    root.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    root = Tk()
    root.title("Phương trình bậc 1")
    center_window(root, 350, 150)

    Label(root, text="Giải phương trình bậc 1", font=("tohama", 16), fg="red", justify=CENTER).grid(row=0, column=1)

    Label(root, text="Hệ số a:").grid(row=1, column=0)
    entry_A = Entry(root, width=30)
    entry_A.grid(row=1, column=1)

    Label(root, text="Hệ số b:").grid(row=2, column=0)
    entry_B = Entry(root, width=30)
    entry_B.grid(row=2, column=1)

    btnFrame = Frame(root)
    btnGiai = Button(btnFrame, text="Giải", command=giaiAction).grid(row=0, column=0)
    btnTiep = Button(btnFrame, text="Tiếp", command=tiepAction).grid(row=0, column=1)
    btnThoat = Button(btnFrame, text="Thoát", command=exit).grid(row=0, column=2)
    btnFrame.grid(row=3, column=1)

    Label(root, text="Kết quả").grid(row=4, column=0)
    entry_KQ = Entry(root, width=30)
    entry_KQ.grid(row=4, column=1)

    root.mainloop()

 