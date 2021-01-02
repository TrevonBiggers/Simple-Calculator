from tkinter import *
import tkinter as tk
# Used to define what happens when button is clicked. Lambda function is used to pass in parameter from function
# add more info on how function works

"""Simple calculator using Tkinter.
It works by passing a number through to a function via the lambda command, the number is than
converted to a string and input into the entry bar. 
The out put is converted back into a float just in case decimal values are used.
The calculator will add, multiply, divide and subtract. It will also calculate 1/x value, square root and an exponent of 2.
It can also store a number via the memory buttons. Memory buttons will activate when a number is stored and deactivate 
when it is cleared. It has backspace functionality, percentage value and clear entry buttons. Will also append decimal value and
change output from negative to positive via the +/- button.

KNOWN BUGS:
-Can't do calculation with decimal if it is the second number used
-Issues with memory buttons appearing and reappearing, don't know to regenerate bug yet

ADDITIONAL FEATURES WOULD LIKE TO ADD:
-Start calculator with 0 in entry bar
-When decimal is selected do not show decimal input until after another number is selected
-A bar at the top that shows what calculation your doing

Notes taken from Tkinter gui tutorial from https://www.youtube.com/watch?v=oq3lJdhnPp8

Questions/Notes to SELF:
When can I and cannot call global variable, and in what scope can i call it in
When and how to call a function with arguments in another function
"""

# takes parameter from clicked button and passes it to this function
# variable that reads in entry box
# deletes whats in entry box after saving it to variable to insert it again later, deletes whats in entry box so there
# are no duplicate numbers
def button_click(number):
    global current
    current = outPut.get()
    outPut.delete(0, END)
    outPut.insert(0, str(current) + str(number))
    noMoreZeros()

# function is used to so user can't input multiple zeroes into entery bar also may cause errors with other inputs
def noMoreZeros():
    x = outPut.get()
    if x[0] == "0":
        outPut.delete(0, END)

# generates buttons from labels when the user clicks memory store
def generate_buttons():
    global memClear1
    memClear1 = tk.Button(botFrame, text="MC", bg='gray60', fg='white', font=(None, 16), command=button_memClear)
    memClear1.place(relx=0, rely=0, relwidth=.2, relheight=.0875)
    global memRecall1
    memRecall1 = tk.Button(botFrame, text="MR", bg='gray60', fg='white', font=(None, 16), command=button_memRecall)
    memRecall1.place(relx=.2, rely=0, relwidth=.2, relheight=.0875)
    global memSub1
    memSub1 = tk.Button(botFrame, text="M-", bg='gray60', fg='white', font=(None, 16), command=button_memMinus)
    memSub1.place(relx=.6, rely=0, relwidth=.2, relheight=.0875)
    global memAdd1
    memAdd1 = tk.Button(botFrame, text="M+", bg='gray60', fg='white', font=(None, 16), command=button_memAdd)
    memAdd1.place(relx=.4, rely=0, relwidth=.2, relheight=.0875)


# clears most recent entry and variable from first entry
def button_clear():
   global f_num
   f_num = None
   outPut.delete(0, END)


# clears most recent entry
def button_clearEntry():
    outPut.delete(0, END)


# deletes by slicing the string starting from the last index in the output
# inserts a new string from index 0 up to the index specified in backspace
def button_backspace():
    backspace = outPut.get()
    backspace = backspace[:-1:]
    outPut.delete(0, END)
    outPut.insert(0, backspace)


# adds current entry number to memory variable
def button_memAdd():
    output_number = outPut.get()
    global memory
    memory = float(output_number) + float(memory)


# subtracts current entry number to memory variable
def button_memMinus():
    output_number = outPut.get()
    global memory
    memory = float(output_number) - float(memory)


# stores number to memory to use again later than produces buttons from function
def button_memStore():
    global memory
    memory = outPut.get()
    generate_buttons()

# restores number from memory variable
def button_memRecall():
    outPut.delete(0, END)
    outPut.insert(0, str(memory))

# clears memory variable and also disables buttons that were created
def button_memClear():
    global memory
    memory = ""
    memClear1.destroy()
    memRecall1.destroy()
    memSub1.destroy()
    memAdd1.destroy()

#
def button_add():
    first_number = outPut.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    outPut.delete(0, END)

def button_subtract():
    first_number = outPut.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    outPut.delete(0, END)


def button_multiply():
    first_number = outPut.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    outPut.delete(0, END)


def button_divide():
    first_number = outPut.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    outPut.delete(0, END)


def button_exponent():
    first_number = outPut.get()
    global f_num
    f_num = float(first_number)
    outPut.delete(0, END)
    outPut.insert(0, f_num*f_num)
    clear_zero()


def button_oneOverEx():
    first_number = outPut.get()
    global f_num
    f_num = float(first_number)
    outPut.delete(0, END)
    outPut.insert(0, 1 / f_num)
    clear_zero()


