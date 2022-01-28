from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root=root
        self.root.title("Garden Maintenance System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)

        #Background Image
        image= Image.open("gard.jpg")
        image =image.resize((1200,800), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(image)
        self.bg_image = Label(self.root, image= self.bg).pack()

        #Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=120, y=190, height=340, width= 500)

        title =Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white").place(x=50, y=10)
        desc = Label(Frame_login, text="Garden Maintenance System Login", font=("Goudy old style", 20, "bold"), fg="#d25d17", bg="white").place(x=50,
                                                                                                                  y=80)
        lbl_user= Label(Frame_login, text="Username", font=("Goudy old style", 20, "bold"), fg="gray",bg="white").place(x=50, y=120)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="darkgray")
        self.txt_user.place(x=50, y=150, width= 350, height= 35)

        lbl_user = Label(Frame_login, text="Password", font=("Goudy old style", 20, "bold"), fg="gray",
                         bg="white").place(x=50, y=190)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="darkgray")
        self.txt_pass.place(x=50, y=220, width=350, height=35)

        forget_button= Button(Frame_login, text="Forget Password?", bg="white", fg="#d77337", bd=0, font=("times new roman", 12)).place(x=50, y=260)
        login_button= Button(Frame_login, command=self.login_func, text="Login", fg="white", bg="#d77337",
                       font=("times new roman", 18)).place(x=50, y=290)
    def login_func(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required", parent= self.root)

        elif self.txt_pass.get() != "123456" or self.txt_user.get() != "@arya":
            messagebox.showerror("Error", "Invalid Username/Password", parent=self.root)

        else:
            messagebox.showinfo("Welcome", f"Welcome {self.txt_user.get()}\n We might think we are nurturing garden, but actually it's our garden that is nurturing us!", parent=self.root)


root = Tk()
obj= Login(root)
root.mainloop()