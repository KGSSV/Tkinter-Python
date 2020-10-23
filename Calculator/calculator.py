import tkinter
from tkinter import RIGHT, END, DISABLED, ACTIVE, NORMAL, IntVar

root = tkinter.Tk()

root.title('Calculator')
root.resizable(0, 0)
root.geometry('305x390')
root.iconbitmap('cal.ico')

# fonts and sizes
entry_font = ('Arial', 30)
button_font = ('Arial', 18)
bg_entry = '#d6f49d'
bg_root = '#ead637'
root_bg = '#a2d2c3'

# functions

t = IntVar


def submit(number):

    t = 1
    print(t)
    if t == 0:
        entry_field.delete(0, END)

    entry_field.insert(END, number)

    # if decimal is pressed disable it
    if '.' in entry_field.get():
        decimal_button.config(state=DISABLED)


def back():
    entry_content = entry_field.get()
    g = entry_content[:-1]

    if entry_content.endswith('.'):
        entry_content = entry_content[:-1]
        entry_field.delete(0, END)
        entry_field.insert(0, entry_content)
        decimal_button.config(state=NORMAL)
    else:
        entry_content = entry_content[:-1]
        entry_field.delete(0, END)
        entry_field.insert(0, entry_content)


def operate(operator):

    global first_numer
    global operation

    operation = operator
    first_numer = entry_field.get()

    # delete for 2nd operator
    entry_field.delete(0, END)
    # desabled
    add_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    devide_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    square_button.config(state=DISABLED)

    # return decimal to normal
    decimal_button.config(state=NORMAL)


def equal():

    if operation == 'add':
        value = float(first_numer) + float(entry_field.get())
    elif operation == 'subtract':
        value = float(first_numer) - float(entry_field.get())
    elif operation == 'multiply':
        value = float(first_numer) * float(entry_field.get())
    elif operation == 'devide':
        if entry_field.get() == '0':
            value = 'ERROR'
        else:
            value = float(first_numer) / float(entry_field.get())
    elif operation == 'exponent':
        value = float(first_numer) ** float(entry_field.get())

    entry_field.delete(0, END)
    entry_field.insert(0, value)
    decimal_button.config(state=DISABLED)

    # ENABLE ALL BUTTONS
    enable()


def enable():
    add_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    devide_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)
    square_button.config(state=NORMAL)


def clear():
    enable()
    decimal_button.config(state=NORMAL)
    entry_field.delete(0, END)


def inverse():
    if entry_field.get() == '0':
        value = 'ERROR'
    else:
        value = 1/float(entry_field.get())
    entry_field.delete(0, END)
    entry_field.insert(0, value)
    decimal_button.config(state=DISABLED)


def square():
    value = float(entry_field.get())**2
    entry_field.delete(0, END)
    entry_field.insert(0, value)


def negate():
    value = -(float(entry_field.get()))
    entry_field.delete(0, END)
    entry_field.insert(0, value)


root.config(bg=root_bg)
# frames
input_frame = tkinter.LabelFrame(root, bg=bg_entry)
button_frame = tkinter.LabelFrame(root)
input_frame.pack(padx=2, pady=(1, 20))
button_frame.pack(padx=2, pady=5)

# buttons
# entry feild
entry_field = tkinter.Entry(
    input_frame, bg=bg_entry, width=50, justify=RIGHT, font=entry_font, borderwidth=5)
entry_field.pack(padx=2, pady=2)


# outputframe
clear_button = tkinter.Button(
    button_frame,  text='Clear', font=button_font, command=clear)
quit_button = tkinter.Button(
    button_frame,  text='Quit', font=button_font, command=root.destroy)
back_space = tkinter.Button(
    button_frame, font=button_font, text='<=', command=back)

inverse_button = tkinter.Button(
    button_frame, text='1/x', font=button_font, bg='#32CD32', fg='black', command=inverse)
square_button = tkinter.Button(
    button_frame, text='x^2', font=button_font, bg='#32CD32', fg='black', command=square)
exponent_button = tkinter.Button(
    button_frame, text='x^n', font=button_font, bg='#32CD32', fg='black', command=lambda: operate('exponent'))
