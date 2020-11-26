import tkinter

root = tkinter.Tk()
root.iconbitmap('F:/Coding Practice/Visual Studio Code/Python/TkinterEnv/Codes/Basics/Images/Icon/CalcIcon.ico')
root.geometry('350x400')
root.resizable(0, 0)


# Why so we need Frames in Tkinter
# (The below code throws error as the both pack and grid manager cannot be used in a same container)
# NameLabel = tkinter.Label(root,text="Hello World")
# NameLabel.pack()
# TimeLabel = tkinter.Label(root,text="From Earth")
# TimeLabel.grid()


# Part 5 (Frames)
# Frame Definition
PackFrame = tkinter.Frame(root, bg="pink")
GridFrame1 = tkinter.Frame(root, bg="Light Green")
GridFrame2 = tkinter.LabelFrame(root, text="Grid System Rules", borderwidth=(5))

PackFrame.pack(fill="both", expand=True)
GridFrame1.pack(fill="x", expand=True)
GridFrame2.pack(fill="both", expand=True)

tkinter.Label(PackFrame, text="textBox").pack()
tkinter.Label(PackFrame, text="textBox").pack()
tkinter.Label(PackFrame, text="textBox").pack()

tkinter.Label(GridFrame1, text="textBox").grid(row=0, column=0)
tkinter.Label(GridFrame1, text="textBox").grid(row=1, column=1)
tkinter.Label(GridFrame1, text="textBox").grid(row=2, column=2)
# tkinter.Label(GridFrame1, text="This is a really long text in this container").grid(row=3, column=0)

tkinter.Label(GridFrame2, text="This is a really long text for checking purposes").grid(row=3, column=0)

# Final Part
root.mainloop()
