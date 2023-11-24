from tkinter import *
import  sqlite3
from PIL import ImageTk,Image
from datetime import date 

con=sqlite3.connect("medicaldata.db")
cur=con.cursor()
cur.execute("create table if not exists login(name text,id text,username text,passward text)")
cur.execute("create table if not exists cusdata(cusname text,cusaddr text,cusid number,contactno number)")
cur.execute("create table if not exists stock(name text,type text,quantity number,purpose text,mafr text,cost number,racklocation number,expdate number)")
# this code is to update the stock
def expchek():
    def chek():
        n=name.get()
        cur.execute('select expdate from   stock where name=?',(n,))
        rs=cur.fetchall()
        con.commit()
        for record in rs:
            x=record
        
        import time
        
        datd = str(x)

        # places a 0 in front of the month if only 1 digit received for month
        d = datd.split("/")
        if len(d[0])==1:
            datd="0"+datd
            print("Changed to: " + datd)

        myDate = (time.strftime("%m/%d/%Y"))

        print ("This is today's date: " + myDate)
        if datd >= myDate:    # if datd is is earlier than todays date
            s1.set(" product  expired. ")
        else:
            s1.set(" Product not expired. ")



    window=Tk()
    window.title("Medical shop managemt app ")
    window['bg']='pink'
    window.geometry('600x500')
    Label(window, text='CHEAK EXPIRE DATE OF PRODUCT',fg='black',font=('algerian',25,'bold'),bg='pink').place(x=30,y=30)
    s1=StringVar(window)


    nlabl=Label(window,text="PRODUCT NAME",bg='pink',font=15).place(x=150,y=150)
    name=Entry(window)
    name.place(x=300,y=150)
    btn=Button(window,text="chek",width=10,command=chek,bg='blue', fg='white',bd=5).place(x=200,y=200)
    Button(window, width=10, text='Main Menu', bg='blue', fg='white',command=mainpage,bd=5 ).place(x=300,y=200)


    res=Label(window,textvariable=s1,bg='gray',font=15).place(x=100,y=350)

    window.mainloop()
    
def modify():
    def update():
        n=name.get()
        q=qnty.get()
        c=cost.get()
        d=exdate.get()
        r=rack.get()
        if len(n)==0:
            s1.set("***SORRY SOMETHING WENT WRONG***")

        else:
            cur.execute("update stock set quantity=?,cost=?,expdate=?,racklocation=? where name=?", (q,c,d,r,n))
            s1.set("***YOUR PRODUCT UPDATED***")
        con.commit()
   

        
        
    window=Tk()
    window.title("Medical shop managemt app ")
    window['bg']='gray'
    window.geometry('600x400')
    
    Label(window, text='UPDATE PRODUCT DETAILS',fg='black',font=('algerian',25,'bold'),bg='gray').place(x=30,y=30)
    s1=StringVar(window)

    global name,mtype,qnty,purpose,mf,cost,rack,exdate

    Label(window, width=15, text='NAME',bg='gray').place(x=100,y=150)
    name=Entry(window)
    name.place(x=215,y=150)

        

    Label(window, width=15, text='Quantity left',bg='gray').place(x=100,y=170)
    qnty=Entry(window)
    qnty.place(x=215,y=170)

    Label(window, width=15, text='Cost',bg='gray').place(x=101,y=190)
    cost=Entry(window)
    cost.place(x=215,y=190)
        
        
    Label(window, width=15, text='expiry date',bg='gray').place(x=101,y=210)
    exdate=Entry(window)
    exdate.place(x=215,y=210)

    Label(window, width=15, text='rack location',bg='gray').place(x=101,y=230)
    rack=Entry(window)
    rack.place(x=215,y=230)
    l4=Label(window,textvariable=s1,bg='gray',font=10).place(x=110,y=330)

    Button(window, width=15, text='MODIFY', bg='blue', fg='white',command=update,bd=5).place(x=200,y=280)
    Button(window, width=10, text='Main Menu', bg='blue', fg='white',command=mainpage,bd=5 ).place(x=350,y=280)


    window.mainloop()
        

