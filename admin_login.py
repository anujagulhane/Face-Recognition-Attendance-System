from tkinter import *
import sys
import os
import datetime
from tkinter import messagebox
now= datetime.datetime.now()

root = Tk()
top=Toplevel()

def command1():
	if entry1.get() == 'Admin_name' and entry2.get() == 'password' or entry1.get() == 'test' and entry2.get() == 'pass':
		root.deiconify()   #displays the window,after using withdraw methods
		top.destroy()

	else:
		messagebox.showerror('Error',"Error,invalid username or password")
	

def command2():
	top.destroy()
	root.destroy()
	sys.exit()

top.geometry("600x400+800+200")
top.title('Login Screen')
top.configure(background='white')

photo2=PhotoImage(file='admin.png')
photo=Label(top,image=photo2,bg='white')
lbl1=Label(top,text='Admin_name:',font=('times new roman',15))
entry1=Entry(top)

lbl2=Label(top,text='Password:',font=('times new roman',15))
entry2=Entry(top,show="*")

button1=Button(top,text='Login',bg="black",fg="white", command=command1).place(x=240,y=350)
button2=Button(top,text='Cancel',bg="black",fg="white",command=lambda:command2()).place(x=320,y=350)

entry2.bind('<Return>',command1)

photo.pack()
lbl1.pack()

entry1.pack()
lbl2.pack()
entry2.pack()

def function1():
    os.system("py dataSet.py")

def function2():  
    os.system("py trainer.py")

def function5():
    os.system("py report.py")
    os.startfile("C:/Users/Anuja/Desktop/Anuja_gulhane/GOAL/HTML/Face_Recognition_new/attendance_files/"+'attendance'+str(now.strftime("%Y-%m-%d"))+'.xlsx')

root.title('Admin Login')
root.geometry("600x400+800+200")


C1 = Canvas(root, bg="blue", height=250, width=300)
filename1 = PhotoImage( file = "image.png")
background_label1 = Label( root, image=filename1)
background_label1.place(x=0, y=0, relwidth=1, relheight=1)
  
label1 = Label(root,text = "Admin-window",font=("times new roman",20),fg="white",bg="black",height=2) 
label1.pack()

button3=Button(root,text="Create new Dataset",font=('times new roman',20),borderwidth=10,bg="black",fg="white",command=function1).place(x=190,y=100)

button4=Button(root,text="Train Dataset",font=('times new roman',20),borderwidth=10,bg="black",fg="white",command=function2).place(x=220,y=180)

button5=Button(root,text="Display Report",font=('times new roman',20),borderwidth=10,bg="black",fg="white",command=function5).place(x=210,y=260)

button6= Button(root, text = "Exit",bg="black",fg="white",borderwidth=10,command = root.destroy).place(x=290,y=350)    # Create exit button. 

C1.pack() 
root.withdraw()
root.mainloop()