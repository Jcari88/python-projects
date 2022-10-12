import random
from tkinter import *
import tkinter as tk
Ewords = ["Puppy", "Dog", "Apple", "Pizza", "Feet", "Mice", "Rat", "Running", "Cake","Hamburger", "Pancake"
              , "Cave", "Airplane", "Computer"]
Hwords = ["Supercalifragilisticexpialidocious", "Worcestershire", "Hippopotomonstrosesquippedaliophobia",
             "Ubiquitous", "Nefarious", "Euphoria", "Hypothesis"]
word='' 
dashes = ""
gword=FALSE
incorrect=0

def getword(mode):
    global word, dashes, gword, incorrect
    body('delete', incorrect)  
    pole()  
    buttons= [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26]
    for b in buttons:
        buttoncolor(b, 'light grey')
    gword=TRUE
    i=0
    dashes = "" ##clear last dashes
    if mode == "easy":
        word = random.choice(Ewords) #new word
    elif mode =="hard":
        word = random.choice(Hwords)#new word
        label2['font']=("Arial",14)
    while i!=len(word): #get dashes
        dashes = str(dashes+" _ ")
        i+=1
    label2['text']=dashes #print dashes
    label1['text']=""
    label3['text']=""
    print(word)

def whenpressed(b):
    global word, dashes, gword, incorrect 
    if gword==TRUE:
        if b['bg']!='red':# if button not red then continue
            x=0
            isin = FALSE
            for l in word:
                x+=1
                if l.upper() == b['text']:
                    dashes = dashes[0:x]+ str(b['text']) + dashes[x+1:]
                    isin=TRUE
                x+=2      
            label2['text']=dashes #print dashes
            
            if isin ==FALSE:
                incorrect+=1 
                body('create', incorrect) 
                
            ndashes = ""
            for n in dashes:
                if n!=" "and n!="_":
                    ndashes = ndashes+n
                    #print(ndashes)
                    
            if ndashes == word.upper():
                gword=FALSE # turn keyboard off
                label1['text']= "Win!"
                label3['text']="Press Easy or Hard to play again!"
                
            buttoncolor(b, 'red')
            
def buttoncolor(b, bcolor):   
    b['bg']= bcolor
    
def pole():
    canvas.create_line(0,190,200,190)#ground
    canvas.create_line(50,190,50,10)#pole
    canvas.create_line(50,10,100,10)#top
    canvas.create_line(100,10,100,30)#rope
    
def body(DorC, i):
    global incorrect, gword
    if DorC== 'create':
        if incorrect==1:
            head = canvas.create_oval(90 , 60, 110, 30)#head
        if incorrect==2:
            body = canvas.create_line(100,60,100,120)#body
        if incorrect==3:
            rarm=canvas.create_line(100,60,70,80)#arm right(left side of canvas)
        if incorrect==4:
            larm=canvas.create_line(100,60,130,80)#arm left(right side of canvas)
        if incorrect==5:
            rleg=canvas.create_line(100,120,70,160)#leg
        if incorrect==6:
            lleg=canvas.create_line(100,120,130,160) #leg
            gword=FALSE # turn keyboard off
            label1['text']= "GAME OVER!"
            label2['text']="The word was "+word+"!"
            label3['text']="Press Easy or Hard to play again!"
    if DorC == 'delete' :
        canvas.delete(ALL) 
        incorrect=0  
            

window =Tk()
window.title("Hangman")
window.configure(bg='light grey')
window.geometry('800x650')
size=200
color ='lightgrey'

bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM, anchor=CENTER)



