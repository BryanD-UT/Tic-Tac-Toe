from tkinter import *
from tkinter import ttk
# import tkinter as tk
from ttt_background import *
import random



# Creating the base variables for the game
grid = [[None, None, None], [None, None, None], [None, None, None]]
status = False
victor = None
P1 = random.choice(["X", "O"])
P2 = "O" if P1 == "X" else "X"
# global Current
Current = P1


def calculator(x, y):
    print(x * y)


def mark(x, y):
    global Current
    #print("Button Press:", x, y, Current)
    if make_move(grid, x, y, Current):
        make_move(grid, x, y, Current)
        ttk.Button(frm, text=Current, state='disabled').grid(column=x, row=y)
        match Current:
            case "X":
                Current = "O"
            case "O":
                Current = "X"
    else:
        print("Invalid Move")
    #draw_board(grid)
    state, winner = game_over(grid)
    #print(game_over(grid))
    if state:

        #root.destroy()
        if winner == "Tie":
            root.title(f'Tic-Tac-Toe, Tie!')
            # print("Tie")
        else:
            root.title(f'Tic-Tac-Toe, Player {winner} Wins!')
            # print(f'Player {winner} Wins!')
root = Tk()
root.title("Tic-Tac-Toe")
frm = ttk.Frame(root, padding=10)
frm.grid()

# Buttons
ttk.Button(frm,
           text="",
           command=lambda: mark(0, 0)).grid(column=0, row=0)
ttk.Button(frm,
           text="",
           command=lambda: mark(0, 1)).grid(column=0, row=1)
ttk.Button(frm,
           text="",
           command=lambda: mark(0, 2)).grid(column=0, row=2)
ttk.Button(frm,
           text="",
           command=lambda: mark(1, 0)).grid(column=1, row=0)
ttk.Button(frm,
           text="",
           command=lambda: mark(1, 1)).grid(column=1, row=1)
ttk.Button(frm,
           text="",
           command=lambda: mark(1, 2)).grid(column=1, row=2)
ttk.Button(frm,
           text="",
           command=lambda: mark(2, 0)).grid(column=2, row=0)
ttk.Button(frm,
           text="",
           command=lambda: mark(2, 1)).grid(column=2, row=1)
ttk.Button(frm,
           text="",
           command=lambda: mark(2, 2)).grid(column=2, row=2)

root.mainloop()


# for row in range(3):
#     for column in range(3):
#         match player:
#             case "X":
#                 ttk.Button(frm,
#                            text="",
#                            command=lambda: mark(column,row)).grid(column=column, row=row)