def button_plusMinus():
    first_number = outPut.get()
    global f_num
    f_num = float(first_number)
    outPut.delete(0, END)
    outPut.insert(0, f_num * (-1))


def square_root():
    first_number = outPut.get()
    global f_num
    f_num = float(first_number)
    x = f_num ** (1/2)
    outPut.delete(0, END)
    outPut.insert(0, x)
    clear_zero()


def button_Percentage():
    first_number = outPut.get()
    global f_num
    f_num = float(first_number)
    outPut.delete(0, END)
    outPut.insert(0, f_num / 100)


# inserts decimal after entry, if decimal is already selected, the function will replace with whatever is currently stored
# to prevent multiple entries of decimals within the entry box
def button_decimal():
    first_number = outPut.get()
    global f_num
    f_num = (first_number + ".")
    outPut.delete(0, END)
    outPut.insert(0, f_num)
    if "." in first_number:
        outPut.delete(0, END)
        outPut.insert(0, first_number)


# takes first number that was input and second number and combines them based on whats stored within the math variable
def button_equal():
    second_number = outPut.get()
    outPut.delete(0, END)

    if math == "addition":
        outPut.insert(0, f_num + float(second_number))

    if math == "subtraction":
        outPut.insert(0, f_num - float(second_number))

    if math == "multiplication":
        outPut.insert(0, f_num * float(second_number))

    if math == "division":
        outPut.insert(0, f_num / float(second_number))

    clear_zero()


# gets rid of .0 that occurs at end of an answer because the values are converted to floats,
# makes the answer look like a normal int value with this function
def clear_zero():
    x = outPut.get()
    a = x[-1]
    b = x[-2]

    if a == "0" and b == ".":
        x = x[:-2:]
        outPut.delete(0, END)
        outPut.insert(0, x)


# Setting Height and width of window
HEIGHT = 500
WIDTH = 400

root = tk.Tk()
# Title of App located in top left corner of window
root.title("Simple Calculator")

# main window, height and width specified in variables above
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# frame within the canvas used for output
outPutFrame = tk.Frame(root, bg='gray', bd=5)
outPutFrame.place(rely=.05, relwidth=1, relheight=0.10)

# frame used for calculator buttons
botFrame = tk.Frame(root, bg='linen', bd=5)  # frame at bottom
botFrame.place(rely=.15, relwidth=1, relheight=1)

calculation = Label(root, font="Helvetica 12", bg='black', fg='white', anchor="e")
calculation.place(rely=0, relx=0, relwidth=1, relheight=.05)

# Output box of calculator
outPut = Entry(outPutFrame, font="Helvetica 24", justify="right")
outPut.place(relx=0, rely=0, relwidth=1, relheight=1)

# Clears memory of stored integer
memClear = Label(botFrame, text="MC", bg='gray60', fg='white', font=(None, 16))
memClear.place(relx=0, rely=0, relwidth=.2, relheight=.0875)

# Recalls stored integer into entry box
memRecall = Label(botFrame, text="MR", bg='gray60', fg='white', font=(None, 16))
memRecall.place(relx=.2, rely=0, relwidth=.2, relheight=.0875)

# Adds to current stored integer
memAdd = Label(botFrame, text="M+", bg='gray60', fg='white', font=(None, 16))
memAdd.place(relx=.4, rely=0, relwidth=.2, relheight=.0875)

# Memory Minus button
memSub = Label(botFrame, text="M-", bg='gray60', fg='white', font=(None, 16))
memSub.place(relx=.6, rely=0, relwidth=.2, relheight=.0875)

# Memory Store button
memStore = tk.Button(botFrame, text="MS", bg='gray60', fg='white', font=(None, 16), command=button_memStore)
memStore.place(relx=.8, rely=0, relwidth=.2, relheight=.0875)

# Percent button
percent = tk.Button(botFrame, text="%", bg='gray35', fg='white', font=(None, 16), command=button_Percentage)
percent.place(relx=0, rely=.0875, relwidth=.25, relheight=.1275)

# Clear Entry button, clears current entry
clearEntry = tk.Button(botFrame, text="CE", bg='gray35', fg='white', font=(None, 16), command=button_clearEntry)
clearEntry.place(relx=.25, rely=.0875, relwidth=.25, relheight=.1275)

# Clear button, clears current entry and equation
clear = tk.Button(botFrame, text="C", bg='gray35', fg='white', font=(None, 16), command=button_clear)
clear.place(relx=.50, rely=.0875, relwidth=.25, relheight=.1275)

# Backspace button
backSpace = tk.Button(botFrame, text="<", bg='gray35', fg='white', font=(None, 16),command=button_backspace)
backSpace.place(relx=.75, rely=.0875, relwidth=.25, relheight=.1275)