def searchstock():
    def search():
        n=name.get()
        cur.execute('select * from   stock where name=?',(n,))
        rs=cur.fetchall()
        con.commit()
        for record in rs:
            x=record
            if len(x)==0:
                s1.set("NO STOCK AVAILABLE WITH THAT NAME")
            

            else:
                s1.set("YOUR STOCK IS AVAILABLE")
                x="\nNAME     TYPE   QUANTITY   PURPOSE  MANUFACTURER  COST  RACKLOCATION EXPIRYDATE \n"
                #x=x+"\n"+str(record[0]) +"  "+ (record[1] )+"  "+ str(record[2])+" "+(record[3]) +"  "+ str(record[4] )+"  "+ str(record[5])+" "+str(record[6])+" "+(record[7])

                x=x+"%5s%5s%5d%5s%5s%5d%5d%5d\n" % (record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7])
    
                lbldata.config(text=x)
        

    window=Tk()

    window.title("Medical shop managemt app ")
    window['bg']='gray'
    window.geometry('500x300')
    Label(window, text='SEARCH  PRODUCT  FROM STOCK',fg='black',font=('algerian',20,'bold'),bg='gray').place(x=30,y=30)
    s1=StringVar(window)

   # Label(window, text='-' * 50).grid(row=1, column=0, columnspan=2)
    
    l4 = Label(window,textvariable=s1,bg='gray',font=10)

    Label(window, width=15, text='PRODUCT NAME',bg='gray').place(x=100, y=100)
    name=Entry(window)
    name.place(x=250,y=100)
    delbtn=Button(window,text="SEARCH",fg='white',bg="green",command=search,bd=5)
    Button(window, width=10, text='Main Menu', bg='green', fg='white',command=mainpage,bd=5 ).place(x=200,y=190)

    delbtn.place(x=100,y=190)
    lbldata=Label(window)
    l4.place(x=200,y=250)
    
    window.mainloop()

# this code is for delete the stock 
def delstock():
    def deldata():
        n=()
        n=name.get()
        if len(n)==0:
            t1.set("***SORRY SOMETHING WENT WRONG***")

        else:
            cur.execute("delete from stock where name= ?", (n,))

            t1.set("***YOUR PRODUCT REMOVE SUCCESFULLY***")
        con.commit()
    window=Tk()
    window.title("Medical shop managemt app ")
    window['bg']='PINK'
    window.geometry('500x300')
    t1=StringVar(window)

    titel=Label(window,text="DELETE PRODUCT DETAILS",fg='black',font=('algerian',25,'bold'),bg='PINK').place(x=30,y=30)
    

    Label(window, width=15, text='PRODUCT NAME',bg='pink',font=('times new roman',10,'bold')).place(x=100, y=100)
    name=Entry(window)
    name.place(x=240,y=100)
    delbtn=Button(window,text="DELETE PRODUCT",bg="GREEN",fg='white',command=deldata,bd=5)
    Button(window, width=10, text='Main Menu', bg='green', fg='white',command=mainpage,bd=5 ).place(x=260,y=160)

    delbtn.place(x=140,y=160)
    leb=Label(window,bg='pink',textvariable=t1,font=10).place(x=100,y=210)
    window.mainloop()

#code to add product details
def addstock():
        n=name.get()
        t=mtype.get()
        q=qnty.get()
        p=purpose.get()
        m=mf.get()
        c=cost.get()
        l=rack.get()
        x=exdate.get()
        #stock=(n,t,q,p,m,c,l,x)
        if len(n)==0 and len(x)==0:
            text.set("***SORRY SOMETHING WENT WRONG***")

        else:
            cur.execute("insert into stock values(?,?,?,?,?,?,?,?)",(n,t,q,p,m,c,l,x))
            text.set("***YOUR PRODUCT DETAILS ARE ADDED SUCCESFULLY***")

        con.commit()

def stock():
    

    window=Tk()
    window.title("Medical shop managemt app ")
    window['bg']='gray'
    window.geometry('950x350')
    global name,mtype,qnty,purpose,mf,cost,rack,exdate,text
    titel=Label(window,text="ENTER YOUR PRODUCT DETAILS",fg='black',font=('algerian',25,'bold'),bg='gray')
    titel.place(x=50,y=30)
    text=StringVar(window)

    Label(window, width=15, text='Name',font=('times new roman',10,'bold'),bg='gray').place(x=200,y=100)


    name=Entry(window)
    name.place(x=350,y=100)


    Label(window, width=15, text='Type',font=('times new roman',10,'bold'),bg='gray').place(x=200,y=120)

    mtype=Entry(window)
    mtype.place(x=350,y=120)



    Label(window, width=15, text='Quantity left',font=('times new roman',10,'bold'),bg='gray').place(x=200,y=140)

    qnty=Entry(window)
    qnty.place(x=350,y=140)


    Label(window, width=15, text='cost',font=('times new roman',10,'bold'),bg='gray').place(x=200,y=160)
    cost=Entry(window)
    cost.place(x=350,y=160)
    Label(window, width=15, text='purpose',font=('times new roman',10,'bold'),bg='gray').place(x=200,y=180)
    purpose=Entry(window)
    purpose.place(x=350,y=180)
    Label(window, width=15, text='expiry date',font=('times new roman',10,'bold'),bg='gray').place(x=200,y=200)
    
    
    exdate=Entry(window)
    exdate.place(x=350,y=200)

    Label(window, width=15, text='rack location',font=('times new roman',10,'bold'),bg='gray').place(x=200,y=220)
    rack=Entry(window)
    rack.place(x=350,y=220)
    Label(window, width=15, text='manufacturer',font=('times new roman',10,'bold'),bg='gray').place(x=200,y=240)  
    mf=Entry(window)
    mf.place(x=350,y=240)

    Button(window, width=15, text='Submit', bg='blue', fg='white',command=addstock,bd=5).place(x=200,y=280)   
    
  
    Button(window, width=10, text='Main Menu', bg='green', fg='white',command=mainpage,bd=5 ).place(x=350,y=280)
    l4=Label(window,bg='gray',textvariable=text).place(x=200,y=320)

    window.mainloop()




