import random

class MENACE:
    def __init__(self):
        self.matchboxes = {
            'empty_board': {'move_1': 3, 'move_2': 3, 'move_3': 3},
        }
        self.history = []

    def select_move(self, board_state):
        moves = self.matchboxes[board_state]
        total_beads = sum(moves.values())
        r = random.randint(1, total_beads)
        cum = 0
        for move, beads in moves.items():
            cum += beads
            if r <= cum:
                self.history.append((board_state, move))
                return move

    def update(self, result):
        for board_state, move in self.history:
            if result == 'win':
                self.matchboxes[board_state][move] += 1
            elif result == 'loss':
                self.matchboxes[board_state][move] -= 1
        self.history.clear()

menace = MENACE()
move = menace.select_move('empty_board')
print("MENACE selected:", move)
