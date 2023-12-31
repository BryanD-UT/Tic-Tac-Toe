# Tic Tac Toe Game
# Bryan Dinh Dec 26, 2023
# tic_tac_toe

from ttt_background import *
import random


grid = [[None, None, None], [None, None, None], [None, None, None]]
status = False
victor = None
P1 = random.choice(["X", "O"])
P2 = "O" if P1 == "X" else "X"

while not status:
    # clear()
    draw_board(grid)
    y1, x1 = make_move_dep(grid, P1)
    grid[y1][x1] = P1
    y2, x2 = make_move_dep(grid, P2)
    # noinspection PyTypeChecker
    grid[y2][x2] = P2
    status, victor = game_over(grid)

if victor == "Tie":
    print("Draw")
else:
    print(f'Player {victor} wins!')