b1 = Button(bottomFrame, text='Q',height= 5, width=10, bg=color, command=lambda:whenpressed(b1))
b2 = Button(bottomFrame, text='W',height= 5, width=10, bg=color, command=lambda:whenpressed(b2))
b3 = Button(bottomFrame, text='E',height= 5, width=10, bg=color, command=lambda:whenpressed(b3))
b4 = Button(bottomFrame, text='R',height= 5, width=10, bg=color, command=lambda:whenpressed(b4))
b5 = Button(bottomFrame, text='T',height= 5, width=10, bg=color, command=lambda:whenpressed(b5))
b6 = Button(bottomFrame, text='Y',height= 5, width=10, bg=color, command=lambda:whenpressed(b6))
b7 = Button(bottomFrame, text='U',height= 5, width=10, bg=color, command=lambda:whenpressed(b7))
b8 = Button(bottomFrame, text='I',height= 5, width=10, bg=color, command=lambda:whenpressed(b8))
b9 = Button(bottomFrame, text='O',height= 5, width=10, bg=color, command=lambda:whenpressed(b9))
b10 = Button(bottomFrame, text='P',height= 5, width=10, bg=color, command=lambda:whenpressed(b10))
b11 = Button(bottomFrame, text='A',height= 5, width=10, bg=color, command=lambda:whenpressed(b11))
b12 = Button(bottomFrame, text='S',height= 5, width=10, bg=color, command=lambda:whenpressed(b12))
b13 = Button(bottomFrame, text='D',height= 5, width=10, bg=color, command=lambda:whenpressed(b13))
b14 = Button(bottomFrame, text='F',height= 5, width=10, bg=color, command=lambda:whenpressed(b14))
b15 = Button(bottomFrame, text='G',height= 5, width=10, bg=color, command=lambda:whenpressed(b15))
b16 = Button(bottomFrame, text='H',height= 5, width=10, bg=color, command=lambda:whenpressed(b16))
b17 = Button(bottomFrame, text='J',height= 5, width=10, bg=color, command=lambda:whenpressed(b17))
b18 = Button(bottomFrame, text='K',height= 5, width=10, bg=color, command=lambda:whenpressed(b18))
b19 = Button(bottomFrame, text='L',height= 5, width=10, bg=color, command=lambda:whenpressed(b19))
b20 = Button(bottomFrame, text='Z',height= 5, width=10, bg=color, command=lambda:whenpressed(b20))
b21 = Button(bottomFrame, text='X',height= 5, width=10, bg=color, command=lambda:whenpressed(b21))
b22 = Button(bottomFrame, text='C',height= 5, width=10, bg=color, command=lambda:whenpressed(b22))
b23 = Button(bottomFrame, text='V',height= 5, width=10, bg=color, command=lambda:whenpressed(b23))
b24 = Button(bottomFrame, text='B',height= 5, width=10, bg=color, command=lambda:whenpressed(b24))
b25 = Button(bottomFrame, text='N',height= 5, width=10, bg=color, command=lambda:whenpressed(b25))
b26 = Button(bottomFrame, text='M',height= 5, width=10, bg=color, command=lambda:whenpressed(b26))

b1.grid(column=0, row = 1)
b2.grid(column=1, row = 1)
b3.grid(column=2, row = 1)
b4.grid(column=3, row = 1)
b5.grid(column=4, row = 1)
b6.grid(column=5, row = 1)
b7.grid(column=6, row = 1)
b8.grid(column=7, row = 1)
b9.grid(column=8, row = 1)
b10.grid(column=9, row = 1)
b11.grid(column=0, row = 2)
b12.grid(column=1, row = 2)
b13.grid(column=2, row = 2)
b14.grid(column=3, row = 2)
b15.grid(column=4, row = 2)
b16.grid(column=5, row = 2)
b17.grid(column=6, row = 2)
b18.grid(column=7, row = 2)
b19.grid(column=8, row = 2)
b20.grid(column=1, row = 3)
b21.grid(column=2, row = 3)
b22.grid(column=3, row = 3)
b23.grid(column=4, row = 3)
b24.grid(column=5, row = 3)
b25.grid(column=6, row = 3)
b26.grid(column=7, row = 3)


##########################mid
midFrame = Frame(window)
midFrame.pack(side=BOTTOM, anchor=CENTER)
canvas= Canvas(midFrame, width=size, height=size)
#canvas.place(relx=0.5, rely=0.5, anchor= CENTER)
canvas.grid(column=2, row=0)
pole()
##########################toolbar
toolbar = Frame(window,bg='grey')
lbl=Label(toolbar, text="Press Easy or Hard for a new word ", bg='grey')
lbl.pack(side=LEFT)
tb1 = Button(toolbar, text= 'Easy', command=lambda:getword("easy"))
tb1.pack(side= LEFT, padx=2,pady=2)
tb2 = Button(toolbar, text= 'Hard', command=lambda:getword("hard"))
tb2.pack(side= LEFT, padx=2,pady=2)
toolbar.pack(side=TOP,fill=X) #SHOW TOOLBAR
###########top
top = Frame(window,bg='light grey')
label1= Label(top, text= "Welcome!", font=("Arial, 25"), bg=color)
label2 = Label(top, text="click easy or hard to start",font=("Arial",25) , bg = color)
label3 =Label(top, text="",font=("Arial",20) , bg = color)
label1.pack()
label2.pack()
label3.pack()
top.pack(side=TOP)


window.mainloop()
