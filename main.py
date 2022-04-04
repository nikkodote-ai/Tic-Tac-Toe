from logo import art
from board import Board
from player import Player

print(art)
board = Board()

continue_game = True

while continue_game:
    row = int(input('Row:'))
    col = int(input('Column:'))
    try:
        if board.occupied(row, col):
            print('Already Occupied. Try Again')
        else:
            board.add_move(row,col)
            board.computer_move()


            board.render_board()
            if board.win():
                continue_game = False

    except IndexError:
            print('Only type 1-3')
