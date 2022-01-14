from tkinter import*
import tkinter.messagebox
import dbmsBE
class Student:
    
    def __init__(self,root,ClassID):

        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1400x650+50+50")
        self.root.config(bg="#fb0")
        self.root.iconbitmap("icon.ico")
        self.root.resizable(False,False)

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DOB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        #=================================================================================================================================================================================#


        dbmsBE.studentData(ClassID)

        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Database Management System", "Confirm you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtStdID.delete(0,END)
            self.txtfnam.delete(0,END)
            self.txtSnam.delete(0,END)
            self.txtDOB.delete(0,END)
            self.txtAge.delete(0,END)
            self.txtGender.delete(0,END)
            self.txtAdr.delete(0,END)
            self.txtMob.delete(0,END)

        def addData():
            if(len(StdID.get())!=0 and len(Firstname.get())!=0 and len(DOB.get())!=0 and len(Age.get())!=0 and len(Gender.get())!=0 and len(Mobile.get())!=0):
                dbmsBE.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get(),ClassID)
                studentlist.delete(0,END)
                studentlist.insert(END,StdID.get(), Firstname.get(), Surname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
            else:
                tkinter.messagebox.showerror("Error","Fields can't be empty")


        def DisplayData():
            studentlist.delete(0,END)
            for row in dbmsBE.viewData(ClassID):
                studentlist.insert(END,row,str(""))

        def StudentRec(event):
            global sd
            try:
                searchStd = studentlist.curselection()[0]
                sd = studentlist.get(searchStd)
                self.txtStdID.delete(0,END)
                self.txtStdID.insert(END,sd[1])
                self.txtfnam.delete(0,END)
                self.txtfnam.insert(END,sd[2])
                self.txtSnam.delete(0,END)
                self.txtSnam.insert(END,sd[3])
                self.txtDOB.delete(0,END)
                self.txtDOB.insert(END,sd[4])
                self.txtAge.delete(0,END)
                self.txtAge.insert(END,sd[5])
                self.txtGender.delete(0,END)
                self.txtGender.insert(END,sd[6])
                self.txtAdr.delete(0,END)
                self.txtAdr.insert(END,sd[7])
                self.txtMob.delete(0,END)
                self.txtMob.insert(END,sd[8])
            except:
                pass
            

        def DeleteData():
            if(len(StdID.get())!=0):
               dbmsBE.deleteRec(sd[0],ClassID)
               clearData()
               DisplayData()

        def searchDatabase():
            studentlist.delete(0,END)
            for row in dbmsBE.searchData(StdID.get(), Firstname.get(), Surname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get(),ClassID):
               studentlist.insert(END,row,str("")) 
               


        def update():
            if(len(StdID.get())!=0 and len(Firstname.get())!=0 and len(DOB.get())!=0 and len(Age.get())!=0 and len(Gender.get())!=0 and len(Mobile.get())!=0):
               dbmsBE.updateData(sd[0],StdID.get(), Firstname.get(), Surname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get(),ClassID)
               studentlist.delete(0,END)
               studentlist.insert(END,StdID.get(), Firstname.get(), Surname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
            else:
                tkinter.messagebox.showerror("Error","Fields can't be empty")


               




        #=================================================================================================================================================================================#


        MainFrame = Frame(self.root,bg="#fb0")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2,padx=54, pady=8, bg="#FFFFE0",relief =RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame,font=('Times', 47, 'bold'),text="Student Database Management System",bg="#FFFFE0",fg="Red")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="grey",relief =RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1,padx=20,width=1300, height=400, pady=20, bg="#FAEBD7",relief =RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1,padx=20,width=1000, height=600,relief =RIDGE,font=('Verdana italic',20,'bold'), text="Student Info\n",bg="#696969",fg="#FFFAFA")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1,padx=31,width=450, height=300, pady=3, bg="#696969",relief =RIDGE, font=('Verdana italic',20,'bold'), text="Student Details\n",fg="#FFFAFA")
        DataFrameRight.pack(side=RIGHT)
        #==================================================================================================================================================================================#

        self.lblStdID = Label(DataFrameLeft,font=('Palatino', 20, 'bold'),text="Student ID:", padx=2, pady=2, bg="#696969",fg="white")
        self.lblStdID.grid(row=0,column=0,sticky=W)
        self.txtStdID = Entry(DataFrameLeft,font=('Bookman', 20, 'bold'),textvariable=StdID,width=39)
        self.txtStdID.grid(row=0,column=1)

        self.lblfnam = Label(DataFrameLeft,font=('Palatino', 20, 'bold'),text="Firstname:", padx=2, pady=2, bg="#696969",fg="white")
        self.lblfnam.grid(row=1,column=0,sticky=W)
        self.txtfnam = Entry(DataFrameLeft,font=('Bookman', 20, 'bold'),textvariable=Firstname,width=39)
        self.txtfnam.grid(row=1,column=1)

        self.lblDOB = Label(DataFrameLeft,font=('Palatino', 20, 'bold'),text="Date of Birth:", padx=2, pady=2, bg="#696969",fg="white")
        self.lblDOB.grid(row=3,column=0,sticky=W)
        self.txtDOB = Entry(DataFrameLeft,font=('Bookman', 20, 'bold'),textvariable=DOB,width=39)
        self.txtDOB.grid(row=3,column=1)

        self.lblAge = Label(DataFrameLeft,font=('Palatino', 20, 'bold'),text="Age:", padx=2, pady=2, bg="#696969",fg="white")
        self.lblAge.grid(row=4,column=0,sticky=W)
        self.txtAge = Entry(DataFrameLeft,font=('Bookman', 20, 'bold'),textvariable=Age,width=39)
        self.txtAge.grid(row=4,column=1)

        self.lblGender = Label(DataFrameLeft,font=('Palatino', 20, 'bold'),text="Gender:", padx=2, pady=2, bg="#696969",fg="white")
        self.lblGender.grid(row=5,column=0,sticky=W)
        self.txtGender = Entry(DataFrameLeft,font=('Bookman', 20, 'bold'),textvariable=Gender,width=39)
        self.txtGender.grid(row=5,column=1)

        self.lblAdr = Label(DataFrameLeft,font=('Palatino', 20, 'bold'),text="Address:", padx=2, pady=2, bg="#696969",fg="white")
        self.lblAdr.grid(row=6,column=0,sticky=W)
        self.txtAdr = Entry(DataFrameLeft,font=('Bookman', 20, 'bold'),textvariable=Address,width=39)
        self.txtAdr.grid(row=6,column=1)

        self.lblMob = Label(DataFrameLeft,font=('Palatino', 20, 'bold'),text="Mobile:", padx=2, pady=2,bg="#696969",fg="white")
        self.lblMob.grid(row=7,column=0,sticky=W)
        self.txtMob = Entry(DataFrameLeft,font=('Bookman', 20, 'bold'),textvariable=Mobile,width=39)
        self.txtMob.grid(row=7,column=1)

        self.lblSnam = Label(DataFrameLeft,font=('Palatino', 20, 'bold'),text="Surname:", padx=2, pady=2,bg="#696969",fg="white")
        self.lblSnam.grid(row=2,column=0,sticky=W)
        self.txtSnam = Entry(DataFrameLeft,font=('Bookman', 20, 'bold'),textvariable=Surname,width=39)
        self.txtSnam.grid(row=2,column=1)
        #==================================================================================================================================================================================#


        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0,column=1,sticky='ns')

        studentlist = Listbox(DataFrameRight,width=50,font=('Times New Roman', 12, 'bold'), height=16, yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0,padx=8)
        scrollbar.config(command = studentlist.yview)
        #==================================================================================================================================================================================#

        self.btnAddData = Button(ButtonFrame, text="Add New", font=('Georgia', 20, 'bold'), width=10, height=1, bd=4,command=addData,bg="#F5FFFA")
        self.btnAddData.grid(row=0,column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('Georgia', 20, 'bold'), width=10, height=1, bd=4, command=DisplayData, bg="#F5FFFA")
        self.btnDisplayData.grid(row=0,column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('Georgia', 20, 'bold'), width=10, height=1, bd=4, command=clearData, bg="#F5FFFA")
        self.btnClearData.grid(row=0,column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('Georgia', 20, 'bold'), width=10, height=1, bd=4, command=DeleteData, bg="#F5FFFA")
        self.btnDeleteData.grid(row=0,column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('Georgia', 20, 'bold'), width=10, height=1, bd=4, command=searchDatabase, bg="#F5FFFA")
        self.btnSearchData.grid(row=0,column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('Georgia', 20, 'bold'), width=10, height=1, bd=4,command=update, bg="#F5FFFA")
        self.btnUpdateData.grid(row=0,column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('Georgia', 20, 'bold'), width=10, height=1, bd=4,command=iExit, bg="#F5FFFA")
        self.btnExit.grid(row=0,column=6)


def main(uclass):
    root = Toplevel()
    application = Student(root,uclass)
    root.mainloop()
    
