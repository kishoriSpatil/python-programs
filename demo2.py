from tkinter import *
import  sqlite3
import time
import random
from PIL import ImageTk,Image
con=sqlite3.connect("kishori.db")
cur=con.cursor()
def login():
    window=Tk()
    window.title("Medical shop managemt app")
    window.geometry("600x400")
    
 
    image_open = Image.open("D:\kishori database\kishori python programs\miniproject\image1.png") #change to where the picture is
    image = ImageTk.PhotoImage(image_open)
    
    bg = Label(image=image) #makes the label the image
    bg.image = image
    
    bg.place(x=-10, y=-10) #places the label in the background
    labname=Label(window,text="USERBANE",font=20)
    txtname=Entry(window)
    labpassward=Label(window,text="PASSWARD",font=20)
    txtpassward=Entry(window,show='*')
    btnsignup=Button(window,text="SIGNUP",bg="pink",fg="black",command=signup)
    btnquit=Button(window,text="QUIT",bg="pink",fg="black",command=window.destroy)
    btnlgn=Button(window,text="LOGIN",bg="pink",fg="black",command=window.destroy)


        
    labname.place(x=150,y=150)
    txtname.place(x=300,y=150)
    labpassward.place(x=150,y=200)
    txtpassward.place(x=300,y=200)
    btnsignup.place(x=150,y=300)
    btnlgn.place(x=250,y=300)
    btnquit.place(x=350,y=300)
    window.mainloop()

    
        
    
    
def signup():
    def adddata():
        n=txtname.get()
        id=txtid.get()
        un=txtusername.get()
        p=txtpassward.get()
        cur.execute("insert into login values(?,?,?,?)",(n,id,un,p))
        print("ok")

        con.commit()

    window=Tk()
    window.title("Medical shop managemt app")
    window.geometry("500x400")
    
 
    image_open = Image.open("D:\kishori database\kishori python programs\miniproject\image1.png") #change to where the picture is
    image = ImageTk.PhotoImage(image_open)
    
    bg = Label(image=image) #makes the label the image
    bg.image = image
    
    bg.place(x=-10, y=-10) #places the label in the background
    labname=Label(window,text="Enter your name",font=20)
    txtname=Entry(window)
    labpassward=Label(window,text="Enter passward",font=20)
    txtpassward=Entry(window,show='*')
    btnsignup=Button(window,text="SIGNUP",bg="pink",fg="black",command=adddata)
    btnquit=Button(window,text="QUIT",bg="pink",fg="black",command=window.destroy)
    btnlgn=Button(window,text="LOGIN",bg="pink",fg="black",command=window.destroy)


        
    

    # functiom to add data

    
    labname=Label(window,text="Enter your name",font=20)
    txtname=Entry(window)
    labid=Label(window,text="Enter Email id",font=20)
    txtid=Entry(window)
    labusername=Label(window,text="Enter user name",font=20)
    txtusername=Entry(window)
    labpassward=Label(window,text="Enter passward",font=20)
    txtpassward=Entry(window,show='*')
    btnsignup=Button(window,text="SIGNUP",bg="pink",fg="black",command=adddata)
    btnquit=Button(window,text="QUIT",bg="pink",fg="black",command=window.destroy)
    

    #labname.place(x=130,y=100)
    labname.grid(row=0,column=0,padx=2,pady=2)

    txtname.grid(row=0,column=1,padx=2,pady=2)
    labid.grid(row=1,column=0,padx=2,pady=2)
    txtid.grid(row=1,column=1,padx=2,pady=2)
    labusername.grid(row=2,column=0,padx=2,pady=2)
    txtusername.grid(row=2,column=1,padx=2,pady=2)
    labpassward.grid(row=3,column=0,padx=2,pady=2)
    txtpassward.grid(row=3,column=1,padx=2,pady=2)
    btnsignup.grid(row=4,column=1)
    btnquit.grid(row=4,column=2,padx=2,pady=2)

    
window=Tk()
window.title("Medical shop managemt app")
window.geometry("600x400")


 
image_open = Image.open("D:\kishori database\kishori python programs\miniproject\image1.png") #change to where the picture is
image = ImageTk.PhotoImage(image_open)
 
bg = Label(image=image) #makes the label the image
bg.image = image
 
bg.place(x=-10, y=-10) #places the label in the background


label1=Label(window,text="If you are new then sign up please !! if you are existing customer login ",bg='gray',fg='black',font=30)
btnlogin=Button(window,text='Login',bg='skyblue',)
btnsignup=Button(window,text='Signup',bg='skyblue',command=signup)
btnquit=Button(window,text="QUIT",bg="pink",fg="black",command=window.destroy)
#f2.pac



label1.place(x=40,y=50)
btnlogin.place(x=100,y=150)
btnsignup.place(x=200,y=150)
btnquit.place(x=300,y=150)
#f2.pack()

login()