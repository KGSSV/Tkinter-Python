import tkinter

# init the root instance
root = tkinter.Tk()

root.resizable(0, 0)
root.geometry('500x500')

# noted - read it
# when we init the root as a whole only one layout manager works(gird or pack or ..... etc)
# this could be troublesome but when we segment the root window in some parts in each of the following parts we  can use own grid manager

frame1 = tkinter.Frame(root, bg='lightblue')
frame2 = tkinter.Frame(root, bg='pink')
frame3 = tkinter.LabelFrame(
    root, bg='grey', text='lets have some fun',)

# packing the stuff - segments are created but still not placed onto root so pack it
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True, padx=10, pady=10)

# adding widgets with diffrent layout manager in diff rent frames

# used frame1 instead of root as we want to place where . we want to place in frame 1
lab1 = tkinter.Label(frame1, text=' hello i am using pack()')
lab1.pack()

# used frame2 instead of root as we want to place where . we want to place in frame 2
lab2 = tkinter.Label(frame2, text=' hello i am using grid()')
lab3 = tkinter.Label(frame2, text=' hello i am using pack()')

lab2.grid(row=1, column=1)
lab3.grid(row=2, column=2)

# used frame3 instead of root as we want to place where . we want to place in frame 3
lab4 = tkinter.Label(frame3, text=' hello i am using pack()')
lab4.pack()

# hence achived of using multiple layout managers in one sngle root window

# run the loop
root.mainloop()
