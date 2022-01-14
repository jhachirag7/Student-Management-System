import sqlite3
import tkinter.messagebox

def checkRepeat(Class):
    con = sqlite3.connect("Classes.db")
    cur = con.cursor()
    cur.execute("SELECT Class FROM Classes WHERE Class=? LIMIT 1",(Class,))

    if cur.fetchone():
        con.commit()
        con.close()
        return False
    else:
        con.commit()
        con.close()
        return True

def LoginCheck(Class,Key):
    con = sqlite3.connect("Classes.db")
    cur = con.cursor()
    cur.execute("SELECT Class,Pass FROM Classes WHERE Class=? AND Pass=? LIMIT 1",(Class,Key))
    if cur.fetchone():
        con.commit()
        con.close()
        return True
    else:
        con.commit()
        con.close()
        return False


def classes():
    con=sqlite3.connect("Classes.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Classes(id INTEGER PRIMARY KEY,Class text,Incharge text,Pass text)")
    con.commit()
    con.close()

def studentClass(Class,Incharge,key):
    con=sqlite3.connect("Classes.db")
    cur=con.cursor()
    if checkRepeat(Class):
        cur.execute("INSERT INTO Classes VALUES(NULL, ?,?,?)",(Class,Incharge,key))
    else:
        tkinter.messagebox.showerror("Error","This Class already exists")
    con.commit()
    con.close()


classes()

