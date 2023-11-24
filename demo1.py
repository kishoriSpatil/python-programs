from tkinter import *
#global apt, flag
#flag = 'apt'
#apt = Tk()

global cur, c, columns, accept, flag, sto, apt
flag = 'sto'
accept = [''] * 10
sto = Tk()
sto.title('STOCK ENTRY')
Label(sto, text='ENTER NEW PRODUCT DATA TO THE STOCK').grid(row=0, column=0, columnspan=2)
Label(sto, text='-' * 50).grid(row=1, column=0, columnspan=2)

Label(sto, width=15, text='name').grid(row=3, column=0)
name=Entry(sto).grid(row=3,column=1)
Label(sto, width=15, text='type').grid(row=4, column=0)
type=Entry(sto).grid(row=4,column=1)

Label(sto, width=15, text='quantity left').grid(row=5, column=0)
quantity=Entry(sto).grid(row=5,column=1)

Label(sto, width=15, text='cost').grid(row=6, column=0)
cost=Entry(sto).grid(row=6,column=1)

Label(sto, width=15, text='purpose').grid(row=7, column=0)
purpose=Entry(sto).grid(row=7,column=1)

Label(sto, width=15, text='expiry date').grid(row=8, column=0)
expdate=Entry(sto).grid(row=8,column=1)

Label(sto, width=15, text='rack location').grid(row=9, column=0)
rlction=Entry(sto).grid(row=9,column=1)

Label(sto, width=15, text='manufacturer').grid(row=10, column=0)
mafr=Entry(sto).grid(row=10,column=1)

Button(sto, width=15, text='Submit', bg='blue', fg='white').grid(row=12, column=1)
Label(sto, text='-' * 165).grid(row=13, column=0, columnspan=7)
Button(sto, width=15, text='Reset', bg='red', fg='white').grid(row=12, column=0)
Button(sto, width=15, text='Refresh stock', bg='skyblue', fg='black', ).grid(row=12, column=4)

Label(sto, text='hello').grid(row=14, column=2)

Button(sto, width=10, text='Main Menu', bg='green', fg='white' ).grid(row=12, column=5)
    
sto.mainloop()
    