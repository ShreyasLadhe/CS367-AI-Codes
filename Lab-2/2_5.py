import random

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def check_move(pos, move):
    row, col = pos
    if move == 'up' and row > 0:
        return True
    if move == 'down' and row < 2:
        return True
    if move == 'left' and col > 0:
        return True
    if move == 'right' and col < 2:
        return True
    return False

def get_pos(pos, move):
    row, col = pos
    if move == 'up':
        return (row - 1, col)
    if move == 'down':
        return (row + 1, col)
    if move == 'left':
        return (row, col - 1)
    if move == 'right':
        return (row, col + 1)

def puzzle(depth):
    curr_state = [row[:] for row in goal]
    blank = (2, 2)
    moves = ['up', 'down', 'left', 'right']
    
    for _ in range(depth):
        move = random.choice(moves)
        if check_move(blank, move):
            new_blank = get_pos(blank, move)
            curr_state[blank[0]][blank[1]], curr_state[new_blank[0]][new_blank[1]] = (
                curr_state[new_blank[0]][new_blank[1]],
                curr_state[blank[0]][blank[1]],
            )
            blank = new_blank

    return curr_state

depth = 5
puzzle_state = puzzle(depth)
for row in puzzle_state:
    print(row)