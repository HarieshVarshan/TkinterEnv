import tkinter
from PIL import ImageTk,Image 

root = tkinter.Tk()
root.title(string="Image Basics")
root.geometry("700x700")
root.resizable(0,0)
root.config(bg="#c5e1a6")

# Part 10 (PNG Images)
Image_1 = tkinter.PhotoImage(file = "TkinterEnv/Codes/Basics/Images/Icon/CamIcon.png")
Label_1 = tkinter.Label(image = Image_1)
Label_1.pack()

Button_1 = tkinter.Button(image = Image_1)
Button_1.pack()

# Part 11 (PNG method does not work for JPG Images)
#Image_2 = tkinter.PhotoImage(file = "TkinterEnv/Codes/Basics/Images/Icon/Scenery.jpeg")
#Label_2 = tkinter.Label(image = Image_1)
#Label_2.pack()

# Part 12 (Using PIL for JPG Images)
JPG_Image = ImageTk.PhotoImage(Image.open("TkinterEnv/Codes/Basics/Images/Icon/BlackHole.jpg"))
JPG_Label = tkinter.Label(root,image = JPG_Image)
JPG_Label.pack()

def JPG_Image_Func():  # --> Belongs to Part 13 
    global Func_Image
    Func_Image = ImageTk.PhotoImage(Image.open("TkinterEnv/Codes/Basics/Images/Icon/Eye.jpg"))
    Func_Image_Label = tkinter.Label(root,image = Func_Image)
    Func_Image_Label.pack()

# Part 13 (JPG Images inside Functions)
JPG_Image_Func()

root.mainloop()