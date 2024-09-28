import random
import time
from collections import deque
import memory_profiler

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

def bfs(graph, initial_state):
    frontier = deque()
    visited = set()
    frontier.append(initial_state)

    while frontier:
        current_node = frontier.popleft()
        
        if current_node == goal:
            return True

        visited.add(tuple(map(tuple, current_node)))

        blank = [(i, j) for i in range(3) for j in range(3) if current_node[i][j] == 0][0]
        for move in ['up', 'down', 'left', 'right']:
            if check_move(blank, move):
                new_blank = get_pos(blank, move)
                new_state = [row[:] for row in current_node]
                new_state[blank[0]][blank[1]], new_state[new_blank[0]][new_blank[1]] = (
                    new_state[new_blank[0]][new_blank[1]],
                    new_state[blank[0]][blank[1]],
                )
                if tuple(map(tuple, new_state)) not in visited:
                    frontier.append(new_state)

    return False

depths = [1, 2, 3, 4, 5, 6, 7, 8]
results = []

for d in depths:
    puzzle_instance = puzzle(d)
    start_time = time.time()
    mem_usage = memory_profiler.memory_usage((bfs, (puzzle_instance,)))
    time_taken = time.time() - start_time
    max_memory = max(mem_usage)

    results.append((d, time_taken, max_memory))

print(f"{'Depth (d)':<10} {'Time Taken (s)':<20} {'Memory Used (MB)':<20}")
for result in results:
    print(f"{result[0]:<10} {result[1]:<20.6f} {result[2]:<20.6f}")