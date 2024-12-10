import tkinter
from tkinter import*
from tkinter import ttk
import mysql.connector
from time import strftime
from PIL import Image,ImageTk
from tkinter import messagebox



class Register:
    def __init__(self, root):
        self.root=root
        self.root.title("Register Form")
        self.root.geometry("1200x600+0+0")
        self.root.resizable(False, False)




        #************varibles***********

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        self.var_check=IntVar()


        #background Image

        img = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\bgimg1.jpg")
        img = img.resize((1200, 600), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)
        bg_label = tkinter.Label(self.root, image=self.bg)
        bg_label.image = self.bg
        bg_label.place(x=0, y=0, width=1200, height=600)

        # image=Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\th.jpg")
        # self.bg = ImageTk.PhotoImage(image)
        # bg_lbl=tkinter.Label(self.root,image=self.bg)
        # bg_lbl.image=self.bg
        # bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)



        #left Image

        imgleft = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\employimg.jpg")
        imgleft = imgleft.resize((400, 520), Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(imgleft)
        lblimleft = Label(bg_label,image=self.photoimage4, bg="black", borderwidth=0)
        lblimleft.place(x=40, y=40, width=400, height=520)



        # main frame

        frame=Frame(bg_label,bg="white")
        frame.place(x=440,y=40,width="700",height="520")

        # dateTime

        def time():
            string = strftime("[%H:%M:%S]  -  [%d-%m-%Y]")

            label.config(text=string)
            label.after(1000, time)

        label = Label(frame, font=("times new roman", 15, "bold"), fg="red",
                      bg="white")
        label.place(x=0, y=0, width=250, height=41)
        time()


         #register

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman", 20, "bold"),fg="green",bg="white")
        register_lbl.place(x=20,y=70)

        #labels&entry
        # row1

        f_name=Label(frame,text="First Name",font=("times new roman", 13, "bold"),bg="white")
        f_name.place(x=30,y=120)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman", 13, "bold"))
        self.fname_entry.place(x=30,y=140,width=270,height=20)

        #row1

        l_name = Label(frame, text="Last Name", font=("times new roman", 13, "bold"), bg="white")
        l_name.place(x=400, y=120)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 13, "bold"))
        self.txt_lname.place(x=400, y=140, width=270, height=20)

         #row2


        contect = Label(frame, text="Contect No.", font=("times new roman", 13, "bold"), bg="white")
        contect.place(x=30, y=180)

        self.txt_contect = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 13, "bold"))
        self.txt_contect.place(x=30, y=200, width=270, height=20)

         #row2

        email = Label(frame, text="Email ID", font=("times new roman", 13, "bold"), bg="white")
        email.place(x=400, y=180)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 13, "bold"))
        self.txt_email.place(x=400, y=200, width=270, height=20)

        #row3



        security_Q=Label(frame,text="Select Securty Question",font=("times new roman", 13, "bold"),bg="white")
        security_Q.place(x=30, y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman", 11, "bold"),state="readonly")
        self.combo_security_Q["values"]=("select","Your Birth Place","Your Girlfriend Name","You are Pet Name")
        self.combo_security_Q.place(x=30, y=260, width=270, height=20)
        self.combo_security_Q.current(0)

        #row3


        security_A = Label(frame, text="Securty Answer", font=("times new roman", 13, "bold"), bg="white")
        security_A.place(x=400, y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA, font=("times new roman", 13, "bold"))
        self.txt_security.place(x=400, y=260, width=270, height=20)

        #row4



        pswd = Label(frame,text="Password", font=("times new roman", 13, "bold"), bg="white")
        pswd.place(x=30, y=300)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 13, "bold"))
        self.txt_pswd.place(x=30, y=320, width=270, height=20)

        #row4

        confirm_pswd = Label(frame, text="Conform Password", font=("times new roman", 13, "bold"), bg="white",fg="black")
        confirm_pswd.place(x=400, y=300)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 13, "bold"))
        self.txt_confirm_pswd.place(x=400, y=320, width=270, height=20)



        #check button

        checkbtn=Checkbutton( frame,variable= self.var_check,text="I Agree The Term & Condition ", font=("times new roman", 13, "bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=30, y=380)

        # icon button
        #register button

        imgR = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\regimg.png")
        imgR = imgR.resize((160, 75), Image.LANCZOS)
        self.photoimageR = ImageTk.PhotoImage(imgR)
        b1 = Button(frame,image=self.photoimageR, borderwidth=0, cursor="hand2",command=self.register_data,font=("times new roman", 13, "bold"),bg="white")
        b1.place(x=70, y=430, width=150)


        #login button
        img1 = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\Login-Button.png")
        img1 = img1.resize((150, 50), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame,image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2",font=("times new roman", 13, "bold"))
        b2.place(x=420, y=425, width=150)



    # function declareation


    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All field are required")

        elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error","password & conform password must be same",parent=self.root)

        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Terms And Condition")

        else:

            conn = mysql.connector.connect(host="localhost", user="root", password="Anuj@123",database="loginwindow")
            my_cur = conn.cursor()

            query = ("select * from employdetail where email=%s")

            value = (self.var_email.get(),)

            my_cur.execute(query, value)

            row = my_cur.fetchone()

            if row != None:

                messagebox.showerror("Error", "User Already Exist,please try another email", parent=self.root)
            else:
                my_cur.execute("insert into employdetail  Values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                                            self.var_fname.get(),

                                                                                            self.var_lname.get(),

                                                                                            self.var_contact.get(),

                                                                                            self.var_email.get(),

                                                                                            self.var_securityQ.get(),

                                                                                            self.var_securityA.get(),

                                                                                            self.var_pass.get()

                                                                                         ))

            conn.commit()

            conn.close()

            messagebox.showinfo("Success", "Register Successfully", parent=self.root)


    def return_login(self):
        self.root.destroy()





if __name__== "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()