import tkinter 

# Part 1 (Main Window)
# Main Container Window
root = tkinter.Tk() 
# Top Bar Title       
root.title('Basics')
# Icon Image Path
root.iconbitmap('F:/Coding Practice/Visual Studio Code/Python/TkinterEnv/Codes/Basics/Images/Icon/CalcIcon.ico')
# Dimension of the Container Window
root.geometry('350x400')
# Restriction on Resizing
root.resizable(0,0)
# Configuration of the Window (bg - Background)
root.config(bg = '#ffcdd2')



# Part 2 (Second Window)
# Container for Secondary Window
top = tkinter.Toplevel()
# Title
top.title("Second Window")
# Configuration of Second Window
top.config(bg = "#ffee58")
# Dimensions ("width x height + xpadding(left) + ypadding(top)")
top.geometry("200x200+50+50")



# Part 3 (Widget Creation)
# Label Widget
Name_Label_1 = tkinter.Label(root,text='This is Hariesh Varshan')
Name_Label_1.pack()

Name_Label_2 = tkinter.Label(root,text="Coimbatore Institute of Technology",fg = "Black",font=("Arial",12,'bold'))
Name_Label_2.pack(padx = 10 , pady = 20)

Name_Label_3 = tkinter.Label(root,bg = "#cb9ca2",fg = "White",text = "Sum",font = ('Aarkvald Bold',12))
Name_Label_3.pack(ipady = 40,ipadx = 170,padx = 10,pady = 10)

Name_Label_4 = tkinter.Label(root,text="Learning Tkinter",fg = '#b968c7',bg = '#890e4f',font=("Cambria",14))
Name_Label_4.pack(fill = 'x')

Name_Label_5 = tkinter.Label(top,text="Learning is Fun",bg = "#bbdefa",fg="#009788",font = ("Cambria",14))
Name_Label_5.pack(fill = 'both',expand = "True")
 

# Final Part
# To keep the window open
root.mainloop()