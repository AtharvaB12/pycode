from tkinter import messagebox
from tkinter import *


a=0
b=0
c=0
d=0


def Miguel_de_cervantes():
    global a
    a=a+1
    print("Miguel de cervantes",a)
    messagebox.showinfo('info','your vote submitted succesfully')
    
def Charles_Dickens():
    global b
    b=b+1
    print("Charles Dickens",b)
    messagebox.showinfo('info','your vote submitted succesfully')
    
def JRR_Tolkien():
    global c
    c=c+1
    print("J.R.R Tolkien",c)
    messagebox.showinfo('info','your vote submitted succesfully')

def Antoine_de_Saint_Exuper():
    global d
    d=d+1
    print("Antoine.de.Saint-Exuper",d)
    messagebox.showinfo('info','your vote submitted succesfully')
    

def result():
    
    if([a]>[b,c,d]):
        print("RESULT = Miguel de cervantes Wins")
    elif([b]>[a,c,d]):
        print("RESULT = Charles Dickens Wins")
    elif([c] > [a,b,d]):
        print("RESULT = J.R.R_Tolkien Wins")
    elif([d]> [a,b,c]):
        print("RESULT = Antoine.de.Saint-Exuper Wins")
    else:
        print("SCORE ON LEVEL")
    
    

r=Tk()
r.geometry('600x700')
r.title('Opinion Poll')
l=Label(r,text='Opinion Poll ',font=('calibri',30,'bold'),fg='brown')
l.place(x=185,y=5)

l=Label(r,text='Who is your favourite author? ',font=('calibri',20,'bold'),fg='black')
l.place(x=10,y=110)

b1=Button(r,text='Miguel de cervantes',font=('calibri',22,'bold'),fg='black',height=0,width=20,command=Miguel_de_cervantes)
b1.place(x=135,y=210)

b2=Button(r,text='Charles Dickens',font=('calibri',22,'bold'),fg='black',height=0,width=20,command=Charles_Dickens)
b2.place(x=135,y=310)


b3=Button(r,text='J.R.R Tolkien',font=('calibri',22,'bold'),fg='black',height=0,width=20,command=JRR_Tolkien)
b3.place(x=135,y=410)

b4=Button(r,text='Antoine.de.Saint-Exuper',font=('calibri',22,'bold'),fg='black',height=0,width=20,command=Antoine_de_Saint_Exuper)
b4.place(x=135,y=510)


b6=Button(r,text='RESULTS',font=('calibri',30,'bold'),fg='brown',height=0,width=10,command=result)
b6.place(x=175,y=610)
r.mainloop()
