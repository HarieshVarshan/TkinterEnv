import tkinter
from tkinter import IntVar

root = tkinter.Tk()
root.title("Radio Button Basics")
root.iconbitmap('F:/Coding Practice/Visual Studio Code/Python/TkinterEnv/Codes/Basics/Images/Icon/CalcIcon.ico')
root.geometry('350x400')
root.resizable(0, 0)
root.config(bg = "Light Blue")

Input_Frame = tkinter.LabelFrame(root,text = "Just for Fun",width = 350,height = 100)
Input_Frame.pack(padx = 10,pady = 10)
Output_Frame = tkinter.Frame(root,width = 350,height = 300,bg = "#af001f")
Output_Frame.pack(padx = 10,pady=(0,10))
Output_Frame.pack_propagate(0)

def PrintOut():
    if number.get() == 1:
        Label_Num = tkinter.Label(Output_Frame,text="One 1")
    if number.get() == 2:
        Label_Num = tkinter.Label(Output_Frame,text="Two 2")
    Label_Num.pack()

# Part 9 (Radio Buttons)
number = IntVar()
number.set(1)
Radio_Button1 = tkinter.Radiobutton(Input_Frame,text = "Print the number one",variable=number,value=1) 
Radio_Button2 = tkinter.Radiobutton(Input_Frame, text = "Print the number two",variable=number,value=2)
Print_Button = tkinter.Button(Input_Frame, text = "Print the number",command = PrintOut)

Radio_Button1.grid(row = 0,column = 0,padx = 10,pady = 10)
Radio_Button2.grid(row = 0,column = 1,padx = 10,pady = 10)
Print_Button.grid(row = 1,column = 0,columnspan = 2,padx = 10,pady = 10)    

root.mainloop()


     

