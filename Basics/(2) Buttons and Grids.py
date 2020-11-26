import tkinter

root = tkinter.Tk()
root.iconbitmap('F:/Coding Practice/Visual Studio Code/Python/TkinterEnv/Codes/Basics/Images/Icon/CalcIcon.ico')
root.geometry('350x400')
root.resizable(0, 0)


# Part 4 (Buttons and Grids)
NameButton = tkinter.Button(root,text="Press",bg='#009788',activebackground='#01c853',borderwidth=3)
NameButton.grid(row=0, column=0,ipadx=2)

TimeButton = tkinter.Button(root,text="Time",bg='#8bc24a',activebackground='#33691e',borderwidth=3)
TimeButton.grid(row=0, column=1,ipadx=2)

PlaceButton = tkinter.Button(root,text="Place",bg='#eeff41',activebackground='#aeea00',borderwidth=3)
PlaceButton.grid(row=0,column=2,ipadx=2)

DayButton = tkinter.Button(root, text="Day",bg='#ffd54f',borderwidth=5,activebackground='#ff8e01')
DayButton.grid(row=1,column=0,columnspan=3,sticky="WE")

TestButton1 = tkinter.Button(root,text="test")
TestButton2 = tkinter.Button(root,text="test")
TestButton3 = tkinter.Button(root,text="test")
TestButton4 = tkinter.Button(root,text="test")
TestButton5 = tkinter.Button(root,text="test")
TestButton6 = tkinter.Button(root,text="test")

TestButton1.grid(row=3, column=0,padx=5,pady=5)
TestButton2.grid(row=3, column=1,padx=5,pady=5)
TestButton3.grid(row=3, column=2,padx=5,pady=5)
TestButton4.grid(row=4, column=0,padx=5,pady=5)
TestButton5.grid(row=4, column=1,padx=5,pady=5)
TestButton6.grid(row=4, column=2,padx=5,pady=5)


# Final Part
root.mainloop()