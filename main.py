from game import Board


def score_board(board):
    score = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                score += 10
            score += (i + j) * board[i][j]
            if i + 1 < len(board):
                if board[i][j] == board[i + 1][j]:
                    score += board[i][j]
            if j + 1 < len(board):
                if board[i][j] == board[i][j + 1]:
                    score += board[i][j]
            if i - 1 >= 0:
                if board[i][j] == board[i - 1][j]:
                    score += board[i][j]
            if j - 1 >= 0:
                if board[i][j] == board[i][j - 1]:
                    score += board[i][j]
    return score


x = Board()
x.display_board()


def play_game(x):
    while x.check_alive:
        max = -1
        move = ""
        left_move = x.move_left(active=False)
        right_move = x.move_right(active=False)
        up_move = x.move_up(active=False)
        down_move = x.move_down(active=False)
        if left_move[0] and score_board(left_move[3]) >= max:
            max = score_board(left_move[3])
            move = "left"
        if up_move[0] and score_board(up_move[3]) >= max:
            max = score_board(left_move[3])
            move = "up"
        if right_move[0] and score_board(right_move[3]) >= max:
            max = score_board(left_move[3])
            move = "right"
        if down_move[0] and score_board(down_move[3]) >= max:
            max = score_board(left_move[3])
            move = "down"
        if not (left_move[0] or right_move[0] or up_move[0] or down_move[0]):
            break
        else:
            x.play_move(move)


def explore_moves(x, board, depth):
    left_move = x.test_left(board)
    right_move = x.test_right(board)
    up_move = x.test_up(board)
    down_move = x.test_down(board)
    best =-1
    move = ""
    possible=False
    if left_move[0]:
        if depth == 0:
            if left_move[1] > best and left_move[0]:
                best = left_move[1]
                move = "left"
                possible = left_move[0]
        else:
            left_sol = explore_moves(x, left_move[2], depth - 1)
            if left_sol[0] + left_move[1]*1.2 > best and left_sol[2]:
                best = left_sol[0] + left_move[1]*1.2
                move = "left"
                possible = left_move[0]
    if right_move[0]:
        if depth == 0:
            if right_move[1] > best and right_move[0]:
                best = right_move[1]
                move = "right"
                possible = right_move[0]
        else:
            right_sol = explore_moves(x, right_move[2], depth - 1)
            if right_sol[0] + right_move[1]*1.2 > best and right_sol[2]:
                best = right_sol[0] + right_move[1]*1.2
                move = "right"
                possible = right_move[0]
    if up_move[0]:
        if depth == 0:
            if up_move[1] > best and up_move[0]:
                best = up_move[1]
                move = "up"
                possible = up_move[0]
        else:
            up_sol = explore_moves(x, up_move[2], depth - 1)
            if up_sol[0] + up_move[1]*1.2 > best and up_move[2]:
                best = up_sol[0] + up_move[1]*1.2
                move = "up"
                possible = up_move[0]
    if down_move[0]:
        if depth == 0:
            if down_move[1] > best and down_move[0]:
                best = down_move[1]
                move = "down"
                possible = down_move[0]
        else:
            down_sol = explore_moves(x, down_move[2], depth - 1)
            if down_sol[0] + down_move[1]*1.2 > best and down_sol[2]:
                best = down_sol[0] + down_move[1]*1.2
                move = "down"
                possible = down_move[0]
    return best,move, possible




def advanced_player(x):
    while x.check_alive:
        max = -1
        move = ""
        left_move = x.move_left(active=False)
        right_move = x.move_right(active=False)
        up_move = x.move_up(active=False)
        down_move = x.move_down(active=False)
        if left_move[0] and score_board(left_move[3]) >= max:
            max = score_board(left_move[3])
            move = "left"
        if up_move[0] and score_board(up_move[3]) >= max:
            max = score_board(left_move[3])
            move = "up"
        if right_move[0] and score_board(right_move[3]) >= max:
            max = score_board(left_move[3])
            move = "right"
        if down_move[0] and score_board(down_move[3]) >= max:
            max = score_board(left_move[3])
            move = "down"
        if not (left_move[0] or right_move[0] or up_move[0] or down_move[0]):
            break
        else:
            x.play_move(move)

def player(x):
    move_list=['left','right','up','down']
    while x.check_alive():
        board_now = x.copy_board()
        result = explore_moves(x, board_now, 3)
        x.play_move(result[1])




board = Board()
scores = []
high_tile = []
for _ in range(100):
    board.new_game()
    player(board)
    scores.append(board.get_score())
    high_tile.append(board.max_tile())

print(scores)
print(max(scores), min(scores), sum(scores) / len(scores))
print(high_tile)
print(max(high_tile), min(high_tile), sum(high_tile) / len(high_tile))
