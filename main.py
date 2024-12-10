import tkinter
from tkinter import*
from tkinter import ttk
import mysql.connector
from PIL import Image,ImageTk
from tkinter import messagebox
import os
from time import strftime




class EmployeeManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Employee Management System")
        self.root.geometry("1600x800+0+0")

        title_lbl = Label(self.root, text="Employee Management System", font=("times new roman", 30, "bold"),
                          bg="yellow", fg="red")
        title_lbl.place(x=0, y=0, width=1600, height=45)

        def time():
            string = strftime("%H:%M:%S  -  %d-%m-%Y")  # ('%H:%M:%S %p')
            label.config(text=string)
            label.after(1000, time)

        label = Label(title_lbl, font=("times new roman", 17, "bold"), fg="green",
                      bg="yellow")
        label.place(x=0, y=10, width=250, height=25)
        time()

    
        img = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\empimg1.jpg")
        img = img.resize((500, 100), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)
        bg_label = tkinter.Label(self.root, image=self.bg)
        bg_label.image = self.bg
        bg_label.place(x=0, y=45, width=500, height=100)
    
    #     img2 = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\empimg2.jpg")
    #     img2 = img2.resize((550, 100), Image.LANCZOS)
    #     self.photoimage2 = ImageTk.PhotoImage(img2)
    #     lblimg2 = tkinter.Label(self.root, image=self.photoimage2)
    #     lblimg2.image = self.photoimage2
    #     lblimg2.place(x=500, y=45, width=550, height=100)
    #
    #     img3 = Image.open(r"C:\Users\91987\PycharmProjects\EmployeeManegmentSystem\Image\empimg3.jpg")
    #     img3 = img3.resize((550, 100), Image.LANCZOS)
    #     self.photoimage3 = ImageTk.PhotoImage(img3)
    #     lblimg3 = tkinter.Label(self.root, image=self.photoimage3)
    #     lblimg3.image = self.photoimage3
    #     lblimg3.place(x=1000, y=45, width=550, height=100)
    #
    #     # varibels
    #
    #     self.var_dep = StringVar()
    #     self.var_name = StringVar()
    #     self.var_degi = StringVar()
    #     self.var_email = StringVar()
    #     self.var_address = StringVar()
    #     self.var_married = StringVar()
    #     self.var_dob = StringVar()
    #     self.var_doj = StringVar()
    #     self.var_idproofcomb = StringVar()
    #     self.var_idproof = StringVar()
    #     self.var_gender = StringVar()
    #     self.var_phone = StringVar()
    #     self.var_country = StringVar()
    #     self.var_salary = StringVar()
    #
    #
    #     #frame
    #
    #
    #     main_frame = Frame(self.root, bd=10)
    #     main_frame.place(x=0, y=150, width=1580, height=600)
    #
    #     uper_frame = LabelFrame(main_frame, bd=3, relief=RIDGE, text="EMPLOYEE DETAILS",
    #                             font=("times new roman", 10, "bold"))
    #     uper_frame.place(x=60, y=0, width=1350, height=210)
    #
    #     #1st line
    #
    #     # EmployeeID_label = Label(uper_frame, text="ID:", font=("times new roman", 15, "bold"), bg="white")
    #     # EmployeeID_label.grid(row=0, column=0, padx=10, sticky=W)
    #     #
    #     # EmployeeID_entry = ttk.Entry(uper_frame, width=20,
    #     #                             font=("times new roman", 15, "bold"))
    #     # EmployeeID_entry.grid(row=0, column=1, padx=10, sticky=W)
    #
    #     dep_label = Label(uper_frame, text="Department", font=("times new roman", 15, "bold"), bg="white")
    #     dep_label.grid(row=0, column=0, padx=10, sticky=W)
    #
    #     dep_combo = ttk.Combobox(uper_frame, textvariable=self.var_dep, font=("times new roman", 15, "bold"),
    #                              width=10, state="readonly")
    #     dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
    #     dep_combo.current(0)
    #     dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
    #
    #
    #
    #     name_label = Label(uper_frame, text="Name:", font=("times new roman", 15, "bold"), bg="white")
    #     name_label.grid(row=0, column=2, padx=10, sticky=W)
    #
    #     name_entry = ttk.Entry(uper_frame,textvariable=self.var_name, width=20,
    #                            font=("times new roman", 15, "bold"))
    #     name_entry.grid(row=0, column=3, padx=20, sticky=W)
    #
    #     phoneno_label = Label(uper_frame, text="Phone No.:", font=("times new roman", 15, "bold"), bg="white")
    #     phoneno_label.grid(row=0, column=4, padx=10, sticky=W)
    #
    #     phoneno_entry = ttk.Entry(uper_frame,textvariable=self.var_phone, width=20,
    #                            font=("times new roman", 15, "bold"))
    #     phoneno_entry.grid(row=0, column=5, padx=20, sticky=W)
    #
    #
    #
    #
    #
    #     #2nd line
    #
    #     Desgination_label = Label(uper_frame, text="Designition:", font=("times new roman", 15, "bold"), bg="white")
    #     Desgination_label.grid(row=1, column=0, padx=10, sticky=W)
    #
    #     Desgination_entry = ttk.Entry(uper_frame,textvariable=self.var_degi, width=20,
    #                                  font=("times new roman", 15, "bold"))
    #     Desgination_entry.grid(row=1, column=1, padx=10, sticky=W)
    #
    #     Email_label = Label(uper_frame, text="Email:", font=("times new roman", 15, "bold"), bg="white")
    #     Email_label.grid(row=1, column=2, padx=10, sticky=W)
    #
    #     Email_entry = ttk.Entry(uper_frame,textvariable=self.var_email, width=20,
    #                            font=("times new roman", 15, "bold"))
    #     Email_entry.grid(row=1, column=3, padx=20, sticky=W)
    #
    #     Country_label = Label(uper_frame, text="Country:.", font=("times new roman", 15, "bold"), bg="white")
    #     Country_label.grid(row=1, column=4, padx=10, sticky=W)
    #
    #     Country_entry = ttk.Entry(uper_frame,textvariable=self.var_country, width=20,
    #                               font=("times new roman", 15, "bold"))
    #     Country_entry.grid(row=1, column=5, padx=20, sticky=W)
    #
    #
    #     #3rd line
    #
    #     Address_label = Label(uper_frame, text="Address:", font=("times new roman", 15, "bold"), bg="white")
    #     Address_label.grid(row=2, column=0, padx=10, sticky=W)
    #
    #     Address_entry = ttk.Entry(uper_frame,textvariable=self.var_address, width=20,
    #                                  font=("times new roman", 15, "bold"))
    #     Address_entry.grid(row=2, column=1, padx=10, sticky=W)
    #
    #
    #     Marred_label = Label(uper_frame, text="Marred Status:", font=("times new roman", 15, "bold"), bg="white")
    #     Marred_label.grid(row=2, column=2, padx=10, sticky=W)
    #
    #     Marred_entry = ttk.Entry(uper_frame,textvariable=self.var_married, width=20,
    #                            font=("times new roman", 15, "bold"))
    #     Marred_entry.grid(row=2, column=3, padx=20, sticky=W)
    #
    #
    #     salary_label = Label(uper_frame, text="Salary(CTC):", font=("times new roman", 14, "bold"), bg="white")
    #     salary_label.grid(row=2, column=4, padx=10, sticky=W)
    #
    #     Salary_entry = ttk.Entry(uper_frame,textvariable=self.var_salary, width=20,
    #                               font=("times new roman", 15, "bold"))
    #     Salary_entry.grid(row=2, column=5, padx=20, sticky=W)
    #
    #     # 4nd line
    #
    #     DOB_label = Label(uper_frame, text="DOB:", font=("times new roman", 15, "bold"), bg="white")
    #     DOB_label.grid(row=3, column=0, padx=10, sticky=W)
    #
    #     DOB_entry = ttk.Entry(uper_frame,textvariable=self.var_dob, width=20,
    #                                   font=("times new roman", 15, "bold"))
    #     DOB_entry.grid(row=3, column=1, padx=10, sticky=W)
    #
    #
    #
    #     DOJ_label = Label(uper_frame, text="DOJ:", font=("times new roman", 15, "bold"), bg="white")
    #     DOJ_label.grid(row=3, column=2, padx=10, sticky=W)
    #
    #     DOJ_entry = ttk.Entry(uper_frame, textvariable=self.var_doj,width=20,
    #                             font=("times new roman", 15, "bold"))
    #     DOJ_entry.grid(row=3, column=3, padx=20, sticky=W)
    #
    #     #5th line
    #
    #     # Adhar_label = Label(uper_frame, text="AdharNO.", font=("times new roman", 13, "bold"), bg="white")
    #     # Adhar_label.grid(row=4, column=0, padx=10, sticky=W)
    #     #
    #     # Adhar_entry = ttk.Entry(uper_frame, width=20,
    #     #                           font=("times new roman", 15, "bold"))
    #     # Adhar_entry.grid(row=4, column=1, padx=20, sticky=W)
    #
    #     idproof_label = Label(uper_frame, text="IDproof", font=("times new roman", 15, "bold"), bg="white")
    #     idproof_label.grid(row=4, column=0, padx=10, sticky=W)
    #
    #     idproof_comb = ttk.Combobox(uper_frame, textvariable=self.var_idproofcomb, font=("times new roman", 15, "bold"),
    #                              width=10, state="readonly")
    #     idproof_comb["values"] = ("Select IDproof","Adhar", "CompanyID", "GovermentID")
    #     idproof_comb.current(0)
    #     idproof_comb.grid(row=4, column=1, padx=2, pady=10, sticky=W)
    #
    #
    #
    #     idproof = Label(uper_frame, text="IDfroofNo.", font=("times new roman", 15, "bold"), bg="white")
    #     idproof.grid(row=4, column=2, padx=10, sticky=W)
    #
    #     idproof_entry = ttk.Entry(uper_frame, textvariable=self.var_idproof, width=20,
    #                              font=("times new roman", 15, "bold"))
    #     idproof_entry.grid(row=4, column=3, padx=20, sticky=W)
    #
    #
    #
    #     Gender_label = Label(uper_frame, text="Gender:", font=("times new roman", 15, "bold"), bg="white")
    #     Gender_label.grid(row=4, column=4, padx=10, sticky=W)
    #
    #     Gender_entry = ttk.Entry(uper_frame, textvariable=self.var_gender,width=20,
    #                             font=("times new roman", 15, "bold"))
    #     Gender_entry.grid(row=4, column=5, padx=20, sticky=W)
    #
    #
    #     #button
    #
    #     save_btn = Button(uper_frame, text="Save",command=self.add_data, width=14, font=("times new roman", 13, "bold"),
    #                       bg="blue", fg="white")
    #     save_btn.grid(row=0, column=9)
    #
    #
    #     update_btn = Button(uper_frame, text="Update", width=14, font=("times new roman", 13, "bold"),
    #                       bg="blue", fg="white")
    #     update_btn.grid(row=1, column=9)
    #
    #     delete_btn = Button(uper_frame, text="Delete", width=14, font=("times new roman", 13, "bold"),
    #                         bg="blue", fg="white")
    #     delete_btn.grid(row=2, column=9)
    #
    #     reset_btn = Button(uper_frame, text="Reset", width=14, font=("times new roman", 13, "bold"),
    #                         bg="blue", fg="white")
    #     reset_btn.grid(row=3, column=9)
    #
    #
    #     #lower frame
    #
    #
    #     lower_frame = LabelFrame(main_frame, bd=3, relief=RIDGE, text="EMPLOYEE DETAILS",
    #                             font=("times new roman", 10, "bold"))
    #     lower_frame.place(x=0, y=220, width=1510, height=370)
    #
    #
    #     search_frame = LabelFrame(lower_frame, bd=3, relief=RIDGE, text="SEARCH EMPLOYEE",
    #                               font=("times new roman", 10, "bold"))
    #     search_frame.place(x=5, y=5, width=1490, height=60)
    #
    #     search_label = Label(search_frame, text=" SEARCH BY:", font=("times new roman", 15, "bold"), bg="red",
    #                          fg="white")
    #     search_label.grid(row=0, column=0, padx=10, sticky=W)
    #
    #     phoneno_label = Label(search_frame, text="Phone No:", font=("times new roman", 15, "bold"), bg="white")
    #     phoneno_label.grid(row=0, column=1, padx=10, sticky=W)
    #
    #     phoneno_entry = ttk.Entry(search_frame, width=20,
    #                               font=("times new roman", 15, "bold"))
    #     phoneno_entry.grid(row=0, column=2, padx=20, sticky=W)
    #
    #
    #     search_btn = Button(search_frame, text="Search", width=20, font=("times new roman", 11, "bold"), bg="blue",
    #                         fg="white")
    #     search_btn.grid(row=0, column=3, padx=10, sticky=W)
    #
    #     showall_btn = Button(search_frame, text="Show All", width=20, font=("times new roman", 11, "bold"), bg="blue",
    #                         fg="white")
    #     showall_btn.grid(row=0, column=4, padx=10, sticky=W)
    #
    #
    #
    #     #scrrolbar
    #
    #     table_frame = Frame(lower_frame, bd=3, relief=RIDGE)
    #     table_frame.place(x=5, y=70, width=1490, height=260)
    #
    #     scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
    #     scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
    #
    #     self.employee_table = ttk.Treeview(table_frame, columns=(
    #         "dep", "name", "degi", "email", "address", "married", "dob", "doj", "idproofcomb", "idproof", "gender", "phone",
    #         "country",
    #         "salary"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    #
    #     scroll_x.pack(side=BOTTOM, fill=X)
    #     scroll_y.pack(side=RIGHT, fill=Y)
    #
    #     scroll_x.config(command=self.employee_table.xview)
    #     scroll_y.config(command=self.employee_table.yview)
    #
    #
    #
    #     self.employee_table.heading("dep", text="Dep")
    #     self.employee_table.heading("name", text="Name")
    #     self.employee_table.heading("degi", text="Degi")
    #     self.employee_table.heading("email",text="Email")
    #     self.employee_table.heading("address", text="Address")
    #     self.employee_table.heading("married", text="Married")
    #     self.employee_table.heading("dob", text="DOB")
    #     self.employee_table.heading("doj", text="DOJ")
    #     self.employee_table.heading("idproofcomb",text="IDproofcomb")
    #     self.employee_table.heading("idproof", text="IDproof")
    #     self.employee_table.heading("gender", text="Gender")
    #     self.employee_table.heading("phone", text="Phone")
    #     self.employee_table.heading("country", text="Country")
    #     self.employee_table.heading("salary", text="Salary")
    #     self.employee_table["show"] = "headings"
    #
    #     self.employee_table.pack(fill=BOTH, expand=1)
    #
    #     self.employee_table.column("dep", width=100)
    #     self.employee_table.column("name", width=100)
    #     self.employee_table.column("degi", width=100)
    #     self.employee_table.column("email", width=100)
    #     self.employee_table.column("address", width=100)
    #     self.employee_table.column("married", width=100)
    #     self.employee_table.column("dob", width=100)
    #     self.employee_table.column("doj", width=100)
    #     self.employee_table.column("idproofcomb", width=100)
    #     self.employee_table.column("idproof", width=100)
    #     self.employee_table.column("gender", width=100)
    #     self.employee_table.column("phone", width=100)
    #     self.employee_table.column("country", width=100)
    #     self.employee_table.column("salary", width=100)
    #
    #     self.employee_table.pack(fill=BOTH, expand=1)
    #
    #     self.employee_table.bind("<ButtonRelease>",self.get_cursor)
    #
    #     self.fatch_data()
    #
    #
    #
    #
    #     #function
    #
    #
    # def add_data(self):
    #     if self.var_dep.get()=="" or self.var_email.get()=="":
    #         messagebox.showerror("Error","All Fields are Required")
    #     else:
    #         try:
    #             conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="Anuj@123",
    #                                            database="employeemanagmentsystem")
    #             my_cur=conn.cursor()
    #
    #             my_cur.execute("insert into employeedetale values( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
    #
    #                                                                                                                 self.var_dep.get(),
    #                                                                                                                 self.var_name.get(),
    #                                                                                                                 self.var_degi.get(),
    #                                                                                                                 self.var_email.get(),
    #                                                                                                                 self.var_address.get(),
    #                                                                                                                 self.var_married.get(),
    #                                                                                                                 self.var_dob.get(),
    #                                                                                                                 self.var_doj.get(),
    #                                                                                                                 self.var_idproofcomb.get(),
    #                                                                                                                 self.var_idproof.get(),
    #                                                                                                                 self.var_gender.get(),
    #                                                                                                                 self.var_phone.get(),
    #                                                                                                                 self.var_country.get(),
    #                                                                                                                 self.var_salary.get()
    #
    #                                                                                                               ))
    #
    #             conn.commit()
    #             self.fatch_data()
    #             conn.close()
    #             messagebox.showinfo("Success", "Employee Detail has been Added Successfully", parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
    #
    #
    #
    # #fatch data
    #
    # def fatch_data(self):
    #     conn =mysql.connector.connect(host='localhost',username='root',password='Anuj@1232',
    #                                   database='employeemanagmentsystem')
    #     my_cur=conn.cursor()
    #     my_cur.execute('select * from employeedetale')
    #     data= my_cur.fetchall()
    #     if len(data) != 0:
    #         self.employee_table(*self.employee_table.get_children())
    #         for i in data :
    #             self.employee_table.insert("",END,values=i)
    #         conn.commit()
    #
    #     conn.close()
    #
    #
    #  # get cursor
    #
    #
    # def get_cursor(self,event=""):
    #     curses_row=self.employee_table.focus()
    #     content = self.employee_table.item(curses_row)
    #     data= content['values']
    #
    #     self.var_dep.set(data[0])
    #     self.var_name.set(data[1])
    #     self.var_degi.set(data[2])
    #     self.var_email.set(data[3])
    #     self.var_address.set(data[4])
    #     self.var_married.set(data[5])
    #     self.var_dob.set(data[6])
    #     self.var_doj.set(data[7])
    #     self.var_idproofcomb.set(data[8])
    #     self.var_idproof.set(data[9])
    #     self.var_gender.set(data[10])
    #     self.var_phone.set(data[11])
    #     self.var_country.set(data[12])
    #     self.var_salary.set(data[13])
    #
    #
    # def update_data(self):
    #     if self.var_dep.get()=="" or self.var_email.get()=="":
    #         messagebox.showerror("Error","All Fields are Required")
    #     else:
    #         try:
    #             Update = messagebox.askyesno("Update", "Do you Want to update Details", parent=self.root)
    #             if Update > 0:
    #
    #                 conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="Anuj@123",
    #                                            database="employeemanagmentsystem")
    #                 my_cur=conn.cursor()
    #                 my_cur.execute('update employeedetale set Dep=%s,Name=%S,Degi=%s,Email%s,Address=%s,Married=%s,DOB=%s,DOJ=%s,IDproofcomb=%s,IDproof=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s',(
    #
    #                                                                                                                                                                                                 self.var_dep.get(),
    #                                                                                                                                                                                                 self.var_name.get(),
    #                                                                                                                                                                                                 self.var_degi.get(),
    #                                                                                                                                                                                                 self.var_email.get(),
    #                                                                                                                                                                                                 self.var_address.get(),
    #                                                                                                                                                                                                 self.var_married.get(),
    #                                                                                                                                                                                                 self.var_dob.get(),
    #                                                                                                                                                                                                 self.var_doj.get(),
    #                                                                                                                                                                                                 self.var_idproofcomb.get(),
    #                                                                                                                                                                                                 self.var_idproof.get(),
    #                                                                                                                                                                                                 self.var_gender.get(),
    #                                                                                                                                                                                                 self.var_phone.get(),
    #                                                                                                                                                                                                 self.var_country.get(),
    #                                                                                                                                                                                                 self.var_salary.get()
    #
    #                                                                                                                     ))
    #
    #             else:
    #
    #                 if not Update:
    #                     return
    #
    #             messagebox.showinfo("Success", "Update Successfully", parent=self.root)
    #
    #             conn.commit()
    #
    #             self.fatch_data()
    #
    #             conn.close()
    #
    #         except Exception as es:
    #
    #             messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #







if __name__== "__main__":
    root = Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()