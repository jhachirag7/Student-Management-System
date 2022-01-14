from tkinter import*
import tkinter.messagebox
import RegisterBE
import os


class Register:

    def __init__(self,base):
        self.base = base
        self.base.title("Register Student Class")
        self.base.geometry("700x700+300+50")
        self.base.config(bg="#fb0")
        self.base.iconbitmap("icon.ico")
        self.base.resizable(False,False)

        ClassID=StringVar()
        InCharge=StringVar()
        Key=StringVar()
        ConKey=StringVar()

        def Register():
            if(len(ClassID.get())!=0 and len(InCharge.get())!=0 and len(Key.get())!=0 and len(ConKey.get())!=0):
                if((Key.get())==(ConKey.get())):
                    RegisterBE.studentClass(ClassID.get(),InCharge.get(),Key.get())
                    base.destroy()
                    os.system("Existing.py")
                else:
                    tkinter.messagebox.showerror("Error","Key Fields are mismatched")
            
            else:
                tkinter.messagebox.showerror("Error","Fields can't be empty")

        def Existing():
            base.destroy()
            os.system("Existing.py")
            
        
        MainFrame = Frame(self.base,bg="#fb0")
        MainFrame.grid()
        
        TitFrame=Frame(MainFrame,bg="#FFFFE0",bd=2,padx=0,relief=RIDGE)
        TitFrame.pack(side=TOP,padx=200)

        ButtonFrame=Frame(MainFrame,bg="#fb0",bd=0,padx=0,relief=RIDGE,width=10,height=1)
        ButtonFrame.pack(side=BOTTOM)

        self.lblTit=Label(TitFrame,font=('Times', 30, 'bold'),text="Register Class",bg="#FFFFE0",fg="Red")
        self.lblTit.grid()

        contentFrame=Frame(MainFrame,width=300,height=400,bg="White",bd=4)
        contentFrame.pack(side=TOP,pady=30)

        self.lblClass=Label(contentFrame,font=('Palatino', 15, 'bold'),text="Class:", padx=2, pady=2,bg="White")
        self.lblClass.grid(row=0,column=0,sticky=W,pady=20)
        self.txtClass=Entry(contentFrame,font=('Bookman', 15, 'bold'),textvariable=ClassID,width=30)
        self.txtClass.grid(row=0,column=1)

        self.lblClassIn=Label(contentFrame,font=('Palatino', 15, 'bold'),text="Incharge:", padx=2, pady=2,bg="White")
        self.lblClassIn.grid(row=1,column=0,sticky=W,pady=20)
        self.txtClassIn=Entry(contentFrame,font=('Bookman', 15, 'bold'),textvariable=InCharge,width=30)
        self.txtClassIn.grid(row=1,column=1)
        
        self.lblKey=Label(contentFrame,font=('Palatino', 15, 'bold'),text="Key:", padx=2, pady=2,bg="White")
        self.lblKey.grid(row=2,column=0,sticky=W,pady=20)
        self.txtKey=Entry(contentFrame,font=('Bookman', 15, 'bold'),show="*",textvariable=Key,width=30)
        self.txtKey.grid(row=2,column=1)

        self.lblKey=Label(contentFrame,font=('Palatino', 15, 'bold'),text="Confirm Key:", padx=2, pady=2,bg="White")
        self.lblKey.grid(row=3,column=0,sticky=W,pady=20)
        self.txtKey=Entry(contentFrame,font=('Bookman', 15, 'bold'),show="*",textvariable=ConKey,width=30)
        self.txtKey.grid(row=3,column=1)

        
        self.btnRegister =Button(ButtonFrame,text="Register",font=('Georgia', 15, 'bold'), width=10, height=1, bd=4,command=Register,bg="#F5FFFA")
        self.btnRegister.grid(row=0,column=0,padx=10)
        self.btnRegister =Button(ButtonFrame,text="Existing User",font=('Georgia', 15, 'bold'), width=10, height=1, bd=4,command=Existing,bg="#F5FFFA")
        self.btnRegister.grid(row=0,column=1)

if __name__=='__main__':
    base = Tk()
    application = Register(base)
    base.mainloop()
