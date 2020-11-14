import tkinter
from tkinter import StringVar, ACTIVE, NORMAL, DISABLED
import random

root = tkinter.Tk()

root.title('Memory Game')
root.iconbitmap('game.ico')
root.geometry('400x400')
root.resizable(0, 0)

#fonts and colors
game_font1 = ('Arial', 12)
game_font2 = ('Arial', 8)

white = '#c6cbcd'
white_light = '#fbfcfc'

megenta = '#90189e'
megenta_light = '#f802f9'

cyan = '#078384'
cyan_light = '#00fafa'

yellow = '#9ba00f'
yellow_light = '#f7f801'

root_color = '#2eb4c6'
game_color = '#f6f7f7'
root.config(bg=root_color)


# set gloabal var
time = 500
score = 0
game_seq = []
player_seq = []

# def functions


def pickseq():
    ''' pick the next val and not the same val again '''

    # seq is 0 choose anything else check the previous is not the same
    while True:
        value = random.randint(1, 4)
        if len(game_seq) == 0:
            game_seq.append(value)
            break
        # make sure the current value is not same as last
        elif value != game_seq[-1]:
            game_seq.append(value)
            break
    # as value has been added
    playseq()


def playseq():
    '''play sequence'''
    changelabel('Playing')

    # without delay al button will animate at same time by after method
    delay = 0

    for value in game_seq:
        if value == 1:
            root.after(delay, lambda: animate(white_button))

        elif value == 2:
            root.after(delay, lambda: animate(megenta_button))

        elif value == 3:
            root.after(delay, lambda: animate(cyan_button))

        elif value == 4:
            root.after(delay, lambda: animate(yellow_button))

    # increment delay for next iteration of loop
        delay += time


def animate(button):
    ''' animate the button'''

    button.config(state=NORMAL)
    button.config(state=ACTIVE)
    root.after(time, lambda: button.config(state=NORMAL))


def changelabel(message):
    ''' update the start button text '''
    start_button.config(text=message)
    if message == 'Wrong!!':
        start_button.config(bg='red')
    else:
        start_button.config(bg=game_color)


def set_diff():
    ''' use radio button'''
    # set time based on flashes
    global time
    # change time

    if diff.get() == 'easy':
        time = 1000
    elif diff.get() == 'medium':
        time = 500
    elif diff.get() == 'difficult':
        time = 250


def press(value):
    # add the players sequence
    player_seq.append(value)

    if len(player_seq) == len(game_seq):
        checkround()


def checkround():
    # check the correctness
    global player_seq
    global game_seq
    global score

    if player_seq == game_seq:
        changelabel('Correct!!')
        score += len(player_seq) + int(1000 / time)
        root.after(500, pickseq)

    # if the player is incorrent
    else:
        changelabel('Wrong!!')
        score = 0
        disable()

        game_seq = []
        root.after(2000, lambda: changelabel("New Game"))

    # regardless of levels player sequence has to be changed
    player_seq = []

    # update score
    score_label.config(text="Score: " + str(score))


def disable():
    '''disable all button'''
    white_button.config(state=DISABLED)
    megenta_button.config(state=DISABLED)
    cyan_button.config(state=DISABLED)
    yellow_button.config(state=DISABLED)


def enable():
    # enable all button
    white_button.config(state=NORMAL)
    megenta_button.config(state=NORMAL)
    cyan_button.config(state=NORMAL)
    yellow_button.config(state=NORMAL)
    pickseq()


# create frames
infoframe = tkinter.Frame(root, bg=root_color)
game_frame = tkinter.LabelFrame(root, bg=game_color)
infoframe.pack(pady=(10, 20))
game_frame.pack()

# add widgets

start_button = tkinter.Button(
    infoframe, text="New Game", font=game_font1, bg=game_color, command=enable)
score_label = tkinter.Label(
    infoframe, text="Score: " + str(score), font=game_font1, bg=root_color)

start_button.grid(row=0, column=0, padx=20, ipadx=30)
score_label.grid(row=0, column=1)

# game button
white_button = tkinter.Button(
    game_frame, bg=white, activebackground=white_light, borderwidth=3, command=lambda: press(1), state=DISABLED)
white_button.grid(row=0, column=0, columnspan=2,
                  padx=10, pady=10, ipadx=60, ipady=50)

megenta_button = tkinter.Button(
    game_frame, bg=megenta, activebackground=megenta_light, borderwidth=3, command=lambda: press(2), state=DISABLED)

cyan_button = tkinter.Button(
    game_frame, bg=cyan, activebackground=cyan_light, borderwidth=3, command=lambda: press(3), state=DISABLED)

yellow_button = tkinter.Button(
    game_frame, bg=yellow, activebackground=yellow_light, borderwidth=3, command=lambda: press(4), state=DISABLED)


megenta_button.grid(row=0, column=2, columnspan=2,
                    padx=10, pady=10, ipadx=60, ipady=50)
cyan_button.grid(row=1, column=0, columnspan=2,
                 padx=10, pady=10, ipadx=60, ipady=50)
yellow_button.grid(row=1, column=2, columnspan=2,
                   padx=10, pady=10, ipadx=60, ipady=50)

# radio button
diff = StringVar()
diff.set('easy')
tkinter.Label(game_frame, text='Difficulty', font=game_font2,
              bg=game_color).grid(row=2, column=0)
tkinter.Radiobutton(game_frame, text='Easy', variable=diff, value='easy',
                    font=game_font2, bg=game_color, command=set_diff).grid(row=2, column=1)
tkinter.Radiobutton(game_frame, text='Medium', variable=diff, value='medium',
                    font=game_font2, bg=game_color, command=set_diff).grid(row=2, column=2)
tkinter.Radiobutton(game_frame, text='Difficult', variable=diff, value='difficult',
                    font=game_font2, bg=game_color, command=set_diff).grid(row=2, column=3)


root.mainloop()
