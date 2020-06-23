from game import Board
from random import randint

x=Board()
x.display_board()


move_list=['left','right','up','down']
for _ in range(10):
    move=move_list[randint(0,3)]
    x.play_move(move)
    x.display_board()


test=x.copy_board()

result=x.test_down(test)
print(result)
result=x.test_up(test)
print(result)
result=x.test_left(test)
print(result)
result=x.test_right(test)
print(result)
