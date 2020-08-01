# KUNAL KAUSHIK 
# X = "FIRST PYTHON PROJECT"
# PRINT(X)

from tkinter import *
from tkinter import messagebox
import math
screen = Tk()
screen.title("My calculator")
screen.iconbitmap('calce.ico')
screen.configure(bg='white')
screen.maxsize(width=453,height=488)
screen.minsize(width=362,height=488)
screen.geometry('362x488')


def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def clear():
    global operator
    operator = ''
    tex.set(operator)


def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo('Notify you','Put a correct number')



################################################################################# adv. wale ke function

def cmsin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notify you','Put a correct number')


def cmsin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notify you','Put a correct number')


def cmcos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notify you','Put a correct number')


def cmtan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notify you','Put a correct number')


def cmlog():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notify you','Put a correct number')


def cmsqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('zcyber`s','Please Put a correct number')





############################################################################################  binding function

def on_enter7(e):
    btn7.configure(bg='silver')
def on_leave7(e):
    btn7.configure(bg='powder blue')

def on_enter8(e):
    btn8.configure(bg='silver')
def on_leave8(e):
    btn8.configure(bg='powder blue')

def on_enter9(e):
    btn9.configure(bg='silver')
def on_leave9(e):
    btn9.configure(bg='powder blue')

def on_enteradd(e):
    btnadd.configure(bg='silver')
def on_leaveadd(e):
    btnadd.configure(bg='powder blue')

def on_enter4(e):
    btn4.configure(bg='silver')
def on_leave4(e):
    btn4.configure(bg='powder blue')

def on_enter5(e):
    btn5.configure(bg='silver')
def on_leave5(e):
    btn5.configure(bg='powder blue')

def on_enter6(e):
    btn6.configure(bg='silver')
def on_leave6(e):
    btn6.configure(bg='powder blue')


def on_entersub(e):
    btnsub.configure(bg='silver')
def on_leavesub(e):
    btnsub.configure(bg='powder blue')

def on_enter1(e):
    btn1.configure(bg='silver')
def on_leave1(e):
    btn1.configure(bg='powder blue')

def on_enter2(e):
    btn2.configure(bg='silver')
def on_leave2(e):
    btn2.configure(bg='powder blue')

def on_enter3(e):
    btn3.configure(bg='silver')
def on_leave3(e):
    btn3.configure(bg='powder blue')

def on_entermu1(e):
    btnmu1.configure(bg='silver')
def on_leavemu1(e):
    btnmu1.configure(bg='powder blue')

def on_enter0(e):
    btn0.configure(bg='silver')
def on_leave0(e):
    btn0.configure(bg='powder blue')

def on_enterdiv(e):
    btndiv.configure(bg='silver')
def on_leavediv(e):
    btndiv.configure(bg='powder blue')

def on_enterequal(e):
    btnequal.configure(bg='silver')
def on_leaveequal(e):
    btnequal.configure(bg='powder blue')

def on_enterclear(e):
    btnclear.configure(bg='silver')
def on_leaveclear(e):
    btnclear.configure(bg='powder blue')

def on_entryenter(e):
    entry1.configure(bg='silver',fg='white')
def on_entryleave(e):
    entry1.configure(bg='powder blue',fg='black')

##################################################################### advan. ke function

def on_entersin(e):
    btnsin.configure(bg='silver')
def on_leavesin(e):
    btnsin.configure(bg='powder blue')

def on_entercos(e):
    btncos.configure(bg='silver')
def on_leavecos(e):
    btncos.configure(bg='powder blue')

def on_entertan(e):
    btntan.configure(bg='silver')
def on_leavetan(e):
    btntan.configure(bg='powder blue')

def on_entersqrt(e):
    btnsqrt.configure(bg='silver')
def on_leavesqrt(e):
    btnsqrt.configure(bg='powder blue')

def on_enterlog(e):
    btnlog.configure(bg='silver')
def on_leavelog(e):
    btnlog.configure(bg='powder blue')


tex = StringVar()
operator = ''

entry1 = Entry(screen ,bg= 'white', font=('arial','20','italic'),bd= '30',justify='right', textvariable=tex)
entry1.grid(row=0,columnspan=4)

btn7 = Button(screen,text='7',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
              ,activebackground='black',command=lambda:click(7))
btn7.grid(row=1,column=0)

btn8 = Button(screen,text='8',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
              ,activebackground='black',command=lambda:click(8))
btn8.grid(row=1,column=1)

btn9 = Button(screen,text='9',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
              ,activebackground='black',command=lambda:click(9))
btn9.grid(row=1,column=2)

btnadd = Button(screen,text='+',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
                ,activebackground='black',command=lambda:click('+'))
btnadd.grid(row=1,column=3)

btn4 = Button(screen,text='4',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
              ,activebackground='black',command=lambda:click(4))
btn4.grid(row=2,column=0)

btn5 = Button(screen,text='5',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
              ,activebackground='black',command=lambda:click(5))
