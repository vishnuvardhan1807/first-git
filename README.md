my image processor app
#my code starts here 
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("images")



my_pic1 = Image.open("angel/vishnu1.png")
resized1 = my_pic1.resize((720,720),Image.ANTIALIAS)


my_pic2 = Image.open("angel/vishnu2.png")
resized2 = my_pic2.resize((720,720),Image.ANTIALIAS)

my_pic3 = Image.open("angel/vishnu3.png")
resized3 = my_pic3.resize((720,720),Image.ANTIALIAS)

my_pic4 = Image.open("angel/rohan.png")
resized4 = my_pic4.resize((720,720),Image.ANTIALIAS)

my_pic5 = Image.open("angel/rohan1.png")
resized5 = my_pic5.resize((720,720),Image.ANTIALIAS)

my_pic6 = Image.open("angel/rohit1.png")
resized6 = my_pic6.resize((720,720),Image.ANTIALIAS)

my_pic7 = Image.open("angel/rohit2.png")
resized7 = my_pic7.resize((720,720),Image.ANTIALIAS)


new_pic1 = ImageTk.PhotoImage(resized1)
new_pic2 = ImageTk.PhotoImage(resized2)
new_pic3 = ImageTk.PhotoImage(resized3)
new_pic4 = ImageTk.PhotoImage(resized4)
new_pic5 = ImageTk.PhotoImage(resized5)
new_pic6 = ImageTk.PhotoImage(resized6)
new_pic7 = ImageTk.PhotoImage(resized7)

my_list = [new_pic1,new_pic2,new_pic3,new_pic4,new_pic5,new_pic6,new_pic7]
my_label=Label(image=new_pic1)
my_label.grid(row=0,column=0,columnspan=3)

status = Label(root,text="image 1 of "+ str(len(my_list)),bd=1,relief=SUNKEN,anchor=E)

def forward(image_no):
    global my_label
    global button_forward
    global button_backward
    
    my_label.grid_forget()
    my_label=Label(image=my_list[image_no-1])
    button_forward=Button(root,text=">>",command=lambda: forward(image_no+1))
    button_backward=Button(root,text="<<",command=lambda: backward(image_no-1))
    
    status = Label(root,text="image "+str(image_no) + " of " + str(len(my_list)),bd=1,relief=SUNKEN,anchor=E)
    
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    my_label.grid(row=0,column=0,columnspan=3)
    button_forward.grid(row=1,column=0)
    button_backward.grid(row=1,column=2)
    

def backward(image_no):
     global my_label
     global button_forward
     global button_backward
     
      
     my_label.grid_forget()
     my_label=Label(image=my_list[image_no-1])
     button_forward=Button(root,text=">>",command=lambda: forward(image_no+1))
     button_backward=Button(root,text="<<",command=lambda: backward(image_no-1))
     status = Label(root,text="image "+str(image_no) + " of " + str(len(my_list)),bd=1,relief=SUNKEN,anchor=E) 
     my_label.grid(row=0,column=0,columnspan=3)
     button_forward.grid(row=1,column=0)
     button_backward.grid(row=1,column=2)
    


button_forward=Button(root,text=">>",command=lambda: forward(2))
button_backward=Button(root,text="<<",command=backward)
button=Button(root,text="press to move",fg="green")

button_forward.grid(row=1,column=0)
button_backward.grid(row=1,column=2)
button.grid(row=1,column=1)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
root.mainloop()

#tjis is muyy image processor app