#code for add data of valued customer

def valcustumer():
    def adddata():
        n=cusname.get()
        addr=cusaddr.get()
        id=cusid.get()
        no=contno.get()
        if len(n)==0 and len(no)==0:
            s1.set("***SORRY SOMETHING WENT WRONG***")

        else:
            cur.execute("insert into cusdata values(?,?,?,?)",(n,addr,id,no))

            s1.set("***REGISTRATION OF VALUED CUSTOMER SUCCESED***")

        
        con.commit()
    window=Tk()
    window.title("Medical shop managemt app ")
    window['bg']='gray'
    window.geometry('750x500')
    s1=StringVar(window)

    titel=Label(window,text="WELCOME TO MEDICAL SHOP MANAGEMENT \n  SYSTEM",fg='black',font=('algerian',25,'bold'),bg='gray')
    titel.place(x=30,y=40)
    Label(window, text="Name: ",font=25).place(x=200, y=150)
    cusname = Entry(window)
    cusname.place(x=300, y=150)
    Label(window, text="Address: ",font=25).place(x=200, y=200)
    cusaddr = Entry(window)
    cusaddr.place(x=300, y=200)

    Label(window, text="cus Id: ",font=25).place(x=200, y=250)

    cusid= Entry(window)
    cusid.place(x=300, y=250)

    Label(window, text="Mobile no: ",font=25).place(x=200, y=300)
    contno = Entry(window)
    contno.place(x=300, y=300)

    Button(window, text='Submit', bg='blue', fg='white',command=adddata,font=15,bd=5 ).place(x=200, y=350)

    Button(window, text='Main Menu', bg='green', fg='white', command=mainpage,font=15,bd=5).place(x=300, y=350)
    l4 = Label(window,textvariable=s1,bg='skyblue')
    l4.place(x=100, y=400) 

    window.mainloop()

# code for first main page
def mainpage():
    
    main=Tk()

    main.title("Medical shop managemt app ")
    main.configure(bg='sky blue')
    main.geometry('900x500')


    titel=Label(main,text="WELCOME TO MEDICAL SHOP MANAGEMENT \n  SYSTEM",fg='black',font=('algerian',25,'bold'),bg='skyblue')
    titel.place(x=30,y=40)

    #This is the first column of over options list. This column displays all the options relating to stock management
    l4=Label(main, text="Stock Maintenance", bg='black', fg='white',font=('ariel', 12 ),).place(x=210, y=150)
    newvcbtn=Button(main, text='New V.C.', width=25, bg='green', font=('ariel', 12 ),fg='white',command=valcustumer).place(x=180, y=170)
    addprodbtn=Button(main ,text='Add product to Stock', bg='green', font=('ariel', 12 ),fg='white', width=25,command=stock).place(x=180, y=200)
    delprodbtn=Button(main ,text='Delete product from Stock', bg='red', font=('ariel', 12 ),fg='white', width=25,command=delstock).place(x=180, y=230)

        #This is for the second column that will hold all the options relating to accessing database. 
        #In order to modify the font size, color etc we used the various propoerties of Button() fuction.
    Label(main ,text="Access Database", bg='black',font=('ariel', 12 ), fg='white').place(x=605, y=150)
    Button(main ,text='Modify', width=15, bg='blue',font=('ariel', 12 ), fg='white',command=modify).place(x=600, y=170)
    Button(main, text='Search', width=15, bg='blue', font=('ariel', 12 ),fg='white',command=searchstock).place(x=600, y=200)
    Button(main, text='Expiry Check', bg='red', fg='white',font=('ariel', 12 ), width=15,command=expchek).place(x=600, y=230)

    #The last column display the options relating to bll generation and logout option
    Button(main, text='Logout', bg='red', fg='white', font=('ariel', 12 ), width=15,command=main.destroy).place(x=600, y=260)
    main.mainloop()

# code for login window in which user enter passward and username


#code for signup button in which user enter there information

