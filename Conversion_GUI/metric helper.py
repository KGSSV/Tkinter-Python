import tkinter
from tkinter import ttk, END
from PIL import ImageTk, Image

# create window
root = tkinter.Tk()
root.title('Conversion Helper')
root.iconbitmap('scale.ico')
# dont specify the geometry based on widgets tkinter decides how space is to be taken make it as small as possible

# functions


def convert():
    '''Converstion defnition'''
    # define dict (key = value pair)
    formula = {
        'Femto': 10**-15,
        'Pico': 10**-12,
        'Nano': 10**-9,
        'Micro': 10**-6,
        'Milli': 10**-3,
        'Centi': 10**-2,
        'Deci': 10**-1,
        'Base Value': 10**0,
        'Deca': 10**1,
        'Hecto': 10**2,
        'Kilo': 10**3,
        'Mega': 10**6,
        'Giga': 10**9,
        'Tera': 10**12,
        'Peta': 10**15,
    }
    output_field.delete(0, END)

    inputstuff = ip_combobox.get()
    outputstuff = op_combobox.get()
    inputvalue = float(input_field.get())

    basevalue = inputvalue * formula[inputstuff]
    endvalue = basevalue / formula[outputstuff]
    output_field.insert(0, str(endvalue))


def clear():
    output_field.delete(0, END)
    input_field.delete(0, END)
    ip_combobox.set('Base Value')
    op_combobox.set('Base Value')


#fonts and colors
bg_color = '#fbac16'
root.config(bg=bg_color)

# header
header = tkinter.Label(root, text="Conversion Helper ",
                       bg=bg_color)
header.config(font=("", 15))
header.grid(columnspan=2)

image = ImageTk.PhotoImage(Image.open('Refresh.png'))
but_image = tkinter.Button(
    root, image=image, bg=bg_color, activebackground=bg_color, borderwidth=0, command=clear)
but_image.grid(row=0, column=2, sticky='e')

# layout

input_field = tkinter.Entry(root, width=20, borderwidth=3)
eq_label = tkinter.Label(root, text='=', bg=bg_color,)
output_field = tkinter.Entry(root, width=20, borderwidth=3)

input_field.grid(row=1, column=0, padx=20, pady=10)
eq_label.grid(row=1, column=1)
output_field.grid(row=1, column=2, padx=20, pady=10)

# to ging in well formed widgets import ttk( mordern looking widgets)
# make list
list_contents = ['Femto', 'Pico', 'Nano', 'Micro', 'Milli', 'Centi', 'Deci',
                 'Base Value', 'Deca', 'Hecto', 'Kilo', 'Mega', 'Giga', 'Tera', 'Peta']
ip_combobox = ttk.Combobox(root, value=list_contents, justify='center')
op_combobox = ttk.Combobox(root, value=list_contents, justify='center')

ip_combobox.grid(row=2, column=0, padx=10, pady=10)
tkinter.Label(root, text='To', bg=bg_color).grid(row=2, column=1)
op_combobox.grid(row=2, column=2, padx=10, pady=10)

ip_combobox.set('Base Value')
op_combobox.set('Base Value')
# submit button
but = tkinter.Button(root, text='Submit', width=20,
                     command=convert, bg="Green", activebackground='Grey')
but.grid(
    row=3, column=0, columnspan=3, padx=10, pady=10)
# run the window mainloop

root.mainloop()
