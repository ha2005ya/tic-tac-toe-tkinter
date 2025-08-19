from tkinter import *
import random

def next_turn(row, col):
    global player

    if game_btns[row][col]['text'] == '' and check_winner() == False:
        game_btns[row][col]['text'] = player

        result = check_winner()
        if result == False:
            player = players[0] if player == players[1] else players[1]
            label.config(text=(player + " turn"))
        elif result == True:
            label.config(text=(player + " wins!"))
        elif result == 'tie':
            label.config(text="Tie, No winner!")

def check_winner():
    # horizontal
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != '':
            for col in range(3):
                game_btns[row][col].config(bg='cyan')
            return True

    # vertical
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != '':
            for row in range(3):
                game_btns[row][col].config(bg='cyan')
            return True

    # diagonals
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != '':
        game_btns[0][0].config(bg='cyan')
        game_btns[1][1].config(bg='cyan')
        game_btns[2][2].config(bg='cyan')
        return True
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != '':
        game_btns[0][2].config(bg='cyan')
        game_btns[1][1].config(bg='cyan')
        game_btns[2][0].config(bg='cyan')
        return True

    # tie
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='red')
        return 'tie'

    return False

def check_empty_spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != "":
                spaces -= 1
    return spaces != 0

def start_new_game():
    global player
    player = random.choice(players)
    label.config(text=(player + " turn"))
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text='', bg='#F0F0F0')

window = Tk()
window.title("Tic-Tac-Toe Game")

players = ['X', 'O']
player = random.choice(players)

game_btns = [[0,0,0],[0,0,0],[0,0,0]]

label = Label(text=(player + " turn"), font=('consolas', 40))
label.pack(side='top')

restart_btn = Button(text='Restart', font=('consolas', 20), command=start_new_game)
restart_btn.pack(side='top')

btns_frame = Frame(window)
btns_frame.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame, text='', font=('consolas', 50), width=4, height=1,
                                     command=lambda row=row, col=col: next_turn(row, col))
        game_btns[row][col].grid(row=row, column=col)

window.mainloop()
