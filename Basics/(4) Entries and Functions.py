import tkinter
from tkinter import END

root = tkinter.Tk()
root.iconbitmap('F:/Coding Practice/Visual Studio Code/Python/TkinterEnv/Codes/Basics/Images/Icon/CalcIcon.ico')
root.geometry('350x400')
root.resizable(0, 0)
root.config(bg = "Light Blue")


#Define the command function --> This comes under Part 7
def printOut():
    TextOut = tkinter.Label(OutputFrame,text = TextIn.get())
    TextOut.pack()
    # Clears the input box after hitting Print everytime
    TextIn.delete(0,END)

def Incrementer(number):  # --> This comes under Part 8
    global value
    CountOut = tkinter.Label(OutputFrame,text=number)
    CountOut.pack()
    value = number+1


# Part 6 (Inputting Functions)
# Frame Definition
InputFrame = tkinter.Frame(root,bg = "Pink",width = 500,height = 100)
OutputFrame = tkinter.Frame(root, bg = "Light Green",width = 500,height = 900)
InputFrame.pack(padx=10,pady=10)
OutputFrame.pack(padx = 10,pady=(0,10))

# Getting Input
TextIn = tkinter.Entry(InputFrame,width = 40)
TextIn.grid(row=0,column=0,padx=5,pady=5)

# To prevent the Frame from shrinking to the size of the widget it holds.
InputFrame.grid_propagate(0)
OutputFrame.pack_propagate(0)

# Part 7 (Actions/Functionalities)
PrintButton = tkinter.Button(InputFrame,text = "Print",command = printOut)
PrintButton.grid(padx=5, pady=5,ipadx=5,row = 0,column = 1)



# Part 8 (Using Lambda Functions)
value = 0
CountButton = tkinter.Button(InputFrame,text = "Count",command = lambda: Incrementer(value))
CountButton.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky = "WE")

# Final Part
root.mainloop()