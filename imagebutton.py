from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("image buttons")
root.iconbitmap("icons/superman.ico")
root.geometry("500x500")

my_image = ImageTk.PhotoImage(Image.open("angel/login1.png"))
my_image1 = Image.open("angel/vishnu1.png")
resize1 = my_image1.resize((100,100),Image.ANTIALIAS)
my_image1 = ImageTk.PhotoImage(resize1)


#my_label = Label(root,image=my_image)

#calling click function
def click():
    my_label = Label(root,text="button clicked")
    #my_label.config(text="you clicked login button")
    my_label.pack(pady=20)
#creating a button
button = Button(root,image=my_image,command=click,borderwidth=0)
button.pack(pady=20)

button = Button(root,image=my_image1,command=click,borderwidth=0)
button.pack(pady=20)

#creating a label
my_label = Label(root,text=" ")






root.mainloop()