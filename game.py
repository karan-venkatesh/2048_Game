from random import randint


class Board:
    def __init__(self, size=4):
        self.board_size = size
        self.game_active = True
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.free_spaces = self.board_size * self.board_size
        self.score = 0
        self.add_tile()
        self.add_tile()

    def count_empty(self):
        self.free_spaces = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == 0:
                    self.free_spaces += 1

    def new_game(self):
        self.game_active = True
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.free_spaces = self.board_size * self.board_size
        self.score = 0
        self.add_tile()
        self.add_tile()

    def add_tile(self):
        fill_spot = randint(0, self.free_spaces - 1)
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == 0:
                    if fill_spot != 0:
                        fill_spot -= 1
                    else:
                        if randint(0,10) == 10:
                            self.board[i][j] = 4
                        else:
                            self.board[i][j] = 2
                        fill_spot -= 1
                        break
            if fill_spot < 0:
                break
        self.count_empty()
        if self.free_spaces == 0 and not (self.move_up(active=False)[0] or self.move_left(active=False)[0] or
                                          self.move_right(active=False)[0] or self.move_down(active=False)[0]):
                self.game_active = False

    def check_alive(self):
        return self.game_active

    def play_move(self, direction):
        if not self.game_active:
            print("Game over start new game")
            return False
        if direction.lower() == 'left':
            if self.move_left()[0]:
                self.count_empty()
                self.add_tile()
                self.display_board()
                return True
            else:
                return False
        elif direction.lower() == 'up':
            if self.move_up()[0]:
                self.count_empty()
                self.add_tile()
                self.display_board()
                return True
            else:
                return False
        elif direction.lower() == 'right':
            if self.move_right()[0]:
                self.count_empty()
                self.add_tile()
                self.display_board()
                return True
            else:
                return False
        elif direction.lower() == 'down':
            if self.move_down()[0]:
                self.count_empty()
                self.add_tile()
                self.display_board()
                return True
            else:
                return False
        else:
            return False

    def test_up(self, board_test):
        score = 0
        change = False
        temp_board = self.copy_board(board_test)
        for i in range(self.board_size):
            add_flag = False
            point = 0
            add_val = 0
            for j in range(self.board_size):
                if board_test[j][i] != 0:
                    if add_flag and add_val == board_test[j][i]:
                        temp_board[point - 1][i] = temp_board[j][i] * 2
                        score += temp_board[j][i] * 2
                        change = True
                        add_flag = False
                        add_val = 0
                    else:
                        if board_test[point][i] != board_test[j][i]:
                            change = True
                            temp_board[point][i] = temp_board[j][i]
                        point += 1
                        add_flag = True
                        add_val = board_test[j][i]
            for j in range(point, self.board_size):
                temp_board[j][i] = 0
        return change, score, temp_board

    def test_down(self, board_test):
        score = 0
        change = False
        temp_board = self.copy_board(board_test)
        for i in range(self.board_size):
            add_flag = False
            point = self.board_size - 1
            add_val = 0
            for j in reversed(range(self.board_size)):
                if board_test[j][i] != 0:
                    if add_flag and add_val == board_test[j][i]:
                        temp_board[point + 1][i] = temp_board[j][i] * 2
                        score += temp_board[j][i] * 2
                        change = True
                        add_flag = False
                        add_val = 0
                    else:
                        if board_test[point][i] != board_test[j][i]:
                            change = True
                            temp_board[point][i] = temp_board[j][i]
                        point -= 1
                        add_flag = True
                        add_val = board_test[j][i]
            for j in reversed(range(0, point + 1)):
                temp_board[j][i] = 0
        return change, score, temp_board

    def test_left(self, board_test):
        score = 0
        change = False
        temp_board = self.copy_board(board_test)
        for i in range(self.board_size):
            add_flag = False
            point = 0
            add_val = 0
            for j in range(self.board_size):
                if board_test[i][j] != 0:
                    if add_flag and add_val == board_test[i][j]:
                        temp_board[i][point - 1] = temp_board[i][j] * 2
                        score += board_test[i][j] * 2
                        change = True
                        add_flag = False
                        add_val = 0
                    else:
                        if board_test[i][point] != board_test[i][j]:
                            change = True
                            temp_board[i][point] = temp_board[i][j]
                        point += 1
                        add_flag = True
                        add_val = board_test[i][j]

            for j in range(point, self.board_size):
                temp_board[i][j] = 0
        return change, score, temp_board

    def test_right(self, board_test):
        score = 0
        change = False
        temp_board = self.copy_board(board_test)
        for i in range(self.board_size):
            add_flag = False
            point = self.board_size - 1
            add_val = 0
            for j in reversed(range(self.board_size)):
                if board_test[i][j] != 0:
                    if add_flag and add_val == board_test[i][j]:
                        temp_board[i][point + 1] = temp_board[i][j] * 2
                        score += board_test[i][j] * 2
                        change = True
                        add_flag = False
                        add_val = 0
                    else:
                        if board_test[i][point] != board_test[i][j]:
                            change = True
                            temp_board[i][point] = temp_board[i][j]
                        point -= 1
                        add_flag = True
                        add_val = board_test[i][j]
            for j in reversed(range(0, point + 1)):
                temp_board[i][j] = 0
        return change, score, temp_board

    def move_up(self, active=True):
        initial_score = self.score
        final_score = initial_score
        change = False
        temp_board = self.copy_board()
        for i in range(self.board_size):
            add_flag = False
            point = 0
            add_val = 0
            for j in range(self.board_size):
                if self.board[j][i] != 0:
                    if add_flag and add_val == self.board[j][i]:
                        if active:
                            self.board[point - 1][i] = self.board[j][i] * 2
                            self.score += self.board[j][i] * 2
                        temp_board[point - 1][i] = temp_board[j][i] * 2
                        final_score += self.board[j][i] * 2
                        change = True
                        add_flag = False
                        add_val = 0
                    else:
                        if self.board[point][i] != self.board[j][i]:
                            change = True
                            if active:
                                self.board[point][i] = self.board[j][i]
                            temp_board[point][i] = temp_board[j][i]
                        point += 1
                        add_flag = True
                        add_val = self.board[j][i]
            for j in range(point, self.board_size):
                if active:
                    self.board[j][i] = 0
                temp_board[j][i] = 0
        return change, initial_score, final_score, temp_board

    def move_left(self, active=True):
        initial_score = self.score
        final_score = initial_score
        change = False
        temp_board = self.copy_board()
        for i in range(self.board_size):
            add_flag = False
            point = 0
            add_val = 0
            for j in range(self.board_size):
                if self.board[i][j] != 0:
                    if add_flag and add_val == self.board[i][j]:
                        if active:
                            self.board[i][point - 1] = self.board[i][j] * 2
                            self.score += self.board[i][j] * 2
                        temp_board[i][point - 1] = temp_board[i][j] * 2
                        final_score += self.board[i][j] * 2
                        change = True
                        add_flag = False
                        add_val = 0
                    else:
                        if self.board[i][point] != self.board[i][j]:
                            change = True
                            if active:
                                self.board[i][point] = self.board[i][j]
                            temp_board[i][point] = temp_board[i][j]
                        point += 1
                        add_flag = True
                        add_val = self.board[i][j]

            for j in range(point, self.board_size):
                if active:
                    self.board[i][j] = 0
                temp_board[i][j] = 0
        return change, initial_score, final_score, temp_board

    def move_right(self, active=True):
        initial_score = self.score
        final_score = initial_score
        change = False
        temp_board = self.copy_board()
        for i in range(self.board_size):
            add_flag = False
            point = self.board_size - 1
            add_val = 0
            for j in reversed(range(self.board_size)):
                if self.board[i][j] != 0:
                    if add_flag and add_val == self.board[i][j]:
                        if active:
                            self.board[i][point + 1] = self.board[i][j] * 2
                            self.score += self.board[i][j] * 2
                        temp_board[i][point + 1] = temp_board[i][j] * 2
                        final_score += self.board[i][j] * 2
                        change = True
                        add_flag = False
                        add_val = 0
                    else:
                        if self.board[i][point] != self.board[i][j]:
                            change = True
                            if active:
                                self.board[i][point] = self.board[i][j]
                            temp_board[i][point] = temp_board[i][j]
                        point -= 1
                        add_flag = True
                        add_val = self.board[i][j]
            for j in reversed(range(0, point + 1)):
                if active:
                    self.board[i][j] = 0
                temp_board[i][j] = 0
        return change, initial_score, final_score, temp_board

    def move_down(self, active=True):
        initial_score = self.score
        final_score = initial_score
        change = False
        temp_board = self.copy_board()
        for i in range(self.board_size):
            add_flag = False
            point = self.board_size - 1
            add_val = 0
            for j in reversed(range(self.board_size)):
                if self.board[j][i] != 0:
                    if add_flag and add_val == self.board[j][i]:
                        if active:
                            self.board[point + 1][i] = self.board[j][i] * 2
                            self.score += self.board[j][i] * 2
                        temp_board[point + 1][i] = temp_board[j][i] * 2
                        final_score += self.board[j][i] * 2
                        change = True
                        add_flag = False
                        add_val = 0
                    else:
                        if self.board[point][i] != self.board[j][i]:
                            change = True
                            if active:
                                self.board[point][i] = self.board[j][i]
                            temp_board[point][i] = temp_board[j][i]
                        point -= 1
                        add_flag = True
                        add_val = self.board[j][i]
            for j in reversed(range(0, point + 1)):
                if active:
                    self.board[j][i] = 0
                temp_board[j][i] = 0
        return change, initial_score, final_score, temp_board

    def copy_board(self, target_board=None):
        board_copy = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        for i in range(self.board_size):
            for j in range(self.board_size):
                if target_board:
                    board_copy[i][j] = target_board[i][j]
                else:
                    board_copy[i][j] = self.board[i][j]
        return board_copy

    def display_board(self):
        for row in self.board:
            print(' _____ _____ _____ _____ ')
            print('|', end='')
            for cell in row:
                pad = ' ' * (5 - len(str(cell)))
                print(pad + str(cell) + '|', end='')
            print('')
        print(' _____ _____ _____ _____ ')
        print('Score:', self.score)
        if not self.game_active:
            print('Game Over')

    def get_score(self):
        return self.score

    def max_tile(self):
        largest=0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j]>largest:
                    largest=self.board[i][j]
        return largest
