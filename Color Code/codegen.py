import tkinter
import random
from tkinter import BOTH, IntVar, DISABLED, filedialog

root = tkinter.Tk()
root.geometry('450x500')
root.resizable(0, 0)
root.title('Color Code Gen')
root.iconbitmap('colorgen.ico')

# fonts useing system def

# functions


def getred(slider_value):
    '''gets the value from slider red  and runs in real time when ever there is any change in value of red'''
    global red_value

    # turn the slider to int as when passed it wiwll be in str
    red_value = hex(int(slider_value))
    # gets with 0x strip that 0x
    red_value = red_value.lstrip('0x')
    while len(red_value) < 2:
        red_value = '0' + red_value
    update_color()


def getgreen(slider_value):
    '''gets the value from slider red  and runs in real time when ever there is any change in value of red'''
    global green_value

    # turn the slider to int as when passed it wiwll be in str
    green_value = hex(int(slider_value))
    # gets with 0x strip that 0x
    green_value = green_value.lstrip('0x')
    while len(green_value) < 2:
        green_value = '0' + green_value
    update_color()


def getblue(slider_value):
    '''gets the value from slider red  and runs in real time when ever there is any change in value of red'''
    global blue_value

    # turn the slider to int as when passed it wiwll be in str
    blue_value = hex(int(slider_value))
    # gets with 0x strip that 0x
    blue_value = blue_value.lstrip('0x')
    while len(blue_value) < 2:
        blue_value = '0' + blue_value
    update_color()


def update_color():
    '''get the values of the slides concatinates and display the value'''
    color_box = tkinter.Label(input_frame, bg='#' +
                              red_value + green_value + blue_value, height=6, width=15)
    color_box.grid(row=1, column=3, columnspan=2,
                   padx=35, pady=10)

    color_hex = tkinter.Label(
        input_frame, text='#' + (red_value + green_value + blue_value).upper())
    color_hex.grid(row=3, column=3, columnspan=2)

    color_tup.config(text='(' + str(red_slider.get()) + '),' + ' (' +
                     str(green_slider.get()) + '),' + ' (' + str(blue_slider.get()) + ')')


def rand():
    red_value = str(random.randint(0, 255))
    green_value = str(random.randint(0, 255))
    blue_value = str(random.randint(0, 255))

    red_slider.set(red_value)
    green_slider.set(green_value)
    blue_slider.set(blue_value)

    update_color()


def set_color(r, g, b):
    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)


def save_color():
    # get the current values
    savered = str(red_slider.get())
    savegreen = str(green_slider.get())
    saveblue = str(blue_slider.get())

    while len(savered) < 3:
        savered = '0' + savered

    while len(str(savegreen)) < 3:
        savegreen = '0' + savegreen

    while len(str(saveblue)) < 3:
        saveblue = '0' + saveblue
    # create new widgets
    recall_button = tkinter.Button(
        output_frame, text='Recall', command=lambda: set_color(savered, savegreen, saveblue))

    new_color_tuple = tkinter.Label(output_frame, text='(' + savered + '),' + ' (' +
                                    savegreen + '),' + ' (' + saveblue + ')')
    new_color_hex = tkinter.Label(
        output_frame, text=('#' + red_value + green_value + blue_value).upper())
    new_outer_color_box = tkinter.Label(
        output_frame, bg='black', height=1, width=3)
    new_inner_color_box = tkinter.Label(
        output_frame, bg='#'+red_value + green_value + blue_value, height=1, width=3)
    recall_button.grid(row=stored_color.get(), column=1, padx=20, )
    new_color_tuple.grid(row=stored_color.get(), column=2, padx=20,)
    new_color_hex.grid(row=stored_color.get(), column=3, padx=20)

    new_outer_color_box.grid(row=stored_color.get(), column=4, padx=20,
                             pady=2, ipadx=5, ipady=5)
    new_inner_color_box.grid(row=stored_color.get(), column=4)
    stored_colors[stored_color.get()] = [new_color_tuple.cget(
        'text'), new_color_hex.cget('text')]

    if stored_color.get() < 5:
        stored_color.set(stored_color.get() + 1)


def save():
    # get directory
    filename = filedialog.asksaveasfilename(
        initialdir='./', title='Save Colors', filetypes=(('Text', '.txt'), ('All files', '*.*')))
    # open the file
    with open(filename, 'w') as f:
        f.write('Color Theme Maker Output\n')
        for save_entry in stored_colors.values():
            f.write(save_entry[0] + '\n' + save_entry[1] + '\n\n')


