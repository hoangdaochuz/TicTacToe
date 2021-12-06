from tkinter import *
import random


def check_winner():
    for row in range(n_row):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for col in range(n_col):
        if buttons[0][col] == buttons[1][col] == buttons[2][col] != "":
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty_remain() is False:
        for row in range(n_row):
            for col in range(n_col):
                buttons[row][col].config(bg="yellow")
        return "Tie"
    else:
        return False


def new_game():
    global player
    player = random.choice(players)
    label.config(text=("Den luot " + player))
    for row in range(n_row):
        for col in range(n_col):
            buttons[row][col]['text'] = ""
            buttons[row][col].config(bg="white")


def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=("Den luot " + players[1]))

            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=("Den luot " + players[0]))

            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")


def empty_remain():
    empty = 9
    for row in range(n_row):
        for col in range(n_col):
            if buttons[row][col]['text'] != "":
                empty = empty - 1
    if empty == 0:
        return False
    else:
        return True


window = Tk()
window.title('Tic-tac-toe')

players = ['X', 'O']
player = random.choice(players)
buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
label = Label(window, text="Den luot " + player, font=("Consolas", 20))
label.pack(side='top')
butt_restart = Button(window, text='New game', font=("Consolas", 20), command=new_game)
butt_restart.pack(side='top')
frame = Frame(window)
frame.pack()
n_row = len(buttons)
n_col = len(buttons[0])

for row in range(n_row):
    for col in range(n_col):
        buttons[row][col] = Button(frame, text="", font=("Consolas", 20), width=5, height=2,
                                   command=lambda row=row, col=col: next_turn(row, col))
        buttons[row][col].grid(row=row, column=col)

window.mainloop()