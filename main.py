from tkinter import *


def reset():
    window.destroy()
    new_game()


def game_cond(player):
    if bc[0] == bc[1] == bc[2] == player or \
            bc[3] == bc[4] == bc[5] == player or \
            bc[6] == bc[7] == bc[8] == player or \
            bc[0] == bc[3] == bc[6] == player or \
            bc[1] == bc[4] == bc[7] == player or \
            bc[2] == bc[5] == bc[8] == player or \
            bc[0] == bc[4] == bc[8] == player or \
            bc[2] == bc[4] == bc[6] == player:
        text = f"Win: {player}"
        for i in range(9):
            btns[i].config(command=NO)
        restart = Button(window, text="Play again.", command=reset)
        restart.place(x=250, y=450, anchor=CENTER)
    elif count == 9:
        text = "No one wins!"
        restart = Button(window, text="Play again.", command=reset)
        restart.place(x=250, y=450, anchor=CENTER)
    else:
        text = "Game in process..."
    game_text.config(text=text)


def bfc(x):
    if bc[x] != -1:
        return
    global count
    count += 1
    if count % 2 == 0:
        txt = "O"
    else:
        txt = "X"
    btns[x].config(text=txt)
    bc[x] = txt
    game_cond(txt)


def new_game():

    global count, bc, btns, game_text, window

    window = Tk()
    window.geometry("500x500")
    window.title("Tic-Tac-Toe")

    count = 0
    bc = [-1] * 9
    btns = []

    game_text = Label(window, text="Starting game!")
    game_text.place(relx=0.5, rely=0.1, anchor=CENTER)

    for i in range(1, 4):
        for j in range(1, 4):
            btn = Button(window, text="", font=("arial", 40))
            btn.place(width=100, height=100, x=i * 100, y=j * 100)
            btns.append(btn)

    for i in range(9):
        btns[i].config(command=lambda x=i: bfc(x))

    mainloop()


new_game()
