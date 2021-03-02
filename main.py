import pygame
import sys
from AI import Computer
import time


class TicTacToe:
    def __init__(self):
        pygame.init()
        self.size_block = 150
        self.margin = 15
        self.width = self.height = self.size_block * 3 + self.margin * 4

        self.size_window = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size_window)
        pygame.display.set_caption('Tic Tac Toe')

        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)
        self.board = [[0] * 3 for _ in range(3)]
        self.query = 0
        self.stop_game = False
        self.bot_move = False
        self.bot = Computer()

    def check_win(self, board, sign):
        zeroes = 0
        for row in board:
            zeroes += row.count(0)
            if row.count(sign) == 3:
                return sign

        for col in range(3):
            if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
                return sign

        if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return sign

        if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            return sign

        if zeroes == 0:
            return 'Tie game'

        return False

    def start_game(self):
        self.stop_game = False
        self.board = [[0] * 3 for _ in range(3)]
        self.query = 0
        self.screen.fill(self.black)

    def run_game(self):
        while not False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.stop_game:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    col = x_mouse // (self.size_block + self.margin)
                    row = y_mouse // (self.size_block + self.margin)
                    if self.board[row][col] == 0 and not self.bot_move:
                        if self.query % 2 == 0:
                            self.board[row][col] = 'x'
                            self.bot_move = True
                            self.query += 1
                        # else:
                        #     self.board[row][col] = 'o'
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.start_game()

            if self.query % 2 != 0 and self.bot_move and not self.stop_game:
                row_1_col_1 = self.bot.computerMove(self.board)
                self.bot_move = False
                print(row_1_col_1)
                self.board[row_1_col_1[0]][row_1_col_1[1]] = 'o'
                self.query += 1

            if not self.stop_game:
                for row in range(3):
                    for col in range(3):
                        if self.board[row][col] == 'x':
                            self.color = self.red
                        elif self.board[row][col] == 'o':
                            self.color = self.green
                        else:
                            self.color = self.white
                        x = col * self.size_block + (col + 1) * self.margin
                        y = row * self.size_block + (row + 1) * self.margin
                        pygame.draw.rect(self.screen, self.color, (x, y, self.size_block, self.size_block))
                        if self.color == self.red:
                            self.draw_lines(x, y)
                        elif self.color == self.green:

                            pygame.draw.circle(self.screen, self.white,
                                               (x + self.size_block // 2, y + self.size_block // 2),
                                               self.size_block // 2 - 3, 10)

            # if (self.query - 1) % 2 == 0:
            #     self.game_over = self.check_win(self.board, 'x')
            # else:
            #     self.game_over = self.check_win(self.board, 'o')

            self.game_over = self.check_win(self.board, 'x')
            if not self.game_over:
                self.game_over = self.check_win(self.board, 'o')
            pygame.display.update()

            if self.game_over:
                self.stop_game = True
                time.sleep(2)
                self.screen.fill(self.black)
                font = pygame.font.SysFont('stxingkai', 80)
                if self.game_over == 'x':
                    self.game_over = 'User win'
                elif self.game_over == 'o':
                    self.game_over = 'Bot win'
                text_1 = font.render(self.game_over, True, self.white)
                text_rect = text_1.get_rect()
                text_x = self.screen.get_width() / 2 - text_rect.width / 2
                text_y = self.screen.get_height() / 2 - text_rect.height / 2
                self.screen.blit(text_1, (text_x, text_y))

            pygame.display.update()

    def draw_lines(self, x, y):
        pygame.draw.line(self.screen, self.white, (x + 5, y + 5),
                         (x + self.size_block - 5, y + self.size_block - 5), 10)
        pygame.draw.line(self.screen, self.white, (x + self.size_block - 5, y + 5),
                         (x + 5, y + self.size_block - 5), 10)


Game = TicTacToe()
Game.run_game()
