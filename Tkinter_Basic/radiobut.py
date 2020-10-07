import tkinter
from tkinter import IntVar


root = tkinter.Tk()
root.iconbitmap('tel.ico')
root.title('radio button!!')
root.geometry('450x450')
root.resizable(0, 0)

# define frames
input_frame = tkinter.LabelFrame(
    root, text='Radio Inputs', bg='lightblue', width=500, height=150)
output_frame = tkinter.Frame(root, bg='grey', width=500, height=340)
input_frame.pack(padx=10, pady=10,)
output_frame.pack(padx=10, pady=(0, 10))

input_frame.grid_propagate(0)
output_frame.pack_propagate(0)

# define funciton to print


def printit():
    global value
    if value.get() == 1:
        text = tkinter.Label(
            output_frame, text='selected 1st radio button with value 1', bg='grey')
        text.pack()

    elif value.get() == 2:
        text1 = tkinter.Label(
            output_frame, text='selected 2nd radio button with value 2', bg='grey')
        text1.pack()


# define intvar
value = IntVar()
value.set(1)

# defining radio button to link the radio button add the same variable
rad1 = tkinter.Radiobutton(
    input_frame, text='print 1 into output_frame', variable=value, value=1, bg='lightblue')
rad2 = tkinter.Radiobutton(
    input_frame, text='print 2 into output_frame', variable=value, value=2, bg='lightblue')
rad1.grid(row=0, column=0, padx=35, pady=10)
rad2.grid(row=0, column=1, padx=(0, 35), pady=10)

but = tkinter.Button(input_frame, text='Print!!', command=printit)
but.grid(row=1, columnspan=2)


# loop it
root.mainloop()
