import tkinter
from tkinter import END

root = tkinter.Tk()
root.title('Basics!!')

root.geometry('500x500')


# defineing functions


def out_text():
    text = tkinter.Label(out_frame, text=inp.get(), bg='lightpink')

    text.pack()
    inp.delete(0, len(inp.get()))


def count(number):
    global value   # referenes global value
    text1 = tkinter.Label(out_frame, text=number, bg='lightpink')
    text1.pack()
    value = number + 1


# defining frames
input_frame = tkinter.Frame(root, width='480', height='100', bg='lightblue')
input_frame.pack(padx='10', pady='10')

out_frame = tkinter.Frame(root, width='480', height='400', bg='lightpink')
out_frame.pack(padx='10', pady=(0, 10))
out_frame.pack_propagate(0)

# now have a input box placed in input frame
inp = tkinter.Entry(input_frame, width=40)
inp.grid(row='0', column='0', padx='10', pady='10')

but1 = tkinter.Button(input_frame, padx='25',
                      text='output', command=out_text)
but1.grid(row=0, column=1)


# propagate function to not to resize the frame
input_frame.grid_propagate(0)

# if we want to pass arg then we have use lambdas normal function cannot pass arg
value = 0
but2 = tkinter.Button(input_frame, text='count!!',
                      command=lambda: count(value))
but2.grid(row=1, column=0, columnspan=2, sticky='we')

root.mainloop()
