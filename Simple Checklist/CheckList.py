import tkinter
from tkinter import END,ANCHOR,BOTTOM,SUNKEN


# Fonts and Colours
RootBackground = "#E3E1E1"
WidgetColour = "#fff1e6"
ListBoxColour = "#DDBEA9"

Font1 = ("Cambria", 10)
Font2 = ("Times New Roman", 12)


# Root Container
root = tkinter.Tk()
root.title(string="CheckList")
root.iconbitmap("Codes/Simple Checklist/Images/Check.ico")
root.resizable(width=0, height=0)
root.geometry('400x400')
root.config(bg=RootBackground)


# Functions
def addItem():
    ''' Adds items from the listEntry to the listBox '''
    if listEntry.get() == '':
        pass
    else:
        listBox.insert(END, ":) " + listEntry.get())
    listEntry.delete(0,END)

def removeItem():
    ''' Removes the selected (anchored) item '''
    listBox.delete(ANCHOR)
    
def clearList():
    ''' Clears the entire list '''
    listBox.delete(0,END)

def saveList():
    ''' Saves the content of the list to a text file '''
    ''' listBox.get() return a tuple '''
    with open('Codes/Simple Checklist/checkList.txt','w') as f:
        listBoxTuple = listBox.get(0,END)
        for item in listBoxTuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item+'\n')

def openSaved():
    ''' Reads the contents of the saved file on startup '''
    try:
        with open('Codes/Simple Checklist/checkList.txt','r') as f:
            for line in f:
                listBox.insert(END,line)
    except:
        return 


# Hover Text Functions
def removeHoverEnterFunc(e):
    hover.config(text="Remove Selected Item")
def clearHoverEnterFunc(e):
    hover.config(text="Clear List")
def saveHoverEnterFunc(e):
    hover.config(text="Save List")
def exitHoverEnterFunc(e):
    hover.config(text="C u Soon, Bye")
def addHoverEnterFunc(e):
    hover.config(text="Add Item")
def welcomeHoverEnterFunc(e):
    hover.config(text="Thank You for Using, From Hariesh Varshan")
def HoverLeaveFunc(e):
    hover.config(text="")



# Frames
inputFrame = tkinter.Frame(root, bg=RootBackground)
outputFrame = tkinter.Frame(root, bg=RootBackground)
buttonFrame = tkinter.Frame(root, bg=RootBackground)
inputFrame.pack()
outputFrame.pack()
buttonFrame.pack()

# Images
removeImage = tkinter.PhotoImage(
    file="Codes/Simple Checklist/Images/Remove.png")
clearImage = tkinter.PhotoImage(file="Codes/Simple Checklist/Images/Clear.png")
saveImage = tkinter.PhotoImage(file="Codes/Simple Checklist/Images/Save.png")
quitImage = tkinter.PhotoImage(file="Codes/Simple Checklist/Images/Exit.png")
addImage = tkinter.PhotoImage(
    file="Codes/Simple Checklist/Images/AddToList.png")
downloadImage = tkinter.PhotoImage(
    file="Codes/Simple Checklist/Images/Notes.png")

# Frame Layout
# Input Layout
listEntry = tkinter.Entry(inputFrame, width=41,
                          borderwidth=3, font=Font2, bg=WidgetColour)
AddtoList = tkinter.Button(inputFrame, text="Add Item", image=addImage,
                           activebackground=RootBackground, borderwidth=0, bg=RootBackground,command=addItem)
listEntry.grid(row=0, column=0, padx=5, pady=(10, 0))
AddtoList.grid(row=0, column=1, padx=5, pady=(7, 0))

# Output Layout
scrollBar = tkinter.Scrollbar(outputFrame,bg=ListBoxColour)
listBox = tkinter.Listbox(outputFrame, height=18,
                          width=51, font=Font1, borderwidth=3, bg=ListBoxColour,yscrollcommand=scrollBar.set)
scrollBar.config(command=listBox.yview)
listBox.grid(row=1, column=0, padx=(5,0), pady=(10, 0))
scrollBar.grid(row=1,column=1,sticky="NS",pady=(10, 0),padx=(0,5))


# Buttons
removeButton = tkinter.Button(buttonFrame, image=removeImage,
                              activebackground=RootBackground, borderwidth=0, bg=RootBackground,command=removeItem)
clearButton = tkinter.Button(buttonFrame, image=clearImage,
                             activebackground=RootBackground, borderwidth=0, bg=RootBackground,command=clearList)
saveButton = tkinter.Button(buttonFrame, image=saveImage,
                            activebackground=RootBackground, borderwidth=0, bg=RootBackground,command=saveList)
quitButton = tkinter.Button(buttonFrame, command=root.destroy, image=quitImage,
                            activebackground=RootBackground, borderwidth=0, bg=RootBackground)
welcomeButton = tkinter.Button(buttonFrame, image=downloadImage,
                               activebackground=RootBackground, borderwidth=0, bg=RootBackground)

removeButton.grid(row=0, column=0, padx=(20, 20), pady=3)
clearButton.grid(row=0, column=1, padx=20, pady=3)
welcomeButton.grid(row=0, column=2, padx=20, pady=3)
saveButton.grid(row=0, column=3, padx=20, pady=3)
quitButton.grid(row=0, column=4, padx=(20, 20), pady=3) 


# Hover Text
hover = tkinter.Label(root,text="",font=Font1,bd=1,anchor = 'e',bg=RootBackground)
hover.pack(fill='x',side=BOTTOM)

removeButton.bind("<Enter>",removeHoverEnterFunc)
removeButton.bind("<Leave>",HoverLeaveFunc)
clearButton.bind("<Enter>",clearHoverEnterFunc)
clearButton.bind("<Leave>",HoverLeaveFunc)
saveButton.bind("<Enter>",saveHoverEnterFunc)
saveButton.bind("<Leave>",HoverLeaveFunc)
quitButton.bind("<Enter>",exitHoverEnterFunc)
quitButton.bind("<Leave>",HoverLeaveFunc)
AddtoList.bind("<Enter>",addHoverEnterFunc)
AddtoList.bind("<Leave>",HoverLeaveFunc)
welcomeButton.bind("<Enter>",welcomeHoverEnterFunc)
welcomeButton.bind("<Leave>",HoverLeaveFunc)


# Opens previous list if available
openSaved()


# Keeps the root window open
root.mainloop()
