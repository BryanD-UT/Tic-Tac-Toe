# Tic Tac Toe Game
# Bryan Dinh Dec 26, 2023
# tic_tac_toe
# Background Processes


def draw_board(grid):
    """
    Draws board in the command line
    :param grid:
    :return: None
    """
    # To underline hello: \033[4mhello\033[0m
    print("________________")
    for i in range(len(grid)):
        print(grid[i][0], grid[i][1], grid[i][2])
        # print(f'\033[4m|{grid[i][0]}|{grid[i][1]}|{grid[i][2]}\033[0m|')



def game_over(grid):
    """
    Checks if the game is over by a victory or a tie
    :param grid:
    :return: Bool
    """
    if all(cell is not None for row in grid for cell in row):
        return True, "Tie"
    if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
        if grid[1][1] is not None:
            return True, grid[1][1]
    for i in range(len(grid)):
        if grid[i][0] == grid[i][1] == grid[i][2]:
            if grid[i][0] is not None:
                return True, grid[i][0]
        elif grid[0][i] == grid[1][i] == grid[2][i]:
            if grid[0][i] is not None:
                return True, grid[0][i]

    return False, None


def make_move_dep(grid, p):
    """
    Makes a move by making a mark on the grid based on the players letter.
    :param grid:
    :param p:
    :return:
    """
    y, x = int(input(f'Player {p}, input your row: ')), int(input('and your column: '))
    while grid[y][x] is not None:
        print(f'Overlapping input, try again:')
        y, x = int(input('input your row: ')), int(input('and your column: '))
    return y, x

def make_move(grid, x, y, p):
    """
    Makes a move
    :param grid:
    :param x:
    :param y:
    :return:
    """
    if grid[y][x] is None:
        match p:
            case "X":
                grid[y][x] = "X"
            case "O":
                grid[y][x] = "O"
        return True
    else:
        return False

def announcement(state, victor):
    if state == True:
        if victor == "Tie":
            return "Draw"
        else:
            msg = f'Player {victor} wins!'
            return msg