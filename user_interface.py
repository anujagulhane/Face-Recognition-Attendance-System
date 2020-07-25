from tkinter import *
from tkinter import ttk 
import os
from tkinter import messagebox
from datetime import datetime;
from PIL import ImageTk,Image

# Create the root window with specified size and title 
root = Tk()   
root.configure(background="blue")
root.title("Welcome!!")
     
def function3():
    os.system("py Recognizer.py")
    messagebox.showinfo('Message',"Attendance added successfully")

def function4():
    os.system("py admin_login.py")
  
root.geometry("600x400+800+200")   

def open_level():
    top2 = Toplevel()
    top2.geometry("600x400+800+200")
    top2.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

    C = Canvas(top2, bg="blue", height=250, width=300)
    filename = PhotoImage( file = "image.png")
    background_label = Label( top2, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    label1 = Label(top2, text = "  FACE RECOGNITION ATTENDANCE SYSTEM  ",font=("times new roman",20),fg="white",bg="black",height=2)
    label1.pack()
    button1 =Button(top2, text = "Admin",font=("times new roman",20),bg="black",fg='white', command = function4, borderwidth=10,padx=22,pady=5).place(x=250,y=100)

    button2 = Button(top2, text = "Employee",font=("times new roman",20),bg="black",fg='white', command = open_Toplevel3, borderwidth=10,padx=5,pady=5).place(x=250,y=200)

    button4 = Button(top2, text = "Exit",bg="black",fg="white",command = top2.destroy, borderwidth=10,padx=5,pady=5).place(x=300,y=300)

    C.pack()
    top2.mainloop()

def open_Toplevel3():    #Employee

    top3 = Toplevel()  # Create widget 
    top3.title("Welcome Employee!!!")    # define title for window 
    top3.geometry("600x400+800+200")   # specify size 
    C = Canvas(top3, bg="blue", height=250, width=300)
    filename = PhotoImage( file = "image.png")
    background_label = Label( top3, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    label = Label(top3,text = "Welcome Employee" ,font=("times new roman",20),fg="white",bg="black",height=2)  # Create label 
    label.pack() 
    
    button3=Button(top3,text="Recognize + Attendance",font=('times new roman',20), borderwidth=10,bg="black",fg="white",command=function3).place(x=165,y=120)

    button= Button(top3, text = "Exit",bg="black",fg="white",command = top3.destroy, borderwidth=10).place(x=300,y=230)    # Create exit button. 
     
    C.pack()
    top3.mainloop()   # Display untill closed manually.

# Create button to open toplevel1-first page

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "logo.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
buttonn=Button(root,text="Next",font=('times new roman',20),bg="black",fg="white",command=open_level, borderwidth=10).place(x=300,y=300)

# Display untill closed manually 
root.mainloop()