# 1 divided by output button
oneDivdedbyChosenValue = tk.Button(botFrame, text="1/x", bg='gray35', fg='white', font=(None, 16), command=button_oneOverEx)
oneDivdedbyChosenValue.place(relx=0, rely=.215, relwidth=.25, relheight=.1275)

# Multiplies output by itself
exponential = tk.Button(botFrame, text="x\u00b2", bg='gray35', fg='white', font=(None, 16), command=button_exponent)
exponential.place(relx=.25, rely=.215, relwidth=.25, relheight=.1275)

# Square root button
square = tk.Button(botFrame, text="\u00b2\u221Ax", bg='gray35', fg='white', font=(None, 16), command=square_root)
square.place(relx=.50, rely=.215, relwidth=.25, relheight=.1275)

# Divide button
divideButton = tk.Button(botFrame, text="\u00f7", bg='gray35', fg='white', font=(None, 20), command=button_divide)
divideButton.place(relx=.75, rely=.215, relwidth=.25, relheight=.1275)

# Number Seven button
numberSeven = tk.Button(botFrame, text="7", bg='gray10', fg='white', font=(None, 16), command=lambda: button_click(7))
numberSeven.place(relx=0, rely=.3425, relwidth=.25, relheight=.1275)

# Number Eight button
numberEight = tk.Button(botFrame, text="8", bg='gray10', fg='white', font=(None, 16), command=lambda: button_click(8))
numberEight.place(relx=0.25, rely=.3425, relwidth=.25, relheight=.1275)

# Number nine button
numberNine = tk.Button(botFrame, text="9", bg='gray10', fg='white', font=(None, 16), command=lambda: button_click(9))
numberNine.place(relx=0.50, rely=.3425, relwidth=.25, relheight=.1275)

# Multiply Button
multiplyButton = tk.Button(botFrame, text="\u00d7", bg='gray35', fg='white', font=(None, 20), command=button_multiply)
multiplyButton.place(relx=.75, rely=.3425, relwidth=.25, relheight=.1275)

# Number Four button
numberFour = tk.Button(botFrame, text="4", bg='gray10', fg='white', font=(None, 16), command=lambda: button_click(4))
numberFour.place(relx=0, rely=.47, relwidth=.25, relheight=.1275)

# Number Five button
numberFive = tk.Button(botFrame, text="5", bg='gray10', fg='white', font=(None, 16), command=lambda: button_click(5))
numberFive.place(relx=.25, rely=.47, relwidth=.25, relheight=.1275)

# Number Six button
numberSix = tk.Button(botFrame, text="6", bg='gray10', fg='white', font=(None, 16), command=lambda: button_click(6))
numberSix.place(relx=.50, rely=.47, relwidth=.25, relheight=.1275)

# Subtraction button
subtractButton = tk.Button(botFrame, text="-", bg='gray35', fg='white', font=(None, 20), command=button_subtract)
subtractButton.place(relx=.75, rely=.47, relwidth=.25, relheight=.1275)

# Number one button
numberOne = tk.Button(botFrame, text="1", bg='gray10', fg='white', font=(None, 16), command=lambda: button_click(1))
numberOne.place(relx=0, rely=.5975, relwidth=.25, relheight=.1275)

# Number two button
numberTwo = tk.Button(botFrame, text="2", bg='gray10', fg='white', font=(None, 16), command=lambda: button_click(2))
numberTwo.place(relx=.25, rely=.5975, relwidth=.25, relheight=.1275)

# Number Three button
numberThree = tk.Button(botFrame, text="3", bg='gray10', fg='white', font=(None, 16), command=lambda: button_click(3))
numberThree.place(relx=.50, rely=.5975, relwidth=.25, relheight=.1275)

# Addition Button
plusButton = tk.Button(botFrame, text="+", bg='gray35', fg='white', font=(None, 20), command=button_add)
plusButton.place(relx=.75, rely=.5975, relwidth=.25, relheight=.1275)

# PlusMinus button
negativePlusButton = tk.Button(botFrame, text="+/-", bg='gray10', fg='white', font=(None, 16), command=button_plusMinus)
negativePlusButton.place(relx=0, rely=.725, relwidth=.25, relheight=.1275)

# Zero button
numberZero = tk.Button(botFrame, text="0", bg='gray10', fg='white', font=(None, 16), command=lambda: button_click(0))
numberZero.place(relx=.25, rely=.725, relwidth=.25, relheight=.1275)

# Decimal Button
decimalButton = tk.Button(botFrame, text=".", bg='gray10', fg='white', font=(None, 20), command=button_decimal)
decimalButton.place(relx=.50, rely=.725, relwidth=.25, relheight=.1275)

# Equals button, output button
equalSign = tk.Button(botFrame, text="=", bg='royalblue3', fg='white', font=(None, 16), command=button_equal)
equalSign.place(relx=.75, rely=.725, relwidth=.25, relheight=.1275)

root.mainloop()
