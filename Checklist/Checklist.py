import tkinter
from tkinter import END, ANCHOR

# root
root = tkinter.Tk()
root.title('Checklist')
root.iconbitmap('checklist.ico')
root.geometry('402x402')
root.resizable(0, 0)

#fonts and colors
my_font = ('Times New Roman', 12)
bg_color = '#3581B8'
button_color = '#CCCCCC'

root.config(bg=bg_color)

# functions


def additem():
    '''add items'''
    listbox.insert(END, list_entry.get())
    list_entry.delete(0, END)


def remove():
    listbox.delete(0, END)
    save_list()


def remove_item():
    listbox.delete(ANCHOR)


def save_list():
    '''save the list in some txt and read it back when opening'''
    list_tuple = listbox.get(0, END)
    with open('Temp.text', 'w') as f:

        for item in list_tuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item + '\n')


def open_list():
    try:
        with open('Temp.text', 'r') as f:
            for item in f:
                listbox.insert(END, item)
    except:
        return


# input frame
input_frame = tkinter.Frame(root, bg=bg_color)
output_frame = tkinter.Frame(root, bg=bg_color)
button_frame = tkinter.Frame(root, bg=bg_color)
input_frame.pack()
output_frame.pack()
button_frame.pack()

# adding widgets to input frame
list_entry = tkinter.Entry(input_frame, width=50,
                           borderwidth=3)

add_but = tkinter.Button(input_frame, text='Add Item',
                         bg=button_color, command=additem)
list_entry.grid(row=0, column=0, padx=10, pady=10)
add_but.grid(row=0, column=1, padx=(0, 10), pady=10, ipadx=5)

# adding widgets to output frame

scrollbar = tkinter.Scrollbar(output_frame)
scrollbar.grid(row=0, column=1, sticky='NS', pady=(0, 10))
listbox = tkinter.Listbox(output_frame, height='19',
                          width='58', yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.grid(row=0, column=0, pady=(0, 10))

# button widgets
removeitem = tkinter.Button(
    button_frame, text='Remove Item', command=remove_item)
clearlist = tkinter.Button(button_frame, text='ClearList', command=remove)
save = tkinter.Button(button_frame, text='Save', command=save_list)
quit_button = tkinter.Button(button_frame, command=root.destroy, text='Quit')
removeitem.grid(row=0, column=0, padx=5, pady=(
    0, 10), ipadx=10, ipady=2, sticky='NS')
clearlist.grid(row=0, column=1, padx=5, pady=(
    0, 10), ipadx=12, ipady=2, sticky='NS')
save.grid(row=0, column=2, padx=5, pady=(
    0, 10), ipadx=20, ipady=2, sticky='NS')
quit_button.grid(row=0, column=3, padx=5, pady=(
    0, 10), ipadx=25, ipady=2, sticky='NS')


open_list()
# run the windows main loop
root.mainloop()
