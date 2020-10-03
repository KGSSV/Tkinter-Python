# import tkinter lib comes with basic package of python
import tkinter

# creating instance
root = tkinter.Tk()
# title naming
root.title("akhil")
# changing icon form generic tkinter
root.iconbitmap('tel.ico')
# chaging dimentions
root.geometry('650x400')

# to open a separate window
top = tkinter.Toplevel()
# use top as we used root to configure root window (main window)
# all function which worked with root will also work with top

# to allow extention of window size
# takes 2 bool values 1,0  (1,0) says extention to x allowed but y not allowed
top.resizable(0, 0)
# the above cmd does not allow entending root winidow at all so maximise button will be disabled

# changing dimentions with placement where to open (def is to pixels)
top.geometry('200x200+500+500')

# to change background of root or top window
top.config(bg='blue')

# using the main gaint loop to run the application
root.mainloop()
