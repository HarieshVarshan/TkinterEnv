import tkinter
from tkinter import BOTH, StringVar,END

# Frame Colours
RootColour = "#D4F5F5"
InputColour = "#554348"
OutputColour = "#8C9A9E"

# Root Window
root = tkinter.Tk()
root.title(string="Welcome to GUI")
root.iconbitmap("Codes/Hello GUI World/Images/InfoIcon.ico")
root.geometry("300x400")
root.resizable(0, 0)
root.config(bg=RootColour)

# Functions
def SubmitName():
    if CaseStyle.get() == "LowerCase":
        NameLabel = tkinter.Label(OutputFrame, text="Hello "+Name.get()+", Keep Learning Tkinter!!", bg=OutputColour)
    elif CaseStyle.get() == "UpperCase":
        NameLabel = tkinter.Label(OutputFrame, text=("Hello "+Name.get()+", Keep Learning Tkinter!!").upper(), bg=OutputColour)
    NameLabel.pack()
    Name.delete(0,END)


# Output and Input Frames
InputFrame = tkinter.Frame(root, bg=InputColour, width=300, height=20)
InputFrame.pack(padx=10, pady=10, fill=BOTH)
InputFrame.pack_propagate(0)
OutputFrame = tkinter.Frame(root, bg=OutputColour, width=300, height=380)
OutputFrame.pack(padx=10, pady=(0, 10), expand=True, fill=BOTH)

# Widgets and Buttons
Name = tkinter.Entry(InputFrame, text="Enter your name: ", width=25)
Name.grid(row=0, column=0, padx=10, pady=10)
Submit = tkinter.Button(InputFrame, text="Submit", command=SubmitName)
Submit.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

# Radio Buttons
CaseStyle = StringVar()
CaseStyle.set('LowerCase')
LowerCaseButton = tkinter.Radiobutton(
    InputFrame, text="Lower Case", variable=CaseStyle, value="LowerCase", bg=InputColour)
UpperCaseButton = tkinter.Radiobutton(
    InputFrame, text="Upper Case", variable=CaseStyle, value="UpperCase", bg=InputColour)
LowerCaseButton.grid(row=1, column=0)
UpperCaseButton.grid(row=1, column=1)

root.mainloop()
