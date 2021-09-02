from tkinter import *

root = Tk()
root.title('Calculator app by Sasidhar R A')
root.iconbitmap('calc.ico')
root.geometry('400x180')
root['bg'] = 'azure'
y = ''


def btn_click(x):
    global y
    y = y + str(x)
    z.set(y)

def sqroot(x):
    pass

def equal():
    a=e0.get()
    b=eval(a)
    z.set(b)

def clear():
    e0.delete(0,END)
    global y
    y = ''
    z.set(y)


z=StringVar()
l0 = Label(root, text='Enter Values:', bg='azure')
e0 = Entry(root, bg='white', fg='black', width='46',textvariable=z)
b9 = Button(root, text='9', bg='khaki1', width=6, command=lambda: btn_click(9))
b8 = Button(root, text='8', bg='khaki1', width=6, command=lambda: btn_click(8))
b7 = Button(root, text='7', bg='khaki1', width=6, command=lambda: btn_click(7))
b6 = Button(root, text='6', bg='khaki1', width=6, command=lambda: btn_click(6))
b5 = Button(root, text='5', bg='khaki1', width=6, command=lambda: btn_click(5))
b4 = Button(root, text='4', bg='khaki1', width=6, command=lambda: btn_click(4))
b3 = Button(root, text='3', bg='khaki1', width=6, command=lambda: btn_click(3))
b2 = Button(root, text='2', bg='khaki1', width=6, command=lambda: btn_click(2))
b1 = Button(root, text='1', bg='khaki1', width=6, command=lambda: btn_click(1))
b0 = Button(root, text='0', bg='khaki1', width='22', command=lambda: btn_click(0))

badd = Button(root, text='+', bg='khaki1', width=5, height=2,command=lambda :btn_click('+'))
bminus = Button(root, text='-', bg='khaki1', width=5, height=2,command=lambda :btn_click('-'))
bmul = Button(root, text='x', bg='khaki1', width=5, height=2,command=lambda :btn_click('*'))
bdiv = Button(root, text='/', bg='khaki1', width=5, height=2,command=lambda :btn_click('/'))
bequal = Button(root, text='=', bg='salmon', width='12',command=equal)
bclear = Button(root, text='C', bg='khaki1', width= 5,height=7,command=clear)

bsqroot= Button(root, text='√', bg='khaki1', width=4, height=1,command=lambda :btn_click('**(1/2)'))
bcbroot= Button(root, text='∛', bg='khaki1', width=4, height=1,command=lambda :btn_click('**(1/3)'))
bpower= Button(root, text='x^y', bg='khaki1', width=4, height=2,command=lambda :btn_click('**'))

l0.place(x=5, y=5)
e0.place(x=5, y=25)
b7.place(x=5, y=50)
b8.place(x=60, y=50)
b9.place(x=115, y=50)
b4.place(x=5, y=80)
b5.place(x=60, y=80)
b6.place(x=115, y=80)
b1.place(x=5, y=110)
b2.place(x=60, y=110)
b3.place(x=115, y=110)
b0.place(x=5, y=140)

badd.place(x=190, y=50)
bminus.place(x=240, y=50)
bmul.place(x=190, y=95)
bdiv.place(x=240, y=95)
bequal.place(x=190, y=140)
bclear.place(x=300, y=50)

bsqroot.place(x=350, y=88)
bcbroot.place(x=350, y=50)
bpower.place(x=350, y=125)

root.mainloop()
