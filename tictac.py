from tkinter import *
import random
from tkinter import font
from tkinter import messagebox

window=Tk()
window.title("Tic Tac Toe")

  
  



root=Frame(window,height=75,width=300,bd=5,bg="#1C2C54")
frame=Frame(window,height=75,width=300,bd=5)
listt=[]
result=[]
win=[]
n=""
play_value=""


#function for raising frame
def fun(value):
    
    global n
    frame.tkraise()
    n=value
    print("Button",value,"pressed")

    
#function for getting winning combo
def win():
    aa=a['text']
    bb=b['text']
    cc=c['text']
    dd=d['text']
    ee=e['text']
    ff=f['text']
    gg=g['text']
    hh=h['text']
    ii=i['text']
    
    cross=("X","X","X")
    zero=("O","O","O")
    #row 1 combination 
    if (aa,bb,cc)==zero:
        a['bg']="#54C6BE"
        b['bg']="#54C6BE"
        c['bg']="#54C6BE"
        messagebox.showinfo("Result","Player X Wins")
    elif (aa,bb,cc)==cross:
        a['bg']="#54C6BE"
        b['bg']="#54C6BE"
        c['bg']="#54C6BE"
        messagebox.showinfo("Result","Player X Wins")

    #row 2 combination 
    if (dd,ee,ff)==zero:
        d['bg']="#54C6BE"
        e['bg']="#54C6BE"
        f['bg']="#54C6BE"
        messagebox.showinfo("Result","Player O Wins")

    elif (dd,ee,ff)==cross:
        d['bg']="#54C6BE"
        e['bg']="#54C6BE"
        f['bg']="#54C6BE"
        messagebox.showinfo("Result","Player X Wins")

     #row 3 combination 
    if (gg,hh,ii)==zero:
        g['bg']="#54C6BE"
        h['bg']="#54C6BE"
        i['bg']="#54C6BE"
        messagebox.showinfo("Result","Player O Wins")

    elif (gg,hh,ii)==cross:
        g['bg']="#54C6BE"
        h['bg']="#54C6BE"
        i['bg']="#54C6BE"
        messagebox.showinfo("Result","Player X Wins")
        
    #column 1 combination 
    if (aa,dd,gg)==zero:
        a['bg']="#54C6BE"
        d['bg']="#54C6BE"
        g['bg']="#54C6BE"
        messagebox.showinfo("Result","Player O Wins")
        
    elif (aa,dd,gg)==cross:
        a['bg']="#54C6BE"
        d['bg']="#54C6BE"
        g['bg']="#54C6BE"
        messagebox.showinfo("Result","Player X Wins")
    #column 2 combination
    if (bb,ee,hh)==zero:
        b['bg']="#54C6BE"
        e['bg']="#54C6BE"
        h['bg']="#54C6BE"
        messagebox.showinfo("Result","Player O Wins")

    elif (bb,ee,hh)==cross:
        b['bg']="#54C6BE"
        e['bg']="#54C6BE"
        h['bg']="#54C6BE"
        messagebox.showinfo("Result","Player X Wins")
        
    #column 3 combination
    if (cc,ff,ii)==zero:
        c['bg']="#54C6BE"
        f['bg']="#54C6BE"
        i['bg']="#54C6BE"
        messagebox.showinfo("Result","Player O Wins")

    elif (cc,ff,ii)==cross:
        c['bg']="#54C6BE"
        f['bg']="#54C6BE"
        i['bg']="#54C6BE"
        messagebox.showinfo("Result","Player X Wins")
        
     #diagonal 1 combination
    if (aa,ee,ii)==zero:
        a['bg']="#54C6BE"
        e['bg']="#54C6BE"
        i['bg']="#54C6BE"
        messagebox.showinfo("Result","Player O Wins")

    elif (aa,ee,ii)==cross:
        a['bg']="#54C6BE"
        e['bg']="#54C6BE"
        i['bg']="#54C6BE"
        messagebox.showinfo("Result","Player X Wins")

    #diagonal 2 combination
    if (cc,ee,gg)==zero:
        c['bg']="#54C6BE"
        e['bg']="#54C6BE"
        g['bg']="#54C6BE"
        messagebox.showinfo("Result","Player O Wins")

    elif (cc,ee,gg)==cross:
        c['bg']="#54C6BE"
        e['bg']="#54C6BE"
        g['bg']="#54C6BE"
        messagebox.showinfo("Result","Player X Wins")
                 
##############function for winning combo ends here#############                
    
    
           

