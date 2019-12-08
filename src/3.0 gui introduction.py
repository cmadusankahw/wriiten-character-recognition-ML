import tkinter as tk

window=tk.Tk() #calling the constructor to create object from tikinter gui library (window)

#action event for the button1
def func1():
    label1.config(text='HELLO',bg='blue') #changing attributes of a widget
    button1.config(bg='blue') 

def func2():
    label1.config(text='OK',bg='red')

font1='Helvetica 20 bold' #creating a customized font
font2='Times 15 italic'

label1=tk.Label (window, text='OK',bg='black',fg='white',font=font1)
#need to give position for the widget
label1.grid(row=0,column=0) #positioning the label using grid method

button1=tk.Button(window,text='CHANGE',bg='red',fg='gray20',font=font2,height=2,width=10,command=func1) #Event for the button widget
button1.grid(row=1,column=0)


button2=tk.Button(window,text='CHANGE',bg='red',fg='gray20',font=font2,height=2,width=10,command=func2) #Event for the button widget
button2.grid(row=1,column=1)

window.mainloop() #for non IDLE IDEs to generate GUI

