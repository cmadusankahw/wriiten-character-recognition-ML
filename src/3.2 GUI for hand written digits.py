import tkinter as tk
from PIL import ImageTk,Image,ImageDraw
import PIL
import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

try:
    os.mkdir('data') #creating a folder in the code directory
except:
    print('Path Already Exists')

count=0

win=tk.Tk()
width=550
height=500
font_button='Helvetica 20 bold'

from sklearn import datasets

digits=datasets.load_digits()

data=digits.data
target=digits.target

from sklearn import svm

clsfr=svm.SVC() #using SVM and training it with toy data set
clsfr.fit(data,target)


#Event fuctions
def event_function(event): #the 'event' parameter is for passing a value related to that event (ex:- x,y coordinstes of the mouse in here)
    x=event.x
    y=event.y
    label_mouse.config(text=str(x)+','+str(y)) #to prove that, we are printing mouse motion coordinates of the pointer to the lable

    x1=x-20
    y1=y-20
    x2=x+20
    y2=y+20
    #Note :- mouse pointer(B1) binding with drawing circle
    canvas.create_oval((x1,y1,x2,y2), fill='black') #drawing the black (set of circles) line with mouse motion
    img_draw.ellipse((x1,y1,x2,y2),fill='white')

def save():
    global count #using the same gloal count variablle inste of creating a local count variablle

    img_array=np.array(img) #converting image to an array
    img_array=cv2.resize(img_array,(8,8)) #resizing the image using cv2
    path=os.path.join('data',str(count)+'.jpg') #joining the path , the createdd image to the data floder
    cv2.imwrite(path,img_array)

    count+=1

def clear():
    global img,img_draw

    canvas.delete('all')
    img=Image.new('RGB',(width,height),(0,0,0))
    img_draw=ImageDraw.Draw(img)

def predict():

    img_array=np.array(img)
    img_array=cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)
    img_array=cv2.resize(img_array,(8,8))

    plt.imshow(img_array,cmap='binary')

    img_array=np.reshape(img_array,(1,64)) #reshaping the 8x8 image array into 1x64 2d arry for prediction using SVM

    img_array=img_array/255.0 * 15 #converting the image array range to 0-15 to similar with train data

    results=clsfr.predict(img_array)

    label_predict.config(text="PREDICTED DIGIT :"+str(results))

    plt.show()

canvas=tk.Canvas(win,width=width,height=height,bg='white')
canvas.grid(row=0,column=0,columnspan=4,rowspan=8) #columnspan - get the next row into colums under this widget


label_mouse=tk.Label(win,text='', bg='white', font=font_button)
label_mouse.grid(row=0,column=3)

btnsave=tk.Button(win,text='SAVE',bg='green',font=font_button,width=7,command=save)
btnsave.grid(row=8,column=0,pady=10) #padx, pady - to add margins among widgets (once applied affected for the entirere row)

btnpredict=tk.Button(win,text='PREDICT',bg='blue',font=font_button,width=7,command=predict)
btnpredict.grid(row=8,column=1)

btnclear=tk.Button(win,text='CLEAR',bg='yellow',font=font_button,width=7,command=clear)
btnclear.grid(row=8,column=2)

btnexit=tk.Button(win,text='EXIT',bg='red',font=font_button,width=7,comman=win.destroy) #command to exit the window
btnexit.grid(row=8,column=3)

label_predict=tk.Label(win,text='PREDICTED DIGIT : NONE', bg='gray90', font=font_button)
label_predict.grid(row=9,column=0,columnspan=4)

canvas.bind('<B1-Motion>', event_function) #b1 is the left corner of the mouse  motion - mouse drag and move  this action is bnided to the canvas
#b1-left click, b2- scroll button b3-right clcick of the mouse  motion - draging action

img=Image.new('RGB',(width,height),(0,0,0))
img_draw=ImageDraw.Draw(img)

win.mainloop()