btn5.grid(row=2,column=1)

btn6 = Button(screen,text='6',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
              ,activebackground='black',command=lambda:click(6))
btn6.grid(row=2,column=2)

btnsub = Button(screen,text='-',bg='powder blue' ,bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
                ,activebackground='black',command=lambda:click('-'))
btnsub.grid(row=2,column=3)

btn1 = Button(screen,text='1',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
              ,activebackground='black',command=lambda:click(1))
btn1.grid(row=3,column=0)

btn2 = Button(screen,text='2',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
              ,activebackground='black',command=lambda:click(2))
btn2.grid(row=3,column=1)

btn3 = Button(screen,text='3',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
              ,activebackground='black',command=lambda:click(3))
btn3.grid(row=3,column=2)

btnmu1 = Button(screen,text='*',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
                ,activebackground='black',command=lambda:click('*'))
btnmu1.grid(row=3,column=3)

btn0 = Button(screen,text='0',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
              ,activebackground='black',command=lambda:click(0))
btn0.grid(row=4,column=0)

btndiv = Button(screen,text='/',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
                ,activebackground='black',command=lambda:click('/'))
btndiv.grid(row=4,column=1)

btnequal = Button(screen,text='=',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
                  ,activebackground='black',command=equal)
btnequal.grid(row=4,column=2)

btnclear = Button(screen,text='c',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
                  ,activebackground='black',command=clear)
btnclear.grid(row=4,column=3)

######################################################## advanced buttons

btnsin = Button(screen,text='sin',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
              ,activebackground='black',command=cmsin)
btnsin.grid(row=0,column=4)


btncos = Button(screen,text='cos',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='16',pady='16'
              ,activebackground='black',command=cmcos)
btncos.grid(row=1,column=4)

btntan = Button(screen,text='tan',bg='powder blue',bd='8',font=('arial','22','bold'),activeforeground='white',padx='16',pady='16'
              ,activebackground='black',command=cmtan)
btntan.grid(row=2,column=4)


btnsqrt = Button(screen,text='sq.',bg='powder blue',bd='8',font=('arial','23','bold'),activeforeground='white',padx='18',pady='16'
              ,activebackground='black',command=cmsqrt)
btnsqrt.grid(row=3,column=4)


btnlog = Button(screen,text='log',bg='powder blue',bd='8',font=('arial','20','bold'),activeforeground='white',padx='18',pady='16'
              ,activebackground='black',command=cmlog)
btnlog.grid(row=4,column=4)
############################################################.....................numbers binding mtlb=over effects

btnsin.bind('<Enter>',on_entersin)
btnsin.bind('<Leave>',on_leavesin)

btncos.bind('<Enter>',on_entercos)
btncos.bind('<Leave>',on_leavecos)

btntan.bind('<Enter>',on_entertan)
btntan.bind('<Leave>',on_leavetan)

btnsqrt.bind('<Enter>',on_entersqrt)
btnsqrt.bind('<Leave>',on_leavesqrt)

btnlog.bind('<Enter>',on_enterlog)
btnlog.bind('<Leave>',on_leavelog)

###########################################################.....................numbers binding


btn7.bind('<Enter>', on_enter7)
btn7.bind('<Leave>', on_leave7)

btn8.bind('<Enter>', on_enter8)
btn8.bind('<Leave>', on_leave8)

btn9.bind('<Enter>', on_enter9)
btn9.bind('<Leave>', on_leave9)

btnadd.bind('<Enter>', on_enteradd)
btnadd.bind('<Leave>', on_leaveadd)

btn4.bind('<Enter>', on_enter4)
btn4.bind('<Leave>', on_leave4)

btn5.bind('<Enter>', on_enter5)
btn5.bind('<Leave>', on_leave5)

btn6.bind('<Enter>', on_enter6)
btn6.bind('<Leave>', on_leave6)

btnsub.bind('<Enter>', on_entersub)
btnsub.bind('<Leave>', on_leavesub)

btn1.bind('<Enter>', on_enter1)
btn1.bind('<Leave>', on_leave1)

btn2.bind('<Enter>', on_enter2)
btn2.bind('<Leave>', on_leave2)

btn3.bind('<Enter>', on_enter3)
btn3.bind('<Leave>', on_leave3)

btnmu1.bind('<Enter>', on_entermu1)
btnmu1.bind('<Leave>', on_leavemu1)

btn0.bind('<Enter>', on_enter0)
btn0.bind('<Leave>', on_leave0)

btndiv.bind('<Enter>', on_enterdiv)
btndiv.bind('<Leave>', on_leavediv)

btnequal.bind('<Enter>', on_enterequal)
btnequal.bind('<Leave>', on_leaveequal)

btnclear.bind('<Enter>', on_enterclear)
btnclear.bind('<Leave>', on_leaveclear)

entry1.bind('<Enter>', on_entryenter)
entry1.bind('<Leave>', on_entryleave)
####################################################....................numbers binding




screen.mainloop()
