# hello gui world
import tkinter
from tkinter import StringVar, BOTH, END, DISABLED, NORMAL
from PIL import ImageTk, Image

# define root window
root = tkinter.Tk()
root.iconbitmap('icon.ico')
root.resizable(0, 0)
root.geometry('500x500')
root.title('Hello World')

# input color frames
input_color = '#9684A1'
root_color = '#C1EDCC'
output_color = '#EDB230'

root.config(bg=root_color)

# define the functions


def printname():
    '''to enter text in output feild()'''
    if style.get() == 'lower':
        print_stuff = tkinter.Label(output_frame, text=(
            'Hello ' + name_field.get()).lower(), bg=output_color)
    elif style.get() == 'upper':
        print_stuff = tkinter.Label(output_frame, text=(
            'Hello ' + name_field.get()).upper(), bg=output_color)
    else:
        print_stuff = tkinter.Label(
            output_frame, text='Hello ' + name_field.get(), bg=output_color)
    name_field.delete(0, END)
    print_stuff.pack()


# define frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.Frame(root, bg=output_color)
input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=(0, 10), fill=BOTH, expand=True)

# add widgets
name_field = tkinter.Entry(input_frame, width=20)
name_field.insert(0, "Enter Name")
name_field.configure(state=DISABLED)


def on_click(event):
    name_field.configure(state=NORMAL)
    name_field.delete(0, END)


on_click_id = name_field.bind('<Button-1>', on_click)
submit = tkinter.Button(input_frame, text='Submit!!', command=printname)
name_field.grid(row=0, column=0, columnspan=2, padx=10, pady=10, ipadx=10)
submit.grid(row=0, column=2, padx=10, ipadx=10)

# define radio button
style = StringVar()
style.set('lower')
radiobut1 = tkinter.Radiobutton(
    input_frame, text='Lower Case', variable=style, value='lower', bg=input_color)
radiobut2 = tkinter.Radiobutton(
    input_frame, text='Upper Case', variable=style, value='upper', bg=input_color)
radiobut3 = tkinter.Radiobutton(
    input_frame, text='Normal Case', variable=style, value='normal', bg=input_color)

radiobut1.grid(row=1, column=0)
radiobut2.grid(row=1, column=1)
radiobut3.grid(row=1, column=2)

# output frame
image = ImageTk.PhotoImage(Image.open('flower.png'))
image_label = tkinter.Label(
    output_frame, image=image, bg=output_color)
image_label.pack(pady=5)

# run the window loop
root.mainloop()