#this functiion refresh the window   
def refresh():
        global n
        global listt
        global funlist
        default=window.cget('bg')
        a['text']=""
        b['text']=""
        c['text']=""
        d['text']=""
        e['text']=""
        f['text']=""
        g['text']=""
        h['text']=""
        i['text']=""
        a['bg']=default
        e['bg']=default
        f['bg']=default
        g['bg']=default
        h['bg']=default
        i['bg']=default
        b['bg']=default
        c['bg']=default
        d['bg']=default
        listt.clear()
        button_pressed.clear()
        funlist=[atext,btext,ctext,dtext,etext,ftext,gtext,htext,itext]

#main game function

player=[]
computer=[]
button_pressed=[]


def tac(value,press):
            global listt
            global result
            global win
            global n
            global play_value
            global player
            global computer
            
            i=0
            
            if play_value=="Player":
                if not listt:

                     value['text']=n
                     if value['text']=="X":
                       value['bg']="blue"
                     else:
                        value['bg']="yellow"
                         
                     listt.append(value['text'])
                     x=value.cget('text')
                     y=value['text']
                     z={x,y}
                     print(y)
                     result.append(z)
                     
                     print(x)
                   
                    
                elif listt[-1]=="O":
                    value['text']="X"
                    value['bg']="blue"
                    listt.append(value['text'])
                    x=value.cget('text')
                    y=value['text']
                    z={x,y}
                    print(x)
                    result.append(z)
                  
                    
                elif listt[-1]=="X":
                    value['text']="O"
                    value['bg']="yellow"
                    listt.append(value['text'])
                    x=value.cget('text')
                    y=value['text']
                    print(x)
                    print(y)
                    z={x,y}
                    result.append(z)
                win()
                button_pressed.append(press)
                print(press,"Button Pressed")
                
                

###################################################################################################################################################################
#####################################################################################################################################################################
            
            print("ashu")
            if play_value=="Computer":
                if not listt:

                     value['text']=n
                     if value['text']=="X":
                       value['bg']="blue"
                     else:
                        value['bg']="yellow"
                         
                     listt.append(value['text'])
                     x=value.cget('text')
                     y=value['text']
                     z={x,y}
                     print(y)
                     result.append(z)
                     
                     print(x)
                   
                    
                elif listt[-1]=="O":
                    value['text']="X"
                    value['bg']="blue"
                    listt.append(value['text'])
                    x=value.cget('text')
                    y=value['text']
                    z={x,y}
                    print(x)
                    result.append(z)
                  
                    
                elif listt[-1]=="X":
                    value['text']="O"
                    value['bg']="yellow"
                    listt.append(value['text'])
                    x=value.cget('text')
                    y=value['text']
                    print(x)
                    print(y)
                    z={x,y}
                    result.append(z)
                button_pressed.append(press)
                print(press,"Button Pressed")
                
                win()
                ml()
#################################################################################################################################################################
listt2=[]
def atext():
    global button_pressed
    if 1 not in button_pressed:
            a['text']="X"
           
    print("Called")
def btext():
    global button_pressed
    if 2 not in button_pressed:
            b['text']="X"
    print("Called")
def ctext():
    global button_pressed
    if 3 not in button_pressed:
            c['text']="X"
    print("Called")

def dtext():
    global button_pressed
    if 4 not in button_pressed:
            d['text']="X"
    print("Called")
def etext():
    global button_pressed
    if 5 not in button_pressed:
            e['text']="X"
    print("Called")

def ftext():
    global button_pressed
    if 6 not in button_pressed:
            f['text']="X"
    print("Called")

def gtext():
    global button_pressed
    if 7 not in button_pressed:
            g['text']="X"
    print("Called")
def htext():
    global button_pressed
    if 8 not in button_pressed:
            h['text']="X"
    print("Called")
def itext():
    global button_pressed
    if 3 not in button_pressed:
            i['text']="X"
    print("Called")

funlist=[[etext,gtext,htext,itext],[atext,ctext,etext,gtext,htext,itext],[etext,btext,gtext,htext,itext],[atext,btext,ctext,dtext,etext,ftext,gtext,htext,itext],etext,ftext,gtext,htext,itext]


def ml():
    global listt
    global listt2
    global funlist
    global button_pressed
    
    aa=a['text']
    bb=b['text']
    cc=c['text']
    dd=d['text']
    ee=e['text']
    ff=f['text']
    gg=g['text']
    hh=h['text']
    ii=i['text']


    listt3=[(a['text'],aa),(b['text'],bb),(c['text'],cc),(d['text'],dd),(e['text'],ee),(f['text'],ff),(g['text'],gg),(h['text'],hh), (i['text'],ii) ]
    listt4=[a,b,c,d,e,f,g,h,i]
    
    listt2=[aa,bb,cc,dd,ee,ff,gg,hh,ii]
    
    print(listt2)
    if listt[-1]=="O":
        index=button_pressed[-1]
        move(index)
        
         
         
         
            
                    
            


