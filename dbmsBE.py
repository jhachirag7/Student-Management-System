import sqlite3
import tkinter.messagebox

def checkRepeat(StdID,ClassID):
    con = sqlite3.connect("{}.db".format(ClassID))
    cur = con.cursor()
    cur.execute("SELECT StdID FROM {} WHERE StdID=? LIMIT 1".format(ClassID),(StdID,))

    if cur.fetchone():
        con.commit()
        con.close()
        return False
    else:
        con.commit()
        con.close()
        return True


def studentData(ClassID):
    con = sqlite3.connect("{}.db".format(ClassID))
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, StdID text, Firstname text, Surname text, DOB text, Age text, Gender text, Address text, Mobile text)".format(ClassID))
    con.commit()
    con.close()


def addStdRec(StdID, Firstname, Surname, DOB, Age, Gender, Address, Mobile,ClassID):
    con = sqlite3.connect("{}.db".format(ClassID))
    cur = con.cursor()
    if checkRepeat(StdID,ClassID):
        cur.execute("INSERT INTO {} VALUES (NULL, ?,?,?,?,?,?,?,?)".format(ClassID), (StdID, Firstname, Surname, DOB, Age, Gender, Address, Mobile))
    else:
        tkinter.messagebox.showerror("Error","The student of this id already exists")
    con.commit()
    con.close()

def viewData(ClassID):
    con = sqlite3.connect("{}.db".format(ClassID))
    cur = con.cursor()
    cur.execute("SELECT * FROM {}".format(ClassID))
    row = cur.fetchall()
    con.close()
    return row


def deleteRec(id,ClassID):
    con = sqlite3.connect("{}.db".format(ClassID))
    cur = con.cursor()
    cur.execute("DELETE FROM {} WHERE id=?".format(ClassID),(id,))
    con.commit()
    con.close()


def searchData(StdID="", Firstname="", Surname="", DOB="", Age="", Gender="", Address="", Mobile="",classID=""):
    con = sqlite3.connect("{}.db".format(classID))
    cur = con.cursor()
    cur.execute("SELECT * FROM {} WHERE StdID=? OR Firstname=? OR Surname=? OR DOB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?".format(classID), (StdID, Firstname, Surname, DOB, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    con.close()
    return rows

def updateData(id,StdID="", Firstname="", Surname="", DOB="", Age="", Gender="", Address="", Mobile="",classID=""):
    con = sqlite3.connect("{}.db".format(classID))
    cur = con.cursor()
    cur.execute("UPDATE {} Set StdID=? , Firstname=? , Surname=? , DOB=? , Age=? , Gender=? , Address=? , Mobile=? WHERE id=?".format(classID), (StdID, Firstname, Surname, DOB, Age, Gender, Address, Mobile,id))
    con.commit()
    con.close()
    