# defining layouts
input_frame = tkinter.LabelFrame(root, padx=9, pady=5)
output_frame = tkinter.LabelFrame(root, padx=5, pady=5)

input_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
output_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

red_label = tkinter.Label(input_frame, text='R')
red_slider = tkinter.Scale(input_frame, from_=0, to=255, command=getred)
red_button = tkinter.Button(input_frame, text='Red',
                            command=lambda: set_color(255, 0, 0))

green_label = tkinter.Label(input_frame, text='G')
green_slider = tkinter.Scale(input_frame, from_=0, to=255, command=getgreen)
green_button = tkinter.Button(
    input_frame, text='Green', command=lambda: set_color(0, 255, 0))

blue_label = tkinter.Label(input_frame, text='B')
blue_slider = tkinter.Scale(input_frame, from_=0, to=255, command=getblue)
blue_button = tkinter.Button(
    input_frame, text='Blue', command=lambda: set_color(0, 0, 255))


yellow_button = tkinter.Button(
    input_frame, text='Yellow', command=lambda: set_color(255, 255, 0))
cyan_button = tkinter.Button(
    input_frame, text='Cyan', command=lambda: set_color(0, 255, 255))
magenta_button = tkinter.Button(
    input_frame, text='Megenta', command=lambda: set_color(255, 0, 255))

# functionality buttons
store_button = tkinter.Button(input_frame, text='Store', command=save_color)
save_button = tkinter.Button(input_frame, text='Save', command=save)
quit_button = tkinter.Button(input_frame, text='Quit', command=root.destroy)
random_col = tkinter.Button(input_frame, text='Randomize', command=rand)

# use grid system
red_label.grid(row=0, column=0, sticky='W')
red_slider.grid(row=1, column=0)
red_button.grid(row=2, column=0, padx=1, pady=1, ipadx=20)

green_label.grid(row=0, column=1, sticky='W')
green_slider.grid(row=1, column=1)
green_button.grid(row=2, column=1, padx=1, pady=1, ipadx=14)


blue_label.grid(row=0, column=2, sticky='W')
blue_slider.grid(row=1, column=2)
blue_button.grid(row=2, column=2, padx=1, pady=1, ipadx=17)


yellow_button.grid(row=3, column=0, sticky='we', padx=1, pady=1)
magenta_button.grid(row=3, column=1, sticky='we', padx=1, pady=1)
cyan_button.grid(row=3, column=2, sticky='we', padx=1, pady=1)

store_button.grid(row=4, column=0, columnspan=3,  sticky='we', padx=1, pady=1)
save_button.grid(row=4, column=3,  sticky='we', padx=1, pady=1, ipadx=10)
quit_button.grid(row=4, column=4,  sticky='we', padx=1, pady=1, ipadx=10)
random_col.grid(row=0, column=3, columnspan=3, sticky='e', padx=(0, 33))

# color code box

color_box = tkinter.Label(input_frame, bg='black', height=6, width=15)
color_tup = tkinter.Label(input_frame, text='(0), (0), (0)')
color_hex = tkinter.Label(input_frame, text='#FFFFFF')

# pack them
color_box.grid(row=1, column=3, columnspan=2,
               padx=35, pady=10, ipadx=10, ipady=10)
color_tup.grid(row=2, column=3, columnspan=2)
color_hex.grid(row=3, column=3, columnspan=2)

# doing the output frame
stored_colors = {}
stored_color = IntVar()

for i in range(6):
    radio = tkinter.Radiobutton(output_frame, variable=stored_color, value=i)
    radio.grid(row=i, column=0, sticky='w')

    recall_button = tkinter.Button(output_frame, text='Recall', state=DISABLED)
    recall_button.grid(row=i, column=1, padx=20, )

    new_color_tuple = tkinter.Label(output_frame, text='(255), (255), (255)')
    new_color_hex = tkinter.Label(output_frame, text='#FFFFFF')

    new_outer_color_box = tkinter.Label(
        output_frame, bg='black', height=1, width=3)
    new_inner_color_box = tkinter.Label(
        output_frame, bg='white', height=1, width=3)

    new_color_tuple.grid(row=i, column=2, padx=20,)
    new_color_hex.grid(row=i, column=3, padx=20)

    new_outer_color_box.grid(row=i, column=4, padx=20,
                             pady=2, ipadx=5, ipady=5)
    new_inner_color_box.grid(row=i, column=4)

    # .cget() gets value to specific value
    stored_colors[stored_color.get()] = [new_color_tuple.cget(
        'text'), new_color_hex.cget('text')]
red_value = '00'
green_value = '00'
blue_value = '00'


# run the windows loop
root.mainloop()