devide_button = tkinter.Button(
    button_frame, text='/', font=button_font, bg='#32CD32', fg='black', command=lambda: operate('devide'))
multiply_button = tkinter.Button(
    button_frame, text='x', font=button_font, bg='#32CD32', fg='black', command=lambda: operate('multiply'))
subtract_button = tkinter.Button(
    button_frame, text='-', font=button_font, bg='#32CD32', fg='black', command=lambda: operate('subtract'))
add_button = tkinter.Button(
    button_frame, text='+', font=button_font, bg='#32CD32', fg='black', command=lambda: operate('add'))
equal_button = tkinter.Button(
    button_frame, text='=', font=button_font, bg='#32CD32', fg='black', command=equal)
decimal_button = tkinter.Button(
    button_frame, text='.', font=button_font, bg='black', fg='white',  command=lambda: submit('.'))
negate_button = tkinter.Button(
    button_frame, text='+/-', font=button_font, bg='black', fg='white', command=negate)

nine_button = tkinter.Button(
    button_frame, text='9', font=button_font, bg='black', fg='white', command=lambda: submit(9))
eight_button = tkinter.Button(
    button_frame, text='8', font=button_font, bg='black', fg='white', command=lambda: submit(8))
seven_button = tkinter.Button(
    button_frame, text='7', font=button_font, bg='black', fg='white', command=lambda: submit(7))
six_button = tkinter.Button(button_frame, text='6',
                            font=button_font, bg='black', fg='white', command=lambda: submit(6))
five_button = tkinter.Button(
    button_frame, text='5', font=button_font, bg='black', fg='white', command=lambda: submit(5))
four_button = tkinter.Button(
    button_frame, text='4', font=button_font, bg='black', fg='white', command=lambda: submit(4))
three_button = tkinter.Button(
    button_frame, text='3', font=button_font, bg='black', fg='white', command=lambda: submit(3))
two_button = tkinter.Button(button_frame, text='2',
                            font=button_font, bg='black', fg='white', command=lambda: submit(2))
one_button = tkinter.Button(button_frame, text='1',
                            font=button_font, bg='black', fg='white', command=lambda: submit(1))
zero_button = tkinter.Button(
    button_frame, text='0', font=button_font, bg='black', fg='white', command=lambda: submit(0))

# first row
clear_button.grid(row=0, column=0, sticky='WE', columnspan=2)
quit_button.grid(row=0, column=2, sticky='WE')
back_space.grid(row=0, column=3, sticky='WE')
# second row
inverse_button.grid(row=1, column=0,  sticky='WE', pady=1)
square_button.grid(row=1, column=1,  sticky='WE', pady=1)
exponent_button.grid(row=1, column=2,  sticky='WE', pady=1)
devide_button.grid(row=1, column=3,  sticky='WE', pady=1)

# third row

seven_button.grid(row=2, column=0, pady=1, ipadx=20, sticky='WE')
eight_button.grid(row=2, column=1, pady=1, ipadx=20, sticky='WE')
nine_button.grid(row=2, column=2, pady=1, ipadx=20, sticky='WE')
multiply_button.grid(row=2, column=3, pady=1, ipadx=20, sticky='WE')

# fourth butotn

four_button.grid(row=3, column=0, pady=1, ipadx=20, sticky='WE')
five_button.grid(row=3, column=1, pady=1, ipadx=20, sticky='WE')
six_button.grid(row=3, column=2, pady=1, ipadx=20, sticky='WE')
subtract_button.grid(row=3, column=3, pady=1, ipadx=20, sticky='WE')

# fifth row

three_button.grid(row=4, column=0, pady=1, ipadx=20, sticky='WE')
two_button.grid(row=4, column=1, pady=1, ipadx=20, sticky='WE')
one_button.grid(row=4, column=2, pady=1, ipadx=20, sticky='WE')
add_button.grid(row=4, column=3, pady=1, ipadx=20, sticky='WE')

# sixth row
negate_button.grid(row=5, column=0,  sticky='WE', pady=1)
zero_button.grid(row=5, column=1,  sticky='WE', pady=1)
decimal_button.grid(row=5, column=2,  sticky='WE', pady=1)
equal_button.grid(row=5, column=3,  sticky='WE', pady=1)


# run the windows loop
root.mainloop()
