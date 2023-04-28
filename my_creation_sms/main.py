'''student management system project in python using tkinter and mysql'''
from functools import partial
from tkinter import *

from tkinter import messagebox
import pymysql
import colors as cs
import database as cr

class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Student Management System")
        self.window.maxsize(width=940 ,  height=680)
        self.window.minsize(width=940 ,  height=680)		

        #self.window.geometry("780x480")
        self.window.config(bg = "white")

        # Customization
        self.color_1 = cs.color_1
        self.color_2 = cs.color_2
        self.color_3 = cs.color_3
        self.color_4 = cs.color_4
        self.font_1 = cs.font_1
        self.font_2 = cs.font_2

        # User Credentials
        self.host = cr.host
        self.user = cr.user
        self.password = cr.password
        self.database = cr.database

        # Left Frame
        self.frame_1 = Frame(self.window, bg=self.color_1)
        self.frame_1.place(x=0, y=0, width=940,height = 100)

        # Right Frame
        self.frame_2 = Frame(self.window, bg = self.color_2)
        self.frame_2.place(x=0,y=100,width=940, height=580)
        

        # Buttons
        self.add_bt = Button(self.frame_1, text='SIGN UP', font=(self.font_1, 12), bd=2, command=self.AddStudent, cursor="hand2",
                      bg=self.color_1,fg=self.color_3).place(x=68,y=40,width=90)
        self.view_bt = Button(self.frame_1, text='LOG IN', font=(self.font_1, 12), bd=2, command=self.GetContact_View,
                      cursor="hand2", bg=self.color_1,fg=self.color_3).place(x=188,y=40,width=90)
        self.update_bt = Button(self.frame_1, text='UPDATE', font=(self.font_1, 12), bd=2, command=self.GetContact_Update, cursor="hand2",
                      bg=self.color_1,fg=self.color_3).place(x=308,y=40,width=90)
        self.delete_bt = Button(self.frame_1, text='DELETE', font=(self.font_1, 12), bd=2, command=self.GetContact_Delete,cursor="hand2",
                      bg=self.color_1,fg=self.color_3).place(x=428,y=40,width=90)
        self.clear_bt = Button(self.frame_1, text='CLEAR', font=(self.font_1, 12), bd=2, command=self.ClearScreen, cursor="hand2",
                      bg=self.color_1,fg=self.color_3).place(x=548,y=40,width=90)
        
        self.date_bt = Button(self.frame_1, text='DATE', font=(self.font_1, 12), bd=2, command=self.date,cursor="hand2", bg=self.color_1,
                      fg=self.color_3).place(x=668,y=40,width=90)
        self.exit_bt = Button(self.frame_1, text='EXIT', font=(self.font_1, 12), bd=2, command=self.Exit,cursor="hand2", bg=self.color_1,
                      fg=self.color_3).place(x=788,y=40,width=90)



    '''Widgets for adding student data'''
    def AddStudent(self):
        self.ClearScreen()

        self.name = Label(self.frame_2, text="First Name", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=20)
        self.name_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.name_entry.place(x=100,y=50, width=200)

        self.surname = Label(self.frame_2, text="Last Name", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=20)
        self.surname_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.surname_entry.place(x=530,y=50, width=200)

        self.course = Label(self.frame_2, text="Course", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=80)
        self.course_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.course_entry.place(x=100,y=110, width=200)

        self.Course_Package = Label(self.frame_2, text="Course Package", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=80)
        self.Course_Package_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Course_Package_entry.place(x=530,y=110, width=200)

        self.date = Label(self.frame_2, text="Date", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=140)
        self.date_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.date_entry.place(x=100,y=170, width=200)

        self.age = Label(self.frame_2, text="Age", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=140)
        self.age_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.age_entry.place(x=530,y=170, width=200)

        self.gender = Label(self.frame_2, text="Gender", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=200)
        self.gender_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.gender_entry.place(x=100,y=230, width=200)

        self.birth = Label(self.frame_2, text="Birthday", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=200)
        self.birth_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.birth_entry.place(x=530,y=230, width=200)

        self.contact = Label(self.frame_2, text="Contact No", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=260)
        self.contact_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.contact_entry.place(x=100,y=290, width=200)

        self.email = Label(self.frame_2, text="Email", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=260)
        self.email_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.email_entry.place(x=530,y=290, width=200)

        self.Current_Course = Label(self.frame_2, text="Current Course", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=320)
        self.Current_Course_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Current_Course_entry.place(x=100,y=350, width=200)

        self.Pending_Course = Label(self.frame_2, text="Pending Course", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=320)
        self.Pending_Course_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Pending_Course_entry.place(x=530,y=350, width=200)

        self.Completed_Course = Label(self.frame_2, text="Completed Course", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=380)
        self.Completed_Course_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Completed_Course_entry.place(x=100,y=410, width=200)

        self.Total_Fees = Label(self.frame_2, text="Total Fees", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=380)
        self.Total_Fees_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Total_Fees_entry.place(x=530,y=410, width=200)

        self.Paid_Fees = Label(self.frame_2, text="Paid Fees", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=440)
        self.Paid_Fees_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Paid_Fees_entry.place(x=100,y=470, width=200)

        self.Balance_Fees = Label(self.frame_2, text="Balance Fees", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=440)
        self.Balance_Fees_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Balance_Fees_entry.place(x=530,y=470, width=200)

        self.submit_bt_1 = Button(self.frame_2, text='Submit', font=(self.font_1, 12), bd=2, command=self.Submit, cursor="hand2",
        bg=self.color_1,fg=self.color_3).place(x=365,y=520,width=100)


    '''Get the contact number to show a student details'''
    def GetContact_View(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_2, text="Enter Contact Number", font=(self.font_2, 18, "bold"), bg=self.color_2).place(x=332,y=170)
        self.getInfo_entry = Entry(self.frame_2, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=360, y=220, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_2, text='Submit', font=(self.font_1, 10), bd=2, command=self.CheckContact_View, cursor="hand2", 
        bg=self.color_1,fg=self.color_3).place(x=420,y=280,width=80)
            
    '''To update a student details, get the contact number'''
    def GetContact_Update(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_2, text="Enter Contact Number", font=(self.font_2, 18, "bold"), bg=self.color_2).place(x=332,y=170)
        self.getInfo_entry = Entry(self.frame_2, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=360, y=220, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_2, text='Submit', font=(self.font_1, 10), bd=2, command=self.CheckContact_Update, cursor="hand2",
         bg=self.color_1,fg=self.color_3).place(x=420,y=280,width=80)

    '''Get the contact number to delete a student record'''
    def GetContact_Delete(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_2, text="Enter Contact Number", font=(self.font_2, 18, "bold"), bg=self.color_2).place(x=332,y=170)
        self.getInfo_entry = Entry(self.frame_2, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=360, y=220, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_2, text='Submit', font=(self.font_1, 10), bd=2, command=self.DeleteData, cursor="hand2", 
        bg=self.color_1,fg=self.color_3).place(x=420,y=280,width=80)

    '''get date to view details'''
    def date(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_2, text="Enter Date", font=(self.font_2, 18, "bold"), bg=self.color_2).place(x=400,y=170)
        self.getInfo_entry = Entry(self.frame_2, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=365, y=220, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_2, text='Submit', font=(self.font_1, 10), bd=2, command=self.Checkdate_View, cursor="hand2", 
        bg=self.color_1,fg=self.color_3).place(x=420,y=280,width=80)

    '''Remove all widgets from the frame 1'''
    def ClearScreen(self):
        for widget in self.frame_2.winfo_children():
            widget.destroy()

    '''Exit window'''
    def Exit(self):
        self.window.destroy()

    '''
    Checks whether the contact number is available or not. If available, 
    the function calls the 'ShowDetails' function to display the result.
    '''
    def CheckContact_View(self):
       if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your contact number",parent=self.window)
       else:
           try:
               connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
               curs = connection.cursor()
               curs.execute("select * from student_register where contact=%s", self.getInfo_entry.get())
               row=curs.fetchone()
               if row == None:
                   messagebox.showerror("Error!","Contact number doesn't exists",parent=self.window)
               else:
                   self.ShowDetails(row)
                   connection.close()
           except Exception as e:
               messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    '''
    Checks whether the contact date is available or not. If available, 
    the function calls the 'ShowDetails' function to display the result.
    '''
    def Checkdate_View(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your contact number",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where date=%s", self.getInfo_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Contact number doesn't exists",parent=self.window)
                else:
                    self.ShowDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)




    '''
    Checks whether the contact number is available or not. If available, 
    the function calls the 'GetUpdateDetails' function to get the new data to perform
    update operation.
    '''
    def CheckContact_Update(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your contact number",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", self.getInfo_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Contact number doesn't exists",parent=self.window)
                else:
                    self.GetUpdateDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    
    '''Clears a student record'''
    def DeleteData(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your contact number",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", self.getInfo_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Contact number doesn't exists",parent=self.window)
                else:
                    curs.execute("delete from student_register where contact=%s", self.getInfo_entry.get())
                    connection.commit()
                    messagebox.showinfo('Done!', "The data has been deleted")
                    connection.close()
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)


    '''Gets the data that the user wants to update to perform the update operation'''
    def GetUpdateDetails(self, row):
        self.ClearScreen()

        self.name = Label(self.frame_2, text="First Name", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=20)
        self.name_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.name_entry.insert(0, row[0])
        self.name_entry.place(x=100,y=50, width=200,height=22)

        self.surname = Label(self.frame_2, text="Last Name", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=20)
        self.surname_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.surname_entry.insert(0, row[1])
        self.surname_entry.place(x=530,y=50, width=200,height=22)

        self.course = Label(self.frame_2, text="Course", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=80)
        self.course_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.course_entry.insert(0, row[2])
        self.course_entry.place(x=100,y=110, width=200,height=22)

        self.Course_Package = Label(self.frame_2, text="Course Package", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=80)
        self.Course_Package_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Course_Package_entry.insert(0, row[3])
        self.Course_Package_entry.place(x=530,y=110, width=200,height=22)

        self.date = Label(self.frame_2, text="Date", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=140)
        self.date_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.date_entry.insert(0, row[4])
        self.date_entry.place(x=100,y=170, width=200,height=22)

        self.age = Label(self.frame_2, text="Age", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=140)
        self.age_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.age_entry.insert(0, row[5])
        self.age_entry.place(x=530,y=170, width=200,height=22)

        self.gender = Label(self.frame_2, text="Gender", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=200)
        self.gender_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.gender_entry.insert(0, row[6])
        self.gender_entry.place(x=100,y=230, width=200,height=22)

        self.birth = Label(self.frame_2, text="Birthday", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=200)
        self.birth_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.birth_entry.insert(0, row[7])
        self.birth_entry.place(x=530,y=230, width=200,height=22)

        contact = Label(self.frame_2, text="Contact", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=260)
        contact_data = Label(self.frame_2, text=row[8], font=(self.font_1, 10)).place(x=100, y=290)
        #contact_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        #contact_entry.insert(0, row[8])
        #contact_entry.place(x=100,y=410, width=200,height=22)

        self.email = Label(self.frame_2, text="Email", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=260)
        self.email_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.email_entry.insert(0, row[9])
        self.email_entry.place(x=530,y=290, width=200,height=22)

        self.Current_Course = Label(self.frame_2, text="Current Course", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=320)
        self.Current_Course_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Current_Course_entry.insert(0, row[10])
        self.Current_Course_entry.place(x=100,y=350, width=200,height=22)

        self.Pending_Course = Label(self.frame_2, text="Pending Course", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=320)
        self.Pending_Course_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Pending_Course_entry.insert(0, row[11])
        self.Pending_Course_entry.place(x=530,y=350, width=200,height=22)

        self.Completed_Course = Label(self.frame_2, text="Completed Course", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=380)
        self.Completed_Course_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Completed_Course_entry.insert(0, row[12])
        self.Completed_Course_entry.place(x=100,y=410, width=200,height=22)

        self.Total_Fees = Label(self.frame_2, text="Total Fees", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=380)
        self.Total_Fees_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Total_Fees_entry.insert(0, row[13])
        self.Total_Fees_entry.place(x=530,y=410, width=200,height=22)

        self.Paid_Fees = Label(self.frame_2, text="Paid Fees", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=440)
        
        self.Paid_Fees_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Paid_Fees_entry.insert(0,row[14])
        self.Paid_Fees_entry.place(x=100,y=470, width=200,height=22)
        

        self.Balance_Fees = Label(self.frame_2, text="Balance Fees", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=440)
        self.Balance_Fees_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.Balance_Fees_entry.insert(0, row[15])
        self.Balance_Fees_entry.place(x=530,y=470, width=200,height=22)

        self.submit_bt_1 = Button(self.frame_2, text='Submit', font=(self.font_1, 12), bd=2, command=partial(self.UpdateDetails, row), 
        cursor="hand2", bg=self.color_1,fg=self.color_3).place(x=300,y=520,width=100)
        self.cancel_bt = Button(self.frame_2, text='Cancel', font=(self.font_1, 12), bd=2, command=self.ClearScreen, cursor="hand2", 
        bg=self.color_1,fg=self.color_3).place(x=420,y=520,width=100)

    
    '''Within frame 1, it displays information about a student'''
    def ShowDetails(self, row):
        self.ClearScreen()
        name = Label(self.frame_2, text="First Name", font=(self.font_2,15,"bold"), bg=self.color_5).place(x=100,y=20)
        name_data = Label(self.frame_2, text=row[0], font=(self.font_1, 10)).place(x=100, y=50)

        surname = Label(self.frame_2, text="Last Name", font=(self.font_2, 15, "bold"), bg=self.color_5).place(x=530,y=20)
        surname_data = Label(self.frame_2, text=row[1], font=(self.font_1, 10)).place(x=530, y=50)

        course = Label(self.frame_2, text="Course", font=(self.font_2, 15, "bold"), bg=self.color_5).place(x=100,y=80)
        course_data = Label(self.frame_2, text=row[2], font=(self.font_1, 10)).place(x=100, y=110)

        Course_Package = Label(self.frame_2, text="Course Package", font=(self.font_2, 15, "bold"), bg=self.color_5).place(x=530,y=80)
        Course_Package = Label(self.frame_2, text=row[3], font=(self.font_1, 10)).place(x=530, y=110)

        Date = Label(self.frame_2, text="Date", font=(self.font_2, 15, "bold"), bg=self.color_5).place(x=100,y=140)
        Date_data = Label(self.frame_2, text=row[4], font=(self.font_1, 10)).place(x=100, y=170)

        age = Label(self.frame_2, text="Age", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=140)
        age_data = Label(self.frame_2, text=row[5], font=(self.font_1, 10)).place(x=530, y=170)

        gender= Label(self.frame_2, text="Gender", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=200)
        gender_data = Label(self.frame_2, text=row[6], font=(self.font_1, 10)).place(x=100, y=230)

        birth = Label(self.frame_2, text="DOB", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=200)
        birth_data = Label(self.frame_2, text=row[7], font=(self.font_1, 10)).place(x=530, y=230)

        contact = Label(self.frame_2, text="Contact No", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=260)
        contact_data = Label(self.frame_2, text=row[8], font=(self.font_1, 10)).place(x=100, y=290)

        email = Label(self.frame_2, text="Email", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=260)
        email_data = Label(self.frame_2, text=row[9], font=(self.font_1, 10)).place(x=530, y=290)

        Current_Course = Label(self.frame_2, text="Current Course", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=320)
        Current_Course_data= Label(self.frame_2, text=row[10], font=(self.font_1, 10)).place(x=100, y=350)

        Pending_Course = Label(self.frame_2, text="Pending Course", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=320)
        Pending_Course_data = Label(self.frame_2, text=row[11], font=(self.font_1, 10)).place(x=530, y=350)

        Completed_Course = Label(self.frame_2, text="Completed Course", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=380)
        Completed_Course_data = Label(self.frame_2, text=row[12], font=(self.font_1, 10)).place(x=100, y=410)

        Total_Fees = Label(self.frame_2, text="Total Fees", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=380)
        Total_Fees_data = Label(self.frame_2, text=row[13], font=(self.font_1, 10)).place(x=530, y=410)

        Paid_Fees = Label(self.frame_2, text="Paid Fees", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=100,y=440)
        Paid_Fees_data = Label(self.frame_2, text=row[14], font=(self.font_1, 10)).place(x=100, y=470)

        Balance_Fees = Label(self.frame_2, text="Balance Fees", font=(self.font_2, 15, "bold"), bg=self.color_2).place(x=530,y=440)
        Balance_Fees_data = Label(self.frame_2, text=row[15], font=(self.font_1, 10)).place(x=530, y=470)


    '''Updates student data'''
    def UpdateDetails(self, row):
        if( self.name_entry.get() == "" or self.surname_entry.get() == "" or self.course_entry.get() == "" or self.Course_Package_entry.get() == "" or 
        self.date_entry.get() == "" or self.age_entry.get() == "" or self.gender_entry.get() == "" or self.birth_entry.get() == "" or self.email_entry.get() == "" or
            self.Current_Course_entry.get()== "" or self.Pending_Course_entry.get()=="" or  self.Completed_Course_entry.get()=="" or self.Total_Fees_entry.get()=="" or
            self.Paid_Fees_entry.get()== "" or self.Balance_Fees_entry.get()== ""):
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", row[8])
                row=curs.fetchone()

                if row==None:
                    messagebox.showerror("Error!","The contact number doesn't exists",parent=self.window)
                else:
                    curs.execute("update student_register set f_name=%s,l_name=%s, course=%s, course_Package=%s, date=%s, age=%s, gender=%s, birth=%s,email=%s,current_course=%s,pending_course=%s,completed_course=%s,total_fees=%s,paid_fees=%s,balance_fees=%s where contact=%s",
                                        (
                                            self.name_entry.get(),
                                            self.surname_entry.get(),
                                            self.course_entry.get(),
                                            self.Course_Package_entry.get(),
                                            self.date_entry.get(),
                                            self.age_entry.get(),
                                            self.gender_entry.get(),
                                            self.birth_entry.get(),
                                            self.email_entry.get(),
                                            self.Current_Course_entry.get(),
                                            self.Pending_Course_entry.get(),
                                            self.Completed_Course_entry.get(),
                                            self.Total_Fees_entry.get(),
                                            self.Paid_Fees_entry.get(),
                                            self.Balance_Fees_entry.get(),
                                            row[8]
                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been updated")
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
    
    
    '''It adds the information of new students'''
    def Submit(self):
        if (self.name_entry.get() == "" or self.surname_entry.get() == "" or self.course_entry.get() == "" or self.Course_Package_entry.get() == "" or 
        self.date_entry.get() == "" or self.age_entry.get() == "" or self.gender_entry.get() == "" or self.birth_entry.get() == "" or self.contact_entry.get() == "" 
        or self.email_entry.get() == "" or self.Current_Course_entry.get()== "" or self.Pending_Course_entry.get() == "" or  self.Completed_Course_entry.get()== "" or self.Total_Fees_entry.get()== "" or
            self.Paid_Fees_entry.get()== "" or self.Balance_Fees_entry.get()== ""):
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", self.contact_entry.get())
                row=curs.fetchone()

                if row!=None:
                    messagebox.showerror("Error!","The contact number is already exists, please try again with another number",parent=self.window)
                else:
                    curs.execute("insert into student_register (f_name,l_name,course,course_package,date,age,gender,birth,contact,email,current_course,pending_course,completed_course,Total_fees,paid_fees,balance_fees)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (
                                            self.name_entry.get(),
                                            self.surname_entry.get(),
                                            self.course_entry.get(),
                                            self.Course_Package_entry.get(),
                                            self.date_entry.get(),
                                            self.age_entry.get(),
                                            self.gender_entry.get(),
                                            self.birth_entry.get(),
                                            self.contact_entry.get(),
                                            self.email_entry.get(),
                                            self.Current_Course_entry.get(),
                                            self.Pending_Course_entry.get(),
                                            self.Completed_Course_entry.get(),
                                            self.Total_Fees_entry.get(),
                                            self.Paid_Fees_entry.get(),
                                            self.Balance_Fees_entry.get()
                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been submitted")
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    '''Reset all the entry fields'''
    def reset_fields(self):
        self.name_entry.delete(0, END)
        self.surname_entry.delete(0, END)
        self.course_entry.delete(0, END)
        self.Course_Package_entry.delete(0, END)
        self.date_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.gender_entry.delete(0, END)
        self.birth_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.Current_Course_entry.delete(0, END)
        self.Pending_Course_entry.delete(0, END)
        self.Completed_Course_entry.delete(0, END)
        self.Total_Fees_entry.delete(0, END)
        self.Paid_Fees_entry.delete(0, END)
        self.Balance_Fees_entry.delete(0, END)

# The main function
if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop
