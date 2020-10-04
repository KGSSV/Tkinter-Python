import tkinter

# root instance
root = tkinter.Tk()

root.title('buttons')
root.geometry('500x500')
root.resizable(0, 0)

# buttons and grid systems

# so we have to understand that the smallest coordinate is taken a the origin even after that the grid system tries to consise the buttons

# creating buttons

but1 = tkinter.Button(root, text='butt1')
but1.grid(row='0', column='0')

# applying the bg
but2 = tkinter.Button(root, text='butt2', bg="#ff0000")
but2.grid(row='0', column='1', padx=(10, 0))

# activebackground changes collor to the hex code when interacted
but3 = tkinter.Button(root, text='butt3', bg="#ff0000",
                      activebackground="#0000ff")
but3.grid(row='0', column='2', padx=(10, 0))

# using columnspan and converting all 3 column to one column only for that row not for all!!!!
but4 = tkinter.Button(root, text='butt2', bg="#ff0000",
                      activebackground='lightblue')
but4.grid(row='1', column='0', columnspan=3, sticky='WE', pady=(10, 0))

# always remember (grid is only fr placement and using padding etc check termical for erroe)

# for grid use the following prop ( row , colum , padx pady , ipadx ipad y , columnspan , rowspan)
root.mainloop()