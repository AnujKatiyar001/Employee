import tkinter
from tkinter import*
from tkinter import ttk
from time import strftime
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from LoginRegistreform import Register
from Employee import EmployeeManagementSystem

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1200x600+0+0")
        self.root.resizable(False,False)

        #varible
        self.var_email1 = StringVar()
        self.var_password1 = StringVar()



        #background image

        img = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\bgimg1.jpg")
        img = img.resize((1200, 600), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)
        bg_label = tkinter.Label(self.root, image=self.bg)
        bg_label.image = self.bg
        bg_label.place(x=0, y=0, width=1200, height=600)





        #frame
        frame= Frame(self.root,bg="black")
        frame.place(x=400,y=40,width=340,height=500)

        #logo image

        img1 = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\mainimg.jpg")
        img1 = img1.resize((50, 50), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=550, y=90, width=50, height=50)


        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="light green",bg="black")
        get_str.place(x=95,y=110)

        #date Time

        def time():
            string = strftime("[%H:%M:%S]  -  [%d-%m-%Y]")

            label.config(text=string)
            label.after(1000, time)

        label = Label(frame, font=("times new roman", 15, "bold"), fg="red",
                      bg="black")
        label.place(x=50, y=0, width=250, height=41)
        time()



        #label

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="blue",bg="black")
        username.place(x=70,y=155)


        #entryfill

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="blue", bg="black")
        password.place(x=70, y=225)

        #entryfill

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # icon image

        img2 = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\lockimg.jpg")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=445, y=268, width=17, height=17)


        img3=Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\persinimg.jpg")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3, bg="black",borderwidth=0)
        lblimg3.place(x=445,y=197,width=17,height=17)




        #Button

        #loginbutton

        loginbtn = Button(frame, text="Login",command=self.login,font=("times new roman", 15, "bold"),bd=3,relief=RIDGE,fg="black",bg="red",activeforeground="white",activebackground="yellow")
        loginbtn.place(x=110,y=330,width=125,height=40)

        # Registerbutton

        Registerbtn = Button(frame, text="New User Register",command=self.rigister_window, font=("times new roman", 15, "bold"),borderwidth=0, relief=RIDGE, fg="blue",
                          bg="black", activeforeground="white", activebackground="black")
        Registerbtn.place(x=15, y=400,)


        #forgot Button

        forgotbtn = Button(frame, text="Forget Password",command=self.forgot_password_window, font=("times new roman", 15, "bold"),borderwidth=0,
                             fg="blue",bg="black", activeforeground="white", activebackground="black")
        forgotbtn.place(x=15, y=430, width=150,)


    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "ALL FIELD REQUIRED", parent=self.root)
        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("success", "WELCOME")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Anuj@123",
                                           database="loginwindow")
            my_cur = conn.cursor()
            my_cur.execute("select * from employdetail where email=%s and password=%s", (

                self.var_email1.get(),
                self.var_password1.get()

            ))

            row = my_cur.fetchone()
            print(row)
            if row is not None:
                messagebox.showerror("Error", "Invalid UserName & password")
            else:
                open_main = messagebox.askyesno("YESNo", "Access Only Admin")
                if open_main > 0:

                    self.new_window = Toplevel(self.root)
                    self.app = EmployeeManagementSystem(self.new_window)

                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()


    # def login(self):
    #     if self.txtuser.get()=="" or self.txtpass.get()=="":
    #         messagebox.showerror("Error","ALL FIELD REQUIRED",parent=self.root)
    #     elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
    #         messagebox.showinfo("success","WELCOME")
    #     else:
    #         conn = mysql.connector.connect(host="localhost", user="root", password="Anuj@123", database="loginwindow")
    #         my_cur = conn.cursor()
    #         my_cur.execute("select * from employdetail where email=%s and password=%s",(
    #
    #                                                                                     self.var_email1.get(),
    #                                                                                     self.var_password1.get()
    #
    #                                                                                           ))
    #
    #         row=my_cur.fetchone()
    #         #print(row)
    #         if row == None:
    #            messagebox.showerror("Error","Invalid UserName & password")
    #         else:
    #             open_main=messagebox.askyesno("YESNo","Access Only Admin")
    #             if open_main>0:
    #                 self.new_window=Toplevel(self.root)
    #                 self.app=EmployeeManagementSystem(self.new_window)
    #
    #             else:
    #                 if not open_main:
    #                     return
    #
    #         conn.commit()
    #         conn.close()


    #Reset Password

    def reset_pass(self):
        if self.combo_security_Q.get()=="select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter new Password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Anuj@123",
                                                    database="loginwindow")
            my_cur = conn.cursor()
            qury=("select * from employdetail where email=%s and securtyQ=%s and securtyA=%s")
            Vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cur.execute(qury,Vlaue)
            row=my_cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer",parent=self.root2)
            else:
                query=("update employdetail set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cur.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password is reset, Please Login New Password",parent=self.root2)
                self.root2.destroy()


    #forgot_password_window

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter the email address to reset password")

        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Anuj@123",
                                           database="loginwindow")
            my_cur = conn.cursor()
            query = ("select * from employdetail where email=%s")
            value = (self.txtuser.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
                #print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")


                #frame


                L= Label(self.root2,text="Forgo Password",font=("times new roman", 20, "bold"),fg="red",bg="white")
                L.place(x=0,y=10,relwidth=1)

                #row1

                security_Q = Label(self.root2, text="Select Securty Question", font=("times new roman", 13, "bold"),bg="white")
                security_Q.place(x=20, y=60)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 11, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("select", "Your Birth Place", "Your Girlfriend Name", "You are Pet Name")
                self.combo_security_Q.place(x=20, y=90, width=270, height=20)
                self.combo_security_Q.current(0)

                # row2

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 13, "bold"), bg="white")
                security_A.place(x=20, y=150)

                self.txt_security = ttk.Entry(self.root2,font=("times new roman", 13, "bold"))
                self.txt_security.place(x=20, y=180, width=270, height=20)

                # row3

                new_password = Label(self.root2, text="New Password", font=("times new roman", 13, "bold"), bg="white")
                new_password.place(x=20, y=210)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 13, "bold"))
                self.txt_newpass.place(x=20, y=240, width=270, height=20)
                #button

                btn=Button(self.root2,text="Reset",command=self.reset_pass, font=("times new roman", 13, "bold"),fg="white",bg="green")
                btn.place(x=120,y=300)



if __name__== "__main__":
    root = Tk()
    app = Login_window(root)
    root.mainloop()

