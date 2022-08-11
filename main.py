from select import select
from tkinter.tix import Tree
import numpy as np
import pandas as pd
from Stroke import Stroke
from mobile import Mobile
from models import Model
from livefacebook import Live
from insurance import Ins
from tkinter import OptionMenu, StringVar, ttk, Tk
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

def draw_table1(st, data):
    print(data)
    data['des'] = data.index
    tree1 = ttk.Treeview(st)
    cols = list(data.columns)
    tree1.grid(column= 0, row = 0)
    tree1.column("#0", width=0)
    tree1["columns"] = cols
    for i in cols:
        tree1.column(i, width=60, anchor="w")
        tree1.heading(i, text=i, anchor='w')
    for index, row in data.iterrows():
        tree1.insert("", 0, values=list(row))

def show_stat(value):
    global display
    global drop
    global desc
    global tree
    
    st = Toplevel()
    st.title('Machine Learning Models')
    st.iconbitmap('plots\deep-learning.ico')
    st.geometry("850x600")
    st['background']='#7AC5CD'

    selcet = value
    if selcet == ' Live Facebook Data':
        draw_table1(st, Live().desc())
        img1 = ImageTk.PhotoImage(Image.open("plots/num_loves.png"))
        le = Label(st, image= img1).grid(row=1, column=0)
    elif selcet == ' Mobile Data':
        img2 = ImageTk.PhotoImage(Image.open("plots/3G_supported.png"))
        le2 = Label(st, image= img2).grid(row=1, column=0)
        img3 = ImageTk.PhotoImage(Image.open("plots/4G_supported.png"))
        le3 = Label(st, image= img3).grid(row=1, column=1)
        draw_table1(st, Mobile().desc())
    elif selcet == ' Stroke Data':
        draw_table1(st, Stroke().desc())
        img5 = ImageTk.PhotoImage(Image.open("plots/StrokePlot1.png"))
        le5 = Label(st, image= img5).grid(row=1, column=0)
        
    elif selcet == ' Health Insurance Data':
        draw_table1(st, Ins().load().describe())
        img6 = ImageTk.PhotoImage(Image.open("plots/smoker.png"))
        le6 = Label(st, image= img6).grid(row=1, column=0)
        img7 = ImageTk.PhotoImage(Image.open("plots/insur.png"))
        le7 = Label(st, image= img7).grid(row=1, column=1)
        


    st.mainloop()

def apply_model(mod, value, m, le, but):
    global model
    global liv_data
    global ins_data
    global mob_data
    global str_data

    but.pack_forget()
    le.pack_forget()

    but = Button(m, text="Get Accuracy", command=lambda: apply_model(mod, value, m, le, but))

    ans = ""
    selcet = value
    if selcet == ' Live Facebook Data':
        if(mod.get() == ' K-means'):
            ans = str(model.K_means(liv_data))
        elif(mod.get() == ' Random forest'):
            ans = str(model.randforst(liv_data))
        elif(mod.get() == ' Knn'):
            ans = str(model.knn(liv_data))
        elif(mod.get() == ' Desision Tree'):
            ans = str(model.decision(liv_data))
        elif(mod.get() == ' Logistic Regression'):
            ans = str(model.Logistic(liv_data))
        else:
            ans = "Please choose a model"


    elif selcet == ' Mobile Data':
        if(mod.get() == ' Linear Regression'):
            ans = str(model.Linear(mob_data))
        elif(mod.get() == ' Random forest'):
            ans = str(model.randforst(mob_data))
        elif(mod.get() == ' Knn'):
            ans = str(model.knn(mob_data))
        elif(mod.get() == ' Desision Tree'):
            ans = str(model.decision(mob_data))
        elif(mod.get() == ' Logistic Regression'):
            ans = str(model.Logistic(mob_data))
        else:
            ans = "Please choose a model"

    elif selcet == ' Stroke Data':
        if(mod.get() == ' Gaussian Naive Bayes'):
            ans = str(model.naive(str_data))
        elif(mod.get() == ' Random forest'):
            ans = str(model.randforst(str_data))
        elif(mod.get() == ' Knn'):
            ans = str(model.knn(str_data))
        elif(mod.get() == ' Desision Tree'):
            ans = str(model.decision(str_data))
        elif(mod.get() == ' Logistic Regression'):
            ans = str(model.Logistic(str_data))
        else:
            ans = "Please choose a model"

    else:
        if(mod.get() == ' Linear Regression'):
            ans = str(model.Linear(ins_data))
        else:
            ans = "Please choose a model"

    le = Label(m, text= ans)
    le.pack()
    but.pack()
       


