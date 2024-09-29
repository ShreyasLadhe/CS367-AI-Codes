from collections import deque
import numpy as np
import random

class Node:
    def __init__(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth

def get_successors(node):
    successors = []
    value = 0
    index = node.state.index(0)
    quotient = index//3
    remainder = index%3
    if quotient == 0:
        moves = [3]
    if quotient == 1:
        moves = [-3, 3]
    if quotient == 2:
        moves = [-3]
    if remainder == 0:
        moves += [1]
    if remainder == 1:
        moves += [-1, 1]
    if remainder == 2:
        moves += [-1]

    for move in moves:
        im = index + move
        if im >= 0 and im < 9:
            new_state = list(node.state)
            temp = new_state[im]
            new_state[im] = new_state[index]
            new_state[index] = temp
            successor = Node(new_state, node, node.depth + 1) 
            successors.append(successor)
    return successors

def dls(node, goal_state, depth_limit):
    if node.state == goal_state:
        path = []
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1]

    if node.depth >= depth_limit:
        return None

    for successor in get_successors(node):
        result = dls(successor, goal_state, depth_limit)
        if result:
            return result

    return None

def depth_limited_search(start_state, goal_state, depth_limit):
    start_node = Node(start_state)
    return dls(start_node, goal_state, depth_limit)

start_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
s_node = Node(start_state)
D = 20  
d = 0
while d <= D:
    goal_state = random.choice(list(get_successors(s_node))).state
    s_node = Node(goal_state)
    d = d + 1

depth_limit = 10

solution = depth_limited_search(start_state, goal_state, depth_limit)

if solution:
    print("Solution found within depth limit:")
    for step in solution:
        print(step)
else:
    print(f"No solution found within depth limit {depth_limit}.")