def move(index):
     global listt2
     global funlist
     global listt
     if listt2[index]=="O":
         r=random.choice(funlist[index])
         r()
         
         listt.append("X")
         print(funlist)
    
               
            
        


####################################################################################################################################################################            
def choose():
    root.tkraise()
    print("Choose button pressed")
    global n
    global listt
    default=window.cget('bg')
    a['text']=""
    b['text']=""
    c['text']=""
    d['text']=""
    e['text']=""
    f['text']=""
    g['text']=""
    h['text']=""
    i['text']=""
    a['bg']=default
    e['bg']=default
    f['bg']=default
    g['bg']=default
    h['bg']=default
    i['bg']=default
    b['bg']=default
    c['bg']=default
    d['bg']=default      
    n=""
    listt.clear()
            
            
            
def play(value):
    global play_value
    play_value=value
    print(play_value)
    C.tkraise()
      

#main game menu start here

C=Frame(window,height=300,width=200,bd=7,bg="red")


a=Button(C,cursor="arrow",command=lambda:tac(a,0),bg="white",font=("Helvetica","20"),height=1,width=3)
a.place(x=55,y=10)

b=Button(C,cursor="arrow",command=lambda:tac(b,1),bg="white",font=("Helvetica","20"),height=1,width=3)
b.place(x=110,y=10)
c=Button(C,cursor="arrow",command=lambda:tac(c,2),bg="white",font=("Helvetica","20"),height=1,width=3)
c.place(x=165,y=10)
d=Button(C  ,cursor="arrow",command=lambda:tac(d,3),bg="white",font=("Helvetica","20"),height=1,width=3)
d.place(x=55,y=55)
e=Button(C ,cursor="arrow",command=lambda:tac(e,4),bg="white",font=("Helvetica","20"),height=1,width=3)
e.place(x=110,y=55)
f=Button(C,cursor="arrow",command=lambda:tac(f,5),bg="white",font=("Helvetica","20"),height=1,width=3)
f.place(x=165,y=55)

g=Button(C,cursor="arrow",command=lambda:tac(g,6),bg="white",font=("Helvetica","20"),height=1,width=3)
g.place(x=55,y=100)
h=Button(C,cursor="arrow",command=lambda:tac(h,7),bg="white",font=("Helvetica","20"),height=1,width=3)
h.place(x=110,y=100)
i=Button(C,cursor="arrow",command=lambda:tac(i,8),bg="white",font=("Helvetica","20"),height=1,width=3)
i.place(x=165,y=100)

j=Button(C,text="New Game",cursor="arrow",bg="#F7B15C",relief=GROOVE,bd=3,command=refresh,font=("Helvetica","15"),height=1,width=9)
j.place(x=20,y=180)

l=Button(C,text="Choose",cursor="arrow",relief=GROOVE,bd=3,command=lambda:choose(),font=("Helvetica","15"),height=1,width=9)
l.place(x=155,y=180)

k=Button(C,text="Exit",cursor="arrow",relief=GROOVE,bd=3,command=window.destroy,font=("Helvetica","15"),height=1,width=5)
k.place(x=110,y=240)

C.grid(row=0, column=0, sticky='news')



#choice


label1=Label(root,text="Enter your choice",fg='red',font=("Times", "20", "bold italic"),bg="#1C2C54")
label1.place(x=40,y=50)

button1=Button(root,text="CROSS\nX",bg="blue",relief=GROOVE,bd=3,cursor="arrow",command=lambda:fun("X"),font=("Helvetica 15 bold"),height=2,width=10)
button1.place(x=15,y=100)

button2=Button(root,text="ZERO\nO",bg="yellow",cursor="arrow",relief=GROOVE,bd=3,command=lambda:fun("O"),font=("Helvetica 15 bold"),height=2,width=10)
button2.place(x=160,y=100)

button3=Button(root,text="Quit",bg="red",cursor="arrow",relief=GROOVE,bd=3,command=window.destroy,font=("Helvetica","15"),height=2,width=8)
button3.place(x=100,y=190)

root.grid(row=0, column=0, sticky='news')



########################frame 3

player=Button(frame,text="Player",bg="red",cursor="arrow",relief=GROOVE,command=lambda:play("Player"),bd=3,font=("Comic Sans MS"," 15 "),height=2,width=8)
player.place(x=100,y=80)
computer=Button(frame,text="Computer",bg="red",cursor="arrow",relief=GROOVE,command=lambda:play("Computer"),bd=3,font=("Comic Sans MS"," 15 "),height=2,width=8)
computer.place(x=100,y=190)

frame.grid(row=0, column=0, sticky='news')

root.tkraise()





window.mainloop()
