import random


class Computer:
    def __init__(self):
        self.sign = 'o'
        self.user = 'x'

    def computerMove(self, board):
        attack = self.attack_or_defense(board, self.sign)

        if attack:
            return attack

        defense = self.attack_or_defense(board, self.user)

        if defense:
            return defense

        continue_move = self.continue_moving(board, self.sign)

        if continue_move:
            return continue_move

        if board[1][1] == 'x':
            return self.strategy(board)

        return self.randomMove(board)

    def randomMove(self, board):
        move = board[1][1]
        row, col = 1, 1

        while move == 'x':
            row = random.choice([0, 1, 2])
            col = random.choice([0, 1, 2])
            move = board[row][col]

        return row, col

    def strategy(self, board):
        possible = [(0, 0), (2, 0), (0, 2), (2, 2)]
        row, col = random.choice(possible)

        while board[row][col] != 0:
            row, col = random.choice(possible)

        return row, col

    def continue_moving(self, board, sign):
        for i in range(3):
            if board[i][0] == sign and board[i][1] == 0 and board[i][2] == 0:
                return i, 2
            elif board[i][0] == 0 and board[i][1] == 0 and board[i][2] == sign:
                return i, 1
            elif board[i][0] == 0 and board[i][1] == sign and board[i][2] == 0:
                return i, 0

        for i in range(3):
            if board[0][i] == sign and board[1][i] == 0 and board[2][i] == 0:
                return 2, i
            elif board[0][i] == 0 and board[1][i] == 0 and board[2][i] == sign:
                return 1, i
            elif board[0][i] == 0 and board[1][i] == sign and board[2][i] == 0:
                return 2, i

        if board[0][0] == sign and board[1][1] == 0 and board[2][2] == 0:
            return 2, 2
        elif board[0][0] == 0 and board[1][1] == 0 and board[2][2] == sign:
            return 1, 1
        elif board[0][0] == 0 and board[1][1] == sign and board[2][2] == 0:
            return 0, 0

        if board[0][2] == sign and board[1][1] == 0 and board[2][0] == 0:
            return 2, 0
        elif board[0][2] == 0 and board[1][1] == 0 and board[2][0] == sign:
            return 1, 1
        elif board[0][2] == 0 and board[1][1] == sign and board[2][0] == 0:
            return 0, 2

        return False

    def attack_or_defense(self, board, sign):
        for i in range(3):
            if board[i][0] == sign and board[i][1] == sign and board[i][2] == 0:
                return i, 2
            elif board[i][0] == sign and board[i][1] == 0 and board[i][2] == sign:
                return i, 1
            elif board[i][0] == 0 and board[i][1] == sign and board[i][2] == sign:
                return i, 0

        for i in range(3):
            if board[0][i] == sign and board[1][i] == sign and board[2][i] == 0:
                return 2, i
            elif board[0][i] == sign and board[1][i] == 0 and board[2][i] == sign:
                return 1, i
            elif board[0][i] == 0 and board[1][i] == sign and board[2][i] == sign:
                return 2, i

        if board[0][0] == sign and board[1][1] == sign and board[2][2] == 0:
            return 2, 2
        elif board[0][0] == sign and board[1][1] == 0 and board[2][2] == sign:
            return 1, 1
        elif board[0][0] == 0 and board[1][1] == sign and board[2][2] == sign:
            return 0, 0

        if board[0][2] == sign and board[1][1] == sign and board[2][0] == 0:
            return 2, 0
        elif board[0][2] == sign and board[1][1] == 0 and board[2][0] == sign:
            return 1, 1
        elif board[0][2] == 0 and board[1][1] == sign and board[2][0] == sign:
            return 0, 2

        return False
