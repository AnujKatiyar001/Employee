import tkinter
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from time import strftime

import mysql.connector
from tkinter import messagebox



class EmployeeManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Employee Management System")
        self.root.geometry("1600x800+0+0")

        lbl_title = Label(self.root, text="Employee Management System", font=("times new roman", 30, "bold"),
                                 bg="yellow", fg="red")
        lbl_title.place(x=0, y=0, width=1600, height=45)


        img_logo = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\logo kruti.png")
        img_logo =img_logo.resize((50,50),Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo= Label(self.root,image=self.photo_logo)
        self.logo.place(x=475,y=0,width=40,height=45)

        def time():
            string = strftime("%H:%M:%S  -  %d-%m-%Y")  # ('%H:%M:%S %p')
            label.config(text=string)
            label.after(1000, time)

        label = Label(lbl_title, font=("times new roman", 17, "bold"), fg="green",
                      bg="yellow")
        label.place(x=0, y=10, width=250, height=25)
        time()

        #*****************variables*********

        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_desi = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_married_status = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_id_proof_type = StringVar()
        self.var_id_proof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()

        self.var_com_search = StringVar()
        self.var_search = StringVar()


        #Image Frame

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1600,height=160)

        #1st image

        img1 = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\empimg1.jpg")
        img1 = img1.resize((500, 160), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)
        # bg_label = tkinter.Label(self.root, image=self.photo1)
        # bg_label.image = self.photo1
        # bg_label.place(x=0, y=45, width=500, height=160)
        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=500, height=155)

        # 2st image

        img2 = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\empimg2.jpg")
        img2 = img2.resize((500, 160), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)
        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=500, y=0, width=500, height=155)

        # 3st image

        img3 = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\empimg3.jpg")
        img3 = img3.resize((550, 160), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)
        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=1000, y=0, width=550, height=155)

        #Main Frame

        main_frame = Frame(self.root, bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=5, y=210, width=1520, height=535)


        #UpperFrame

        uper_frame = LabelFrame(main_frame, bd=3, relief=RIDGE, text="EMPLOYEE DETAILS",
                                font=("times new roman", 10, "bold"),fg='red')
        uper_frame.place(x=10, y=0, width=1490, height=250)


        #1st line

        #department

        label_dep = Label(uper_frame, text="Department", font=("times new roman", 15, "bold"))
        label_dep.grid(row=0, column=0, padx=2,pady=7, sticky=W)

        combo_dep = ttk.Combobox(uper_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"),
                                 width=20, state="readonly")
        combo_dep["values"] = ("Select Department", "HR", "Software", "Manager")
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #Name

        name_label = Label(uper_frame, text="Name:", font=("times new roman", 15, "bold"))
        name_label.grid(row=0, column=2, padx=10, sticky=W)

        name_entry = ttk.Entry(uper_frame, width=20,textvariable=self.var_name,
                               font=("times new roman", 15, "bold"))
        name_entry.grid(row=0, column=3, padx=2,pady=7,sticky=W)


        #Designation

        Designation_label = Label(uper_frame, text="Designation:", font=("times new roman", 15, "bold"))
        Designation_label.grid(row=1, column=0, padx=2,pady=7, sticky=W)

        Designation_entry = ttk.Entry(uper_frame, width=20,textvariable=self.var_desi,
                                      font=("times new roman", 15, "bold"))
        Designation_entry.grid(row=1, column=1, padx=2, pady=7,sticky=W)

        #Email

        Email_label = Label(uper_frame, text="Email:", font=("times new roman", 15, "bold"))
        Email_label.grid(row=1, column=2, padx=10, sticky=W)

        Email_entry = ttk.Entry(uper_frame,  width=20,textvariable=self.var_email,
                                font=("times new roman", 15, "bold"))
        Email_entry.grid(row=1, column=3, padx=2,pady=7, sticky=W)


        #Address

        Address_label = Label(uper_frame, text="Address:", font=("times new roman", 15, "bold"))
        Address_label.grid(row=2, column=0, padx=2, pady=7,sticky=W)

        Address_entry = ttk.Entry(uper_frame, width=20,textvariable=self.var_address,
                                  font=("times new roman", 15, "bold"))
        Address_entry.grid(row=2
                           , column=1, padx=2,pady=7, sticky=W)

        #Married

        Marred_label = Label(uper_frame, text="Marred Status:", font=("times new roman", 15, "bold"))
        Marred_label.grid(row=2, column=2, padx=2,pady=7, sticky=W)

        marred_combo = ttk.Combobox(uper_frame,textvariable=self.var_married_status, font=("times new roman", 13, "bold"),
                                 width=20, state="readonly")
        marred_combo["values"] = ("Select Status","Marred", "Unmarred")
        marred_combo.current(0)
        marred_combo.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        #DOB

        DOB_label = Label(uper_frame, text="DOB:", font=("times new roman", 15, "bold"))
        DOB_label.grid(row=3, column=0, padx=2,pady=7, sticky=W)

        DOB_entry = ttk.Entry(uper_frame,  width=20,textvariable=self.var_dob,
                              font=("times new roman", 15, "bold"))
        DOB_entry.grid(row=3, column=1, padx=2,pady=7, sticky=W)


        #DOJ

        DOJ_label = Label(uper_frame, text="DOJ:", font=("times new roman", 15, "bold"))
        DOJ_label.grid(row=3, column=2, padx=2, pady=7,sticky=W)

        DOJ_entry = ttk.Entry(uper_frame, width=20,textvariable=self.var_doj,
                              font=("times new roman", 15, "bold"))
        DOJ_entry.grid(row=3, column=3, padx=2,pady=7, sticky=W)

        #Id Proof

        Id_proof_combo = ttk.Combobox(uper_frame,textvariable=self.var_id_proof_type, font=("times new roman", 13, "bold"),
                                    width=10, state="readonly")
        Id_proof_combo["values"] = ("Select ID Proof","PAN CARD", "AADHAR","DRIVING LICENCE")
        Id_proof_combo.current(0)
        Id_proof_combo.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        Id_proof_entry = ttk.Entry(uper_frame,textvariable=self.var_id_proof, width=20,
                              font=("times new roman", 15, "bold"))
        Id_proof_entry.grid(row=4, column=1, padx=2, pady=7, sticky=W)

        #Gender

        label_gender = Label(uper_frame, text="Gender", font=("times new roman", 15, "bold"))
        label_gender.grid(row=4, column=2, padx=2, pady=7, sticky=W)

        combo_gender = ttk.Combobox(uper_frame,textvariable=self.var_gender, font=("times new roman", 13, "bold"),
                                 width=20, state="readonly")
        combo_gender["values"] = ("Select Gender", "Male", "Female")
        combo_gender.current(0)
        combo_gender.grid(row=4, column=3, padx=2, pady=7, sticky=W)

        #Phone

        phone_label = Label(uper_frame, text="Phone:", font=("times new roman", 15, "bold"))
        phone_label.grid(row=0, column=4, padx=2, pady=7, sticky=W)

        phone_entry = ttk.Entry(uper_frame,textvariable=self.var_phone, width=20,
                              font=("times new roman", 15, "bold"))
        phone_entry.grid(row=0, column=5, padx=2, pady=7, sticky=W)

        #country

        country_label = Label(uper_frame, text="Country:", font=("times new roman", 15, "bold"))
        country_label.grid(row=1, column=4, padx=2, pady=7, sticky=W)

        country_entry = ttk.Entry(uper_frame,textvariable=self.var_country, width=20,
                                font=("times new roman", 15, "bold"))
        country_entry.grid(row=1, column=5, padx=2, pady=7, sticky=W)

        #CTC

        ctc_label = Label(uper_frame, text="Salary CTC:", font=("times new roman", 15, "bold"))
        ctc_label.grid(row=2, column=4, padx=2, pady=7, sticky=W)

        ctc_entry = ttk.Entry(uper_frame, width=20,textvariable=self.var_salary,
                                font=("times new roman", 15, "bold"))
        ctc_entry.grid(row=2, column=5, padx=2, pady=7, sticky=W)

        #mask image


        img_mask = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\maskimages.jpg")
        img_mask = img_mask.resize((200, 225), Image.LANCZOS)
        self.mask = ImageTk.PhotoImage(img_mask)
        self.img_mask0 = Label(uper_frame, image=self.mask)
        self.img_mask0.place(x=1000, y=0, width=250, height=225)


        #Button Frame

        button_frame = Frame(uper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1250, y=5, width=220, height=190)


        #Button

        save_btn = Button(button_frame,command=self.add_data,  text="Save", width=25,
                          font=("times new roman", 13, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0,padx=1,pady=7,sticky=W)


        update_btn = Button(button_frame,  text="Update", command=self.update_data, width=25, font=("times new roman", 13, "bold"),
                            bg="blue", fg="white")
        update_btn.grid(row=1, column=0,padx=1,pady=7,sticky=W)


        delete_btn = Button(button_frame, text="Delete",command=self.delete_data, width=25, font=("times new roman", 13, "bold"),
                            bg="blue", fg="white")
        delete_btn.grid(row=2, column=0,padx=1,pady=7,sticky=W)


        reset_btn = Button(button_frame, text="Reset", command=self.reset_data,width=25, font=("times new roman", 13, "bold"),
                           bg="blue", fg="white")
        reset_btn.grid(row=3, column=0,padx=1,pady=7,sticky=W)





        #Lower Frame

        lower_frame = LabelFrame(main_frame, bd=3, relief=RIDGE, text="EMPLOYEE DETAILS TABLE",
                                 font=("times new roman", 10, "bold"),fg='green')
        lower_frame.place(x=10, y=260, width=1490, height=260)

        #search frame

        search_frame = LabelFrame(lower_frame, bd=3, relief=RIDGE, text="SEARCH EMPLOYEE INFORMATION",
                                  font=("times new roman", 10, "bold"),fg='orange')
        search_frame.place(x=5, y=5, width=1470, height=60)


        search_label = Label(search_frame, text=" SEARCH BY:", font=("times new roman", 15, "bold"), bg="red",
                             fg="white")
        search_label.grid(row=0, column=0, padx=1,pady=7, sticky=W)


        #search Button

        # self.var_com_search=StringVar()
        # self.var_search=StringVar()

        search_bar_combo = ttk.Combobox(search_frame,textvariable=self.var_com_search, font=("times new roman", 13, "bold"),
                                      width=20, state="readonly")
        search_bar_combo["values"] = ("Search Option", "Phone", "Aadhar", "DRIVING LICENCE")
        search_bar_combo.current(0)
        search_bar_combo.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        search_bar_entry = ttk.Entry(search_frame,textvariable=self.var_search, width=20,
                                   font=("times new roman", 15, "bold"))
        search_bar_entry.grid(row=0, column=2, padx=2, pady=7, sticky=W)


        search_btn = Button(search_frame, text="Search",command=self.search_data, width=20, font=("times new roman", 11, "bold"), bg="blue",
                            fg="white")
        search_btn.grid(row=0, column=3, padx=10, sticky=W)


        showall_btn = Button(search_frame, text="Show All",command=self.fatch_data, width=20, font=("times new roman", 11, "bold"), bg="blue",
                            fg="white")
        showall_btn.grid(row=0, column=4, padx=10, sticky=W)

        #maskimage

        img_mask1 = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\maskimages.jpg")
        img_mask1 = img_mask1.resize((70, 50), Image.LANCZOS)
        self.mask1 = ImageTk.PhotoImage(img_mask1)
        self.img_mask1 = Label(search_frame, image=self.mask1)
        self.img_mask1.place(x=1000, y=0, width=70, height=40)

        #text

        mask_frame = LabelFrame(search_frame, bd=3, relief=RIDGE,
                                  font=("times new roman", 10, "bold"), fg='orange')
        mask_frame.place(x=1100, y=0, width=320, height=40)


        stayhome=Label(mask_frame,text='Wear A Mask',font=("times new roman", 30, "bold"),fg='red')
        stayhome.place(x=0,y=0,width=300,height=35)



        # *********************Employee table***************

        #tableframe

        table_frame = LabelFrame(lower_frame, bd=3, relief=RIDGE,
                                font=("times new roman", 10, "bold"), fg='orange')
        table_frame.place(x=5, y=70, width=1475, height=150)

        #******************scrrolbar*************



        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame, columns=(
            "dep", "name", "desi", "email", "address", "married", "dob", "doj", "id proof type", "id proof", "gender",
            "phone",
            "country",
            "salary"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)


        self.employee_table.heading("dep", text="Department")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("desi", text="Designation")
        self.employee_table.heading("email",text="Email")
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("married", text="Married_Status")
        self.employee_table.heading("dob", text="DOB")
        self.employee_table.heading("doj", text="DOJ")
        self.employee_table.heading("id proof type",text="ID_Type")
        self.employee_table.heading("id proof", text="ID_proof")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading("phone", text="Phone")
        self.employee_table.heading("country", text="Country")
        self.employee_table.heading("salary", text="Salary")
        self.employee_table["show"] = "headings"

        self.employee_table.pack(fill=BOTH, expand=1)

        self.employee_table.column("dep", width=125)
        self.employee_table.column("name", width=125)
        self.employee_table.column("desi", width=125)
        self.employee_table.column("email", width=125)
        self.employee_table.column("address", width=125)
        self.employee_table.column("married", width=125)
        self.employee_table.column("dob", width=125)
        self.employee_table.column("doj", width=125)
        self.employee_table.column("id proof type", width=125)
        self.employee_table.column("id proof", width=125)
        self.employee_table.column("gender", width=125)
        self.employee_table.column("phone", width=125)
        self.employee_table.column("country", width=125)
        self.employee_table.column("salary", width=125)

        self.employee_table.pack(fill=BOTH, expand=1)

    #*****************function Declarations******************


        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fatch_data()


    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", port="3306", user="root", password="Anuj@123",
                                               database="employeemanagmentsystem")
                my_cur=conn.cursor()

                my_cur.execute("insert into employee_delete values( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_desi.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_married_status.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_doj.get(),
                                                                                                                    self.var_id_proof_type.get(),
                                                                                                                    self.var_id_proof.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_country.get(),
                                                                                                                    self.var_salary.get()

                                                                                                                  ))

                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success", "Employee Detail has been Added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)



   #********************fatch data

    def fatch_data(self):
        conn = mysql.connector.connect(host="127.0.0.1", port="3306", user="root", password="Anuj@123",
                                       database="employeemanagmentsystem")
        my_cur = conn.cursor()
        my_cur.execute('select * from employee_delete')
        data = my_cur.fetchall()
        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values=i)
            conn.commit()

        conn.close()


     #*******************get cursor*********************


    def get_cursor(self,event=""):
        curses_row=self.employee_table.focus()
        content = self.employee_table.item(curses_row)
        data= content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_desi.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married_status.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_id_proof_type.set(data[8])
        self.var_id_proof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    # def update_data(self):
    #     if self.var_dep.get() == "" or self.var_email.get() == "":
    #         messagebox.showerror("Error", "All Fields are Required")
    #     else:
    #         try:
    #             Update = messagebox.askyesno("Update", "Do you Want to update Details", parent=self.root)
    #             if Update > 0:
    #
    #                 conn = mysql.connector.connect(host="127.0.0.1", port="3306", user="root", password="Anuj@123",
    #                                                database="employeemanagmentsystem")
    #                 my_cur = conn.cursor()
    #                 my_cur.execute(
    #                     "update employee_delete set Department=%s,Name=%s,Designation=%s,Email%s,Address=%s,Married_Status=%s,DOB=%s,DOJ=%s,ID_Type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where ID_proof=%s ",
    #
    #                     (
    #
    #                                                                                                                                                                                                                         self.var_dep.get(),
    #                                                                                                                                                                                                                         self.var_name.get(),
    #                                                                                                                                                                                                                         self.var_desi.get(),
    #                                                                                                                                                                                                                         self.var_email.get(),
    #                                                                                                                                                                                                                         self.var_address.get(),
    #                                                                                                                                                                                                                         self.var_married_status.get(),
    #                                                                                                                                                                                                                         self.var_dob.get(),
    #                                                                                                                                                                                                                         self.var_doj.get(),
    #                                                                                                                                                                                                                         self.var_id_proof_comb.get(),
    #                                                                                                                                                                                                                         self.var_gender.get(),
    #                                                                                                                                                                                                                         self.var_phone.get(),
    #                                                                                                                                                                                                                         self.var_country.get(),
    #                                                                                                                                                                                                                         self.var_salary.get(),
    #                                                                                                                                                                                                                         self.var_id_proof.get()
    #
    #                                                                                                                                                                                                                          ))
    #
    #             else:
    #
    #                 if not Update:
    #                     return
    #
    #             #messagebox.showinfo("Success", "Update Successfully", parent=self.root)
    #
    #             conn.commit()
    #
    #             self.fatch_data()
    #
    #             conn.close()
    #
    #             messagebox.showinfo("Update", "Update Successfully", parent=self.root)
    #
    #         except Exception as es:
    #
    #             messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def update_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "":
        
            messagebox.showerror("Error", "All Field are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you Want to update Details", parent=self.root)
                if Update > 0:

                    conn = mysql.connector.connect(host="127.0.0.1", port="3306", user="root", password="Anuj@123",
                                                                         database="employeemanagmentsystem")
                    my_cur = conn.cursor()
                    my_cur.execute(
                        "update employee_delete set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married_Status=%s,DOB=%s,DOJ=%s,ID_Type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where ID_proof=%s",
                        (

                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                                        self.var_desi.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_married_status.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_id_proof_type.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_country.get(),
                                                                                                                                                                                                                        self.var_salary.get(),
                                                                                                                                                                                                                        self.var_id_proof.get()

                                                                                                                                                                                                                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Update Successfully", parent=self.root)
                conn.commit()
                self.fatch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_id_proof.get() == "":
            messagebox.showerror("Error", "Employee ID must be require", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do You want to delete this employee",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="127.0.0.1", port="3306", user="root", password="Anuj@123",
                                                   database="employeemanagmentsystem")
                    my_cur = conn.cursor()
                    sql = "delete from employee_delete where ID_proof=%s"
                    value = (self.var_id_proof.get(),)
                    my_cur.execute(sql, value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Delete", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_name.set("")
        self.var_desi.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married_status.set("Select Status ")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_id_proof_comb.set("Select ID Proof")
        self.var_id_proof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")



     #*************search*********
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", port="3306", user="root", password="Anuj@123",
                                               database="employeemanagmentsystem")
                my_cur = conn.cursor()
                my_cur.execute('select * from employee_delete where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cur.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)




if __name__== "__main__":
    root = Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()