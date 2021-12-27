# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 17:36:15 2021

@author: Rino
"""

from tkinter import *
import random
root=Tk()
root.title("Password Generator")
root.geometry("400x400")

password=Label(root)
array3d=[[["1","2","3","4","5","6"],["Head","Tail"],["A","B","C","D","E","F","G","H"]]]
print(array3d[0][2][3])
print(array3d[0][0][4])
print(array3d[0][1][1])

def newpassword():
    randomno1=random.randint(0,5)
    randomno2=random.randint(0,1)
    randomno3=random.randint(0,7)
    
    letter1=str(array3d[0][0][randomno1])
    letter2=str(array3d[0][1][randomno2])
    letter3=str(array3d[0][2][randomno3])
    password["text"]=letter1 + "" + letter2 + "" + letter3
    
btn=Button(root,text="Generate New Password",command=newpassword,bg="yellow",height=2,width=20)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
password.place(relx=0.5,rely=0.5,anchor=CENTER)
    
root.mainloop()