def signup():
    sign=Toplevel()
    sign.title("Medical shop managemt app")
    sign.geometry("600x400")
    sign.configure(bg='tomato4')
    s1=StringVar(sign)


 
    
        
    

    # functiom to add data

    def adddata():
        n=txtname.get()
        id=txtid.get()
        un=txtusername.get()
        p=txtpassward.get()
        if len(un)==0 and len(p)==0:
            s1.set("***SORRY SOMETHING WENT WRONG***")

        else:
            cur.execute("insert into login values(?,?,?,?)",(n,id,un,p))
            s1.set("***REGISTRATION SUCCESED***")


        con.commit()

    
    

    labname=Label(sign,text="Enter your name",font=25)
    txtname=Entry(sign)
    labid=Label(sign,text="Enter Email id",font=25)
    txtid=Entry(sign)
    labusername=Label(sign,text="Enter user name",font=25)
    txtusername=Entry(sign)
    labpassward=Label(sign,text="Enter passward",font=25)
    txtpassward=Entry(sign,show='*')
    btnsignup=Button(sign,text="SIGNUP",bg="pink",fg="black",font=15,command=adddata,bd=5)
    btnquit=Button(sign,text="QUIT",bg="pink",fg="black",font=15,command=sign.destroy,bd=5)
    

    #labname.place(x=130,y=100)
    labname.place(x=100,y=100)

    txtname.place(x=250,y=100)
    labid.place(x=100,y=130)
    txtid.place(x=250,y=130)

    labusername.place(x=100,y=160)
    txtusername.place(x=250,y=160)
    labpassward.place(x=100,y=190)
    txtpassward.place(x=250,y=190)

    btnsignup.place(x=100,y=240)
    btnquit.place(x=300,y=240)
    titel=Label(sign,text="CREATE YOUR ACCOUNT",fg='black',font=('algerian',25,'bold'),bg='tomato4')
    titel.place(x=30,y=40)
    l4 = Label(sign,textvariable=s1,bg='skyblue')
    l4.place(x=100, y=300) 

    



    sign.mainloop()





# code for login window in only two buttons login and signup

   
window=Tk()
window.title("Medical shop managemt app")
window.geometry("800x600")


 
image_open = Image.open("D:\kishori database\kishori python programs\miniproject\image.jpg") #change to where the picture is
image = ImageTk.PhotoImage(image_open)
bg = Label(window,image=image) #makes the label the image
bg.image = image
def verify():
        u=txtname.get()
        p=txtpassward.get()
        if len(u)==0 and len(p)==0:
            s1.set("****please enter username****")
        else:
            cur.execute('select * from   login where username=? and passward=?',(u,p))
            rs=cur.fetchall()
            con.commit()
            if len(rs)==0:
                s1.set("The username or password  you have entered are incorrect.")

            else:
                 mainpage()
            


s1=StringVar(window)


bg.place(x=-10, y=-10) #places the label in the background

frame1=LabelFrame(window, font=('times new roman',15,'bold'),fg='black', bd=5, bg='pink', relief=RIDGE)
frame1.place(x=150, y=190)
  
lblname = Label(frame1, text = " Enter Username ",font=('times new roman',15,'bold'),bg='pink', fg='black')
lblname.grid(row=0, column=0, padx=10, pady=10)
txtname = Entry(frame1, font = ('times new roman',15,'bold'), width=20, bd=5, bg='white', relief=RIDGE)
txtname.grid(row=0, column=1, padx=10, pady=10)
    
frame2=LabelFrame(window, font=('times new roman',15,'bold'),fg='black', bd=5, bg='pink', relief=RIDGE)
frame2.place(x=150, y=270)

lblpassword = Label(frame2, text = " Enter Password ",font=('times new roman',15,'bold'),bg='pink', fg='black')
lblpassword.grid(row=1, column=0, padx=10, pady=10)
txtpassward = Entry(frame2, font = ('times new roman',15,'bold'), width=20, bd=5, bg='white', relief=RIDGE, show='*')
txtpassward.grid(row=1, column=1, padx=10, pady=10)

button = Button(window, text = 'SIGNUP', font=('times new roman',15,'bold'),fg='white', width=7,bg='green',bd=5,command=signup)
button.place(x=200, y=380) 
btnquit=Button(window,text="QUIT",font=('times new roman',15,'bold'),bg="green",fg="white",bd=5,command=window.destroy)
btnquit.place(x=350, y=380) 

btnlgn=Button(window,text="LOGIN",font=('times new roman',15,'bold'),bg="green",fg="white",bd=5,command=verify)
btnlgn.place(x=470, y=380) 

l4 = Label(window,textvariable=s1,bg='skyblue',font=30)
l4.place(x=100, y=500) 
titel=Label(window,text="WELCOME TO MEDICAL SHOP MANAGEMENT \n  SYSTEM",fg='black',font=('algerian',25,'bold'),bg='skyblue')
titel.place(x=30,y=40)


window.mainloop()
