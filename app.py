from tkinter import *
import tkinter.messagebox
import sqlite3
from datetime import *
from datetime import datetime, date


    
class Product2:
    def __init__(self,root):
        
        d = Database()
        
        self.root = root
        self.root.title("Pharmacy Data Management System")
        self.root.geometry("575x620")
        self.root.config(bg="yellow")


        Date=StringVar()


       

        def showing():
            print(showing)
            productList.delete(0,END)
            for row in d.show():
                productList.insert(END,row,str(""))
            print("showing finish\n")
            
        def Check():
            print("search")
            a=self.txtDate.get()
            print(a)
            productList.delete(0,END)
            for row in d.compare(a):
                productList.insert(END,row,str(""))
            print("search finish")


        def close():
            print("close")
            close = tkinter.messagebox.askyesno("Pharmacy Data Management System",
                            "Really want to close the system?")
            if close>0:
                root.destroy()
                print("close finish\n")
                return

        MainFrame= Frame(self.root,bg="red")
        MainFrame.grid()

        HeaderFrame = Frame(MainFrame, bd=1, padx=50, pady=10, bg='white', relief=RIDGE)
        HeaderFrame.pack(side=TOP)

        self.ITitle = Label(HeaderFrame, font=('arial',45,'bold'), fg="red",
                            text = "Check for expiry", bg="white")
        self.ITitle.grid()

        OperationFrame = Frame(MainFrame,bd=3,width=1025,height=50, padx=50,
                               pady=20,bg="white",relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)


        BodyFrame = Frame(MainFrame,bd=3,width=975,height=400, padx=30,
                               pady=20,bg="white",relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        LeftFrame = LabelFrame(BodyFrame,bd=2,width=300,height=380, padx=20,
                               pady=10,bg="yellow",relief=RIDGE, font=('arial',15,'bold'),
                               text="  Date  ")

        LeftFrame.pack(side=TOP)


        
        RightFrame = LabelFrame(BodyFrame,bd=2,width=500,height=380, padx=20,
                            pady=10,bg="yellow",relief=RIDGE,
                            font=('arial',15,'bold'),
                            text="  Products that will be expired by this date  ")

        RightFrame.pack(side=BOTTOM)


        '''Add the Widgets to top'''


        
        self.labelDate = Label(LeftFrame,font=('arial',15,'bold'),
                                text="Date :",pady=2,
                              padx=1,bg="white",fg="blue")
        self.labelDate.grid(row=5,column=0,stick=W)
        

        
        self.txtDate = Entry(LeftFrame,font=('arial',20,'bold'),
                              textvariable=Date,
                            width=20)
        self.txtDate.grid(row=5,column=1,stick=W)      




        ''' Add scroll bar'''
        scroll = Scrollbar(RightFrame)
        scroll.grid(row=0,column=1,sticky="ns")

        productList = Listbox(RightFrame, width=60, height=14,
                        font=('arial',10,'normal'),yscrollcommand=scroll.set)
        productList.grid(row=0,column=0,padx=6)
        scroll.config(command=productList.yview)

        '''Add buttons'''
        self.buttonCheck = Button(OperationFrame,text="Check",width=9,
                                   font=('arial',15,'bold'),height=1, bd=4,
                                   command=Check)
        self.buttonCheck.grid(row=0,column=0)


        self.buttonShow = Button(OperationFrame,text="Show",width=9,
                                   font=('arial',15,'bold'),height=1, bd=4,
                                 command=showing)
        self.buttonShow.grid(row=0,column=1)

        self.buttonClose = Button(OperationFrame,text="Close",width=9,
                                   font=('arial',15,'bold'),height=1, bd=4,
                                 command=close)
        self.buttonClose.grid(row=0,column=2)


class Product:
    def __init__(self,root):
        d = Database()
        #d.conn()
        
        self.root = root
        self.root.title("Pharmacy Data Management System")
        self.root.geometry("1150x650")
        self.root.config(bg="yellow")


        pId=StringVar()
        pName=StringVar()
        pPrice=StringVar()
        pQuantity=StringVar()
        pCompany=StringVar()
        pExpiryDate=StringVar()
        pSymptoms=StringVar()

        #pIdpNamepPricepQuantitypCompanypExpiryDate

        '''lets call the database class methods to perform database operation'''

        def close():
            print("close")
            close = tkinter.messagebox.askyesno("Pharmacy Data Management System",
                            "Really want to close the system?")
            if close>0:
                root.destroy()
                print("close finish\n")
                return

            
        def clear():
            print("clear")
            self.txtpID.delete(0,END)
            self.txtpName.delete(0,END)
            self.txtpPrice.delete(0,END)
            self.txtpQuantity.delete(0,END)
            self.txtpCompany.delete(0,END)
            self.txtpExpiryDate.delete(0,END)
            self.txtpSymptoms.delete(0,END)
            print("clear finish\n")

        def insert():
            print("insert")
            if (len(pId.get())!=0 and len(pName.get())!=0 and
                len(pPrice.get())!=0 and len(pQuantity.get())!=0 and
                len(pCompany.get())!=0 and len(pExpiryDate.get())!=0
                and len(pSymptoms.get())!=0 ):
                
                d.insert(pId.get(),pName.get(),pPrice.get(),pQuantity.get(),
                         pCompany.get(),pExpiryDate.get(),pSymptoms.get())
                productList.delete(0,END)
                productList.insert(END,pId.get(),pName.get(),pPrice.get(),
                        pQuantity.get(), pCompany.get(), pExpiryDate.get()
                        ,pSymptoms.get())
                showing()
            else:
                tkinter.messagebox.showinfo("Pharmacy Data Management System",
                            "Please Enter All Details")
            print("insert end\n")

        def showing():
            print(showing)
            productList.delete(0,END)
            for row in d.show():
                productList.insert(END,row,str(""))
            print("showing finish\n")
                
        def productRec(event):
            print("productREC")
            global pd
            searchPd = productList.curselection()[0]
            pd = productList.get(searchPd)
            
            self.txtpID.delete(0,END)
            self.txtpID.insert(END,pd[0])
            
            self.txtpName.delete(0,END)
            self.txtpName.insert(END,pd[1])
            
            self.txtpPrice.delete(0,END)
            self.txtpPrice.insert(END,pd[2])
            
            self.txtpQuantity.delete(0,END)
            self.txtpQuantity.insert(END,pd[3])
            
            self.txtpCompany.delete(0,END)
            self.txtpCompany.insert(END,pd[4])
            
            self.txtpExpiryDate.delete(0,END)
            self.txtpExpiryDate.insert(END,pd[5])
            
            self.txtpSymptoms.delete(0,END)
            self.txtpSymptoms.insert(END,pd[6])
            print("productREC finish")

        def delete():
            print("delete")
            if (len(pId.get())!=0):
                #print("hello",pd[0])
                #sprinting()
                d.delete(pd[0])
                clear()
                showing()
                #d.printing()
            print("delete finish")

        def search():
            print("search")
            productList.delete(0,END)
            for row in d.search(pId.get(),pName.get(),pPrice.get(),
                        pQuantity.get(), pCompany.get(), pExpiryDate.get()
                                ,pSymptoms.get()):
                productList.insert(END,row,str(""))
            print("search finish")

        def update():
            print("update")
            if (len(pId.get())!=0):
                d.delete(pd[0])
            if (len(pId.get())!=0):
                d.insert(pId.get(),pName.get(),pPrice.get(),pQuantity.get(),
                         pCompany.get(),pExpiryDate.get(),pSymptoms.get())
                productList.delete(0,END)
                productList.insert(END,pId.get(),pName.get(),pPrice.get(),
                        pQuantity.get(),pCompany.get(),pExpiryDate.get(),
                                   pSymptoms.get())
            print("update finish")


        def Expiry():
            root = Tk()
            application = Product2(root)
            root.mainloop() 
                    

        '''Create the Frame'''
        MainFrame= Frame(self.root,bg="red")
        MainFrame.grid()

        HeaderFrame = Frame(MainFrame, bd=1, padx=50, pady=10, bg='white', relief=RIDGE)
        HeaderFrame.pack(side=TOP)

        self.ITitle = Label(HeaderFrame, font=('arial',45,'bold'), fg="red",
                            text = "Pharmacy Data Management System", bg="white")
        self.ITitle.grid()

        OperationFrame = Frame(MainFrame,bd=3,width=1025,height=50, padx=50,
                               pady=20,bg="white",relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)


        BodyFrame = Frame(MainFrame,bd=3,width=975,height=400, padx=30,
                               pady=20,bg="white",relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        LeftFrame = LabelFrame(BodyFrame,bd=2,width=300,height=380, padx=20,
                               pady=10,bg="yellow",relief=RIDGE, font=('arial',15,'bold'),
                               text="  Product Items Details:  ")

        LeftFrame.pack(side=LEFT)


        
        RightFrame = LabelFrame(BodyFrame,bd=2,width=500,height=380, padx=20,
                            pady=10,bg="yellow",relief=RIDGE,
                            font=('arial',15,'bold'),
                            text="  Product Items Information:  ")

        RightFrame.pack(side=RIGHT)


        '''Add the Widgets to LeftFrame'''

        self.labelpID = Label(LeftFrame,font=('arial',15,'bold'),
                              text="Product Id :",pady=2,
                              padx=1,bg="white",fg="blue")
        self.labelpID.grid(row=0,column=0,stick=W)
        
        self.labelpName = Label(LeftFrame,font=('arial',15,'bold'),
                            text="Product Name :",
                            padx=1,bg="white",fg="blue")
        self.labelpName.grid(row=1,column=0,stick=W)

        self.labelpPrice = Label(LeftFrame,font=('arial',15,'bold'),
                              text="Product Price :",pady=2,
                              padx=1,bg="white",fg="blue")
        self.labelpPrice.grid(row=2,column=0,stick=W)
        
        self.labelpQuantity = Label(LeftFrame,font=('arial',15,'bold'),
                                text="Product Quantity :",pady=2,
                              padx=1,bg="white",fg="blue")
        self.labelpQuantity.grid(row=3,column=0,stick=W)

        self.labelpCompany = Label(LeftFrame,font=('arial',15,'bold'),
                              text="Product Company :",pady=2,
                              padx=1,bg="white",fg="blue")
        self.labelpCompany.grid(row=4,column=0,stick=W)
        
        self.labelpExpiryDate = Label(LeftFrame,font=('arial',15,'bold'),
                                text="Product ExpiryDate :",pady=2,
                              padx=1,bg="white",fg="blue")
        self.labelpExpiryDate.grid(row=5,column=0,stick=W)
        
        self.labelpSymptoms = Label(LeftFrame,font=('arial',15,'bold'),
                                text="Product Symptoms :",pady=2,
                              padx=1,bg="white",fg="blue")
        self.labelpSymptoms.grid(row=6,column=0,stick=W)
        

        
        self.txtpID = Entry(LeftFrame,font=('arial',20,'bold'),
                            textvariable=pId,
                            width=20)
        self.txtpID.grid(row=0,column=1,stick=W)
        
        self.txtpName = Entry(LeftFrame,font=('arial',20,'bold'),
                              textvariable=pName,
                            width=20)
        self.txtpName.grid(row=1,column=1,stick=W)
        
        self.txtpPrice = Entry(LeftFrame,font=('arial',20,'bold'),
                            textvariable=pPrice,
                            width=20)
        self.txtpPrice.grid(row=2,column=1,stick=W)
        
        self.txtpQuantity = Entry(LeftFrame,font=('arial',20,'bold'),
                              textvariable=pQuantity,
                            width=20)
        self.txtpQuantity.grid(row=3,column=1,stick=W)
        
        self.txtpCompany = Entry(LeftFrame,font=('arial',20,'bold'),
                            textvariable=pCompany,
                            width=20)
        self.txtpCompany.grid(row=4,column=1,stick=W)
        
        self.txtpExpiryDate = Entry(LeftFrame,font=('arial',20,'bold'),
                              textvariable=pExpiryDate,
                            width=20)
        self.txtpExpiryDate.grid(row=5,column=1,stick=W)
        
        self.txtpSymptoms = Entry(LeftFrame,font=('arial',20,'bold'),
                              textvariable=pSymptoms,
                            width=20)
        self.txtpSymptoms.grid(row=6,column=1,stick=W)

      

        self.labelpC2 = Label(LeftFrame,padx=1,pady=2,bg="yellow")
        self.labelpC2.grid(row=7,column=0,stick=W)
        self.labelpC3 = Label(LeftFrame,padx=1,pady=2,bg="yellow")
        self.labelpC3.grid(row=8,column=0,stick=W)
        self.labelpC1 = Label(LeftFrame,padx=1,pady=2,bg="yellow")
        self.labelpC1.grid(row=9,column=0,stick=W)


        ''' Add scroll bar'''
        scroll = Scrollbar(RightFrame)
        scroll.grid(row=0,column=1,sticky="ns")

        productList = Listbox(RightFrame, width=60, height=20,
                        font=('arial',10,'normal'),yscrollcommand=scroll.set)
        productList.bind('<<ListboxSelect>>',productRec)
        productList.grid(row=0,column=0,padx=6)
        scroll.config(command=productList.yview)


        '''Add buttons to opertation frame'''
        self.buttonInsert = Button(OperationFrame,text="Insert",width=9,
                                   font=('arial',15,'bold'),height=1, bd=4,
                                   command=insert)
        self.buttonInsert.grid(row=0,column=0)
        
        self.buttonShow = Button(OperationFrame,text="Show",width=9,
                                   font=('arial',15,'bold'),height=1, bd=4,
                                 command=showing)
        self.buttonShow.grid(row=0,column=1)

        
        self.buttonDelete = Button(OperationFrame,text="Delete",width=9,
                                   font=('arial',15,'bold'),height=1, bd=4,
                                   command=delete)
        self.buttonDelete.grid(row=0,column=2)

        
        self.buttonUpdate = Button(OperationFrame,text="Update",width=9,
                                   font=('arial',15,'bold'),height=1, bd=4,
                                   command=update)
        self.buttonUpdate.grid(row=0,column=3)

        
        self.buttonSearch = Button(OperationFrame,text="Search",width=9,
                                   font=('arial',15,'bold'),height=1, bd=4,
                                   command=search)
        self.buttonSearch.grid(row=0,column=4)


        self.buttonClose = Button(OperationFrame,text="Close",width=9,bg="red",
                                   font=('arial',15,'bold'),height=1, bd=4,
                                  command=close,fg="white")
        self.buttonClose.grid(row=0,column=7)
        
        self.buttonClear = Button(OperationFrame,text="Clear",width=9,
                                   font=('arial',15,'bold'),height=1, bd=4,
                                  command=clear)
        self.buttonClear.grid(row=0,column=5)

        self.buttonCheck = Button(OperationFrame,text="Check",width=9,
                                   font=('arial',15,'bold'),height=1, bd=4,
                                  command=Expiry)
        self.buttonCheck.grid(row=0,column=6)

        


class Database:
    def conn(self):
        print("Database : connection method called")
        con = sqlite3.connect("med.db")
        c = con.cursor()
        c.execute("""CREATE TABLE medicines(
            pid TEXT,
            name TEXT,
            price TEXT,
            qty TEXT,
            company TEXT,
            expdate TEXT,
            symptoms TEXT
            )""")
        con.commit()
        con.close()
        print("Database : connection method finish\n")


    def insert(self, pid,name,price,qty,company,expdate,symptoms):
        print("Database :insert method called")
        con = sqlite3.connect("med.db")
        c = con.cursor()
        M=[pid,name,price,qty,company,expdate,symptoms]
        c.execute("INSERT INTO medicines VALUES (?,?,?,?,?,?,?)",M)
                  
        con.commit()
        con.close()
        print("Database : insert method finish\n")


    def show(self):
        print("Database :SHOW method called")
        con = sqlite3.connect("med.db")
        c = con.cursor()
        c.execute("SELECT * FROM medicines")
        rows = c.fetchall()
        con.commit()
        con.close()
        print("Database : SHOW method finish\n")
        return rows

    def delete(self, pid):
        print("Database :delete method called",pid)
        con = sqlite3.connect("med.db")
        c = con.cursor()
        c.execute(f"DELETE FROM medicines WHERE pid = '{pid}'")
        con.commit()
        con.close()
        print(pid,"Database : delete method finish\n")


    def search(self, pid="",name="",price="",qty="",company="",expdate=""
               ,symptoms=""):
        print("Database :search method called")
        con = sqlite3.connect("med.db")
        c = con.cursor()
        c.execute("""SELECT * FROM medicines WHERE 
            pid =? OR name =? OR price =? OR qty  =? OR company =?
            OR expdate =? OR  symptoms =?""",(pid,name,price,qty,company,
                                              expdate,symptoms))
        rows = c.fetchall()
        con.commit()
        con.close()
        print("Database : search method finish\n")        
        return rows

    def update(self, pid="",name="",price="",qty="",company="",expdate=""
               ,symptoms=""):
        print("Database :update method called")
        con = sqlite3.connect("med.db")
        c = con.cursor()
        c.execute("""UPDATE medicines SET  
            pid =? OR name =? OR price =? OR qty  =? OR company =?
            OR expdate =? OR  symptoms =? WHERE pid=?""",
            (pid,name,price,qty,company,expdate,symptoms,pid))
        rows = c.fetchall()
        con.commit()
        con.close()
        print("Database : update method finish\n")

    def printing(self):
        con = sqlite3.connect("med.db")
        c = con.cursor()
        c.execute("SELECT * FROM medicines")
        items = c.fetchall()
        #c.fetchone()
        #c.fetchmany(4)
        for item in items:
            print(item[0] + " " + str(item[1]) + " " + str(item[2]))
        con.commit()
        con.close()

    def compare(self,Date):
        ans = []
        con = sqlite3.connect("med.db")
        c = con.cursor()
        c.execute("""SELECT * FROM medicines""")
        rows = c.fetchall()
        for i in range(len(rows)):
            ExpirationDate = datetime.strptime(rows[i][5],"%d-%m-%Y").date()
            checkdate = datetime.strptime(Date,"%d-%m-%Y").date()
            if ExpirationDate <= checkdate:
                print(rows[i])
                ans.append(rows[i])
        con.commit()
        con.close()
        return(ans)


    

if __name__ == '__main__':
    root = Tk()
    application = Product(root)
    root.mainloop()

#billing
#compare expiry date
    #Enter All Details insert()
