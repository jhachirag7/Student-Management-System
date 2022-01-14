from tkinter import*
import tkinter.messagebox
import RegisterBE
import dbmsFE
import os

class Login:

    def __init__(self,base):
        self.base = base
        self.base.title("Existing Student Class")
        self.base.geometry("700x700+300+50")
        self.base.config(bg="#fb0")
        self.base.iconbitmap("icon.ico")
        self.base.resizable(False,False)

        ClassID=StringVar()
        InCharge=StringVar()
        Key=StringVar()

        def Login():
            if(len(ClassID.get())!=0 and len(Key.get())!=0):
               Check = RegisterBE.LoginCheck(ClassID.get(),Key.get())
               if Check:
                   name=ClassID.get()
            
                   dbmsFE.main(name)
               else:
                    tkinter.messagebox.showerror("Error","Invalid Credentials")
            else:
                tkinter.messagebox.showerror("Error","Fields are be empty")

        def New():
            base.destroy()
            os.system("Register.py")
            
        
        MainFrame = Frame(self.base,bg="#fb0")
        MainFrame.grid()
        
        TitFrame=Frame(MainFrame,bg="#FFFFE0",bd=2,padx=0,relief=RIDGE)
        TitFrame.pack(side=TOP,padx=200)

        ButtonFrame=Frame(MainFrame,bg="#fb0",bd=0,padx=0,relief=RIDGE,width=10,height=1)
        ButtonFrame.pack(side=BOTTOM)

        self.lblTit=Label(TitFrame,font=('Times', 30, 'bold'),text="Login Class",bg="#FFFFE0",fg="Red")
        self.lblTit.grid()

        contentFrame=Frame(MainFrame,width=300,height=400,bg="White",bd=4)
        contentFrame.pack(side=TOP,pady=30)

        self.lblClass=Label(contentFrame,font=('Palatino', 15, 'bold'),text="Class:", padx=2, pady=2,bg="White")
        self.lblClass.grid(row=0,column=0,sticky=W,pady=20)
        self.txtClass=Entry(contentFrame,font=('Bookman', 15, 'bold'),textvariable=ClassID,width=30)
        self.txtClass.grid(row=0,column=1)

        
        self.lblKey=Label(contentFrame,font=('Palatino', 15, 'bold'),text="Key:", padx=2, pady=2,bg="White")
        self.lblKey.grid(row=2,column=0,sticky=W,pady=20)
        self.txtKey=Entry(contentFrame,font=('Bookman', 15, 'bold'),show="*",textvariable=Key,width=30)
        self.txtKey.grid(row=2,column=1)

        
        self.btnRegister =Button(ButtonFrame,text="Open",font=('Georgia', 15, 'bold'), width=10, height=1, bd=4,command=Login,bg="#F5FFFA")
        self.btnRegister.grid(row=0,column=0,padx=10)
        self.btnRegister =Button(ButtonFrame,text="New Class",font=('Georgia', 15, 'bold'), width=10, height=1, bd=4,command=New,bg="#F5FFFA")
        self.btnRegister.grid(row=0,column=1)




if __name__=='__main__':
    base = Tk()
    application = Login(base)
    base.mainloop()
