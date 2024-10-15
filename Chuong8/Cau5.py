from tkinter import *
from tkinter import messagebox
import ctypes

loginName = "thi"
passWord = "123"

def update_Pass():
    global passWord
    if(strLoginName.get() == loginName and strPass.get() == passWord):
        if(strNewPass.get() == strNewPassAgain.get()):
            passWord = strNewPass.get()
            close_frmRePass()
        else:
            messagebox.showerror("Error", "Enter new password is not correct")
    else:
        messagebox.showerror("Error", "Login name or password is not conrrect")
        

def open_frmRePass():
    global frmRePass
    frmMain.withdraw()
    frmRePass = Toplevel()
    frmRePass.title("Enter new password")
    center_window(frmRePass, 500, 250)
    frmRePass.resizable(False, False)

    frmRePass.grid_columnconfigure(0, weight=1)
    frmRePass.grid_columnconfigure(1, weight=1)

    Label(frmRePass, text="Login name:", font = ("",10)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    Entry(frmRePass, textvariable=strLoginName).grid(row=0, column=1)

    Label(frmRePass, text="Old PassWord", font = ("",10)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    Entry(frmRePass, textvariable=strPass, show="*").grid(row=1, column=1, padx= 10)

    Label(frmRePass, text="New Password:", font = ("",10)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    Entry(frmRePass, textvariable=strNewPass, show="*").grid(row=2, column=1, padx= 10)

    Label(frmRePass, text="Enter New Password:", font = ("",10)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    Entry(frmRePass, textvariable=strNewPassAgain, show="*").grid(row=3, column=1, padx= 10)

    btnFrame = Frame(frmRePass)
    Button(btnFrame, text="Ok", anchor="center", font=("",9), width=10, relief="groove", command=update_Pass).pack(side=LEFT, padx=10)
    Button(btnFrame, text="Cancel", anchor="center", font=("",9), width=10, relief="groove", command=close_frmRePass).pack(side=RIGHT, padx=10)
    btnFrame.grid(row=4, columnspan=2)

def close_frmRePass():
    frmRePass.destroy()
    frmMain.deiconify()

def signIn():
    if(strLoginName.get() == loginName and strPass.get() == passWord):
        strLoginName.set("")
        strPass.set("")         
        messagebox.showinfo("Confirm", "Login success")
    else:
        messagebox.showerror("Error", "Login name or password is not conrrect")

def center_window(root, w, h):
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = screen_w//2 - w//2
    y = screen_h//2 - h//2
    root.geometry(f"{w}x{h}+{x}+{y}")

if __name__ == "__main__":
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    frmMain = Tk()
    frmMain.title("Sign In")
    center_window(frmMain, 450, 250)

    strLoginName = StringVar()
    strPass = StringVar()
    strNewPass = StringVar()
    strNewPassAgain = StringVar()

    # frmMain
    Label(frmMain, text="Log in",font = ("",15), fg="red", justify="center").grid(row=0, columnspan=2)

    Label(frmMain, text="Login name:", font = ("",13)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    Entry(frmMain, textvariable=strLoginName).grid(row=1, column=1)

    Label(frmMain, text="Password:", font = ("",13)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
    Entry(frmMain, textvariable=strPass, show="*").grid(row=2, column=1)

    Button(frmMain, text="New password", anchor="center", font=("",9), width=13, relief="groove", command=open_frmRePass).grid(row=3, column=0, sticky="e")
    Button(frmMain, text="Log in", anchor="center", font=("",9), width=10, relief="groove", command=signIn).grid(row=3, column=1, sticky="e")
    
    frmMain.mainloop()