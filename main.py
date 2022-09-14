from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('1200x700')
root.title('Inter Converter')

# Variables
number = IntVar()
binary_number = StringVar()
octal_number = StringVar()
hexadecimal_number = StringVar()


# Functions
# enter() function will press the Enter button to convert once the user input a decimal number (base-10)
def enter():
    num = number.get()

    bi = bin(num)
    bi = bi[2:]
    binary_number.set(bi)

    oc = oct(num)
    oc = oc[2:]
    octal_number.set(oc)

    he = hex(num)
    he = he[2:]
    hexadecimal_number.set(he)


# clear() function will press the Clear button to clear the entry
def clear():
    number.set(0)
    binary_number.set('')
    octal_number.set('')
    hexadecimal_number.set('')


# exitGUI() function will press the Exit button and have a popup to ask if you want to exit or not
def exitGUI():
    ch = messagebox.askyesno('Alert', 'Are you sure to exit?')
    if ch > 0:
        root.destroy()


# Label and text for number (base-10)
lblNumber = Label(root, text='Number', font='arial 25 bold', bg='green', fg='white')
lblNumber.grid(row=0, column=0, padx=100, pady=10)
txtNumber = Entry(root, width=30, bd=5, textvariable=number)
txtNumber.grid(row=0, column=1, padx=10, pady=10)

# Label and text for binary number (base-2)
lblBinary = Label(root, text='Binary Number', font='arial 25 bold', bg='green', fg='white')
lblBinary.grid(row=2, column=0, padx=100, pady=10)
txtBinary = Entry(root, width=30, bd=5, textvariable=binary_number)
txtBinary.grid(row=2, column=1, padx=10, pady=10)

# Label and text for octal number (base-8)
lblOctal = Label(root, text='Octal Number', font='arial 25 bold', bg='green', fg='white')
lblOctal.grid(row=4, column=0, padx=100, pady=10)
txtOctal = Entry(root, width=30, bd=5, textvariable=octal_number)
txtOctal.grid(row=4, column=1, padx=10, pady=10)

# Label and text for hexadecimal number (base-16)
lblHexadecimal = Label(root, text='Hexadecimal Number', font='arial 25 bold', bg='green', fg='white')
lblHexadecimal.grid(row=6, column=0, padx=100, pady=10)
txtHexadecimal = Entry(root, width=30, bd=5, textvariable=hexadecimal_number)
txtHexadecimal.grid(row=6, column=1, padx=10, pady=10)

# Buttons
btnEnter = Button(root, text=' Enter ', font='arial 20 bold', fg='blue', bg='gray', command=enter)
btnEnter.grid(row=10, column=1, padx=10, pady=10)

btnClear = Button(root, text=' Clear ', font='arial 20 bold', fg='blue', bg='gray', command=clear)
btnClear.grid(row=14, column=1, padx=10, pady=10)

btnExit = Button(root, text=' Exit ', font='arial 20 bold', fg='blue', bg='gray', command=exitGUI)
btnExit.grid(row=14, column=2, padx=10, pady=10)

root.mainloop()