def show_model(value):
    
    global ans
    mo = Toplevel()
    mo.title('Machine Learning Models') 
    mo.iconbitmap('plots\deep-learning.ico')
    mo.geometry("400x350")
    mo['background']='#7AC5CD'

    clickedd = StringVar()

    selcet = value
    if selcet == ' Live Facebook Data':
        drop1 = OptionMenu(mo, clickedd, *Live_list).pack()

    elif selcet == ' Mobile Data':
        drop2 = OptionMenu(mo, clickedd, *Mobile_list).pack()

    elif selcet == ' Stroke Data':
        drop3 = OptionMenu(mo, clickedd, *Stroke_list).pack()

    elif selcet == ' Health Insurance Data':
        drop4 = OptionMenu(mo, clickedd, *Health_list).pack()

    le = Label(mo, text= ans)
    but = Button(mo, text="Get Accuracy", command=lambda: apply_model(clickedd, value, mo, le, but))
    le.pack()
    but.pack()


    mo.mainloop()


root = Tk()
root.title('Machine Learning Models')
root.iconbitmap('plots\deep-learning.ico')
root.geometry("1200x500")  
root['background']='#7AC5CD'

ans = ""

model = Model()

mob = Mobile()
mob_data = mob.load()

stro = Stroke()
str_data = stro.load()

liv = Live()
liv_data = liv.load()

ins = Ins()
ins_data = ins.load()

def draw_table(data):
    global tree
    tree.grid_forget()
    cols = list(data.columns)
    tree.pack()
    tree.column("#0", width=0)
    tree["columns"] = cols
    for i in cols:
        tree.column(i, width=50, anchor="w")
        tree.heading(i, text=i, anchor='w')
    for index, row in data.head(10).iterrows():
        tree.insert("",index=index, values=list(row))


def print_head(value):
    global display
    global drop
    
    display.grid_forget()
    selcet = value
    if selcet == ' Live Facebook Data':
        draw_table(liv_data)
    elif selcet == ' Mobile Data':
        draw_table(mob_data)
    elif selcet == ' Stroke Data':
        draw_table(str_data)
    elif selcet == ' Health Insurance Data':
        draw_table(ins_data)




data_list = [
    ' Select Your data',
    ' Live Facebook Data', 
    ' Mobile Data', 
    ' Stroke Data',
    ' Health Insurance Data']

Live_list = [
    ' Select Your Model',
    ' K-means', 
    ' Random forest', 
    ' Knn',
    ' Desision Tree',
    ' Logistic Regression']    

Mobile_list = [
    ' Select Your Model',
    ' Linear Regression', 
    ' Random forest', 
    ' Knn',
    ' Desision Tree',
    ' Logistic Regression']   

Stroke_list = [
    ' Select Your Model',
    ' Gaussian Naive Bayes', 
    ' Random forest', 
    ' Knn',
    ' Desision Tree',
    ' Logistic Regression']        

Health_list = [
    ' Select Your Model',
    ' Linear Regression', 
    ] 


clicked = StringVar()
clicked.set(' Mobile Data')

drop = OptionMenu(root, clicked, *data_list).pack()

tree = ttk.Treeview(root)
tree.pack()

display = Button(root, text= "display data", command=  lambda: print_head(clicked.get()))
display.pack()


desc = Button(root, text= "statistics", command=  lambda: show_stat(clicked.get()))
desc.pack()

models = Button(root, text= "Chose Your Model", command=  lambda: show_model(clicked.get()))
models.pack()



root.mainloop()