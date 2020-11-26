import tkinter
from tkinter import StringVar, ttk, END


# Functions
def ConvertFunc():
    MetricDict = {
        "femto": 10**-15,
        "pico": 10**-12,
        "nano": 10**-9,
        "micro": 10**-6,
        "milli": 10**-3,
        "centi": 10**-2,
        "deci": 10**-1,
        "base value": 10**0,
        "deca": 10**1,
        "hecto": 10**2,
        "kilo": 10**3,
        "mega": 10**6,
        "giga": 10**9,
        "tera": 10**12,
        "peta": 10**15
    }

    # Clear the Output and Input Entry Fields
    # Input.delete(0,END)
    Output.delete(0, END)

    # Getting the entered values
    InputGet = float(Input.get())
    InputComboGet = InputComboBox.get()
    OutputComboGet = OutputComboBox.get()

    # Conversion Logic
    BaseValue = InputGet * MetricDict[InputComboGet]
    EndValue = BaseValue / MetricDict[OutputComboGet]

    # Update the Output Text Bxox Widget
    Output.insert(0, str(EndValue))


# Fonts and Colours
RootBackground = "#6930C3"
WidgetColour = "#CC1B2F"
MyFont = ("Cambria", 10)


# Root Container
root = tkinter.Tk()
root.title(string="Metric Converter")
root.iconbitmap("Codes/Metric Converter/Images/MathIcon.ico")
# root.geometry("342x150")
root.resizable(width=0, height=0)
root.config(bg=RootBackground)


# Input and Output Entry Fields
Input = tkinter.Entry(root, width=20, font=MyFont,
                      bg=WidgetColour, fg="White", borderwidth=3)
Output = tkinter.Entry(root, width=20, font=MyFont,
                       bg=WidgetColour, fg="White", borderwidth=3)
Input.grid(row=0, column=0, padx=10, pady=10)
Output.grid(row=0, column=2, padx=10, pady=10)
Input.insert(0, "Enter Value")   # Initial Wordings


# Drop Down Box (Much Older One)
# MetricList = ["femto", "pico", "nano", "micro", "milli", "centi", "deci",
#              "base value", "deca", "hecto", "kilo", "mega", "giga", "tera", "peta"]
#InputChoice = StringVar()
#OutputChoice = StringVar()
#InputDropDown = tkinter.OptionMenu(root,InputChoice,*MetricList)
#OutputDropDown = tkinter.OptionMenu(root,OutputChoice,*MetricList)
# InputDropDown.grid(row=1,column=0)
# OutputDropDown.grid(row=1,column=2)
#InputChoice.set("base value")
#OutputChoice.set("base value")


# ComboBox (A Little Bit Modern)
MetricList = ["femto", "pico", "nano", "micro", "milli", "centi", "deci",
              "base value", "deca", "hecto", "kilo", "mega", "giga", "tera", "peta"]
InputComboBox = ttk.Combobox(
    root, value=MetricList, width=15, font=MyFont, justify="center")
OutputComboBox = ttk.Combobox(
    root, value=MetricList, width=15, font=MyFont, justify="center")
InputComboBox.grid(row=1, column=0, padx=5)
OutputComboBox.grid(row=1, column=2, padx=5)
InputComboBox.set("base value")
OutputComboBox.set("base value")


# Images
ConvertImage = tkinter.PhotoImage(
    file="Codes/Metric Converter/Images/ConvertButton.png")
EqualToImage = tkinter.PhotoImage(
    file="Codes/Metric Converter/Images/EqualTo.png")
ToImage = tkinter.PhotoImage(file="Codes/Metric Converter/Images/To.png")


# Label Widgets
EqualTo = tkinter.Label(root, image=EqualToImage,
                        bg=RootBackground, fg="White")
EqualTo.grid(row=0, column=1)
To = tkinter.Label(root, image=ToImage, bg=RootBackground, fg="White")
To.grid(row=1, column=1, ipadx=10)


# Button Widget
Convert = tkinter.Button(root, image=ConvertImage, bg=RootBackground,
                         activebackground=RootBackground, borderwidth=0, command=ConvertFunc)
Convert.grid(row=2, column=1, padx=10, pady=(10, 10))


# Run the root window's main loop
root.mainloop()
