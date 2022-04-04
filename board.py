import random
class Board():
    def __init__(self):
        self.x_moves = []
        self.o_moves = []
        self.all_moves = []
        self.rows = [['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]
        self.all_possible_moves = [[row, col] for row in range(1, 4) for col in range(1, 4)]


    def occupied(self, row, col):
        for move in self.all_moves:
            if move == [row, col]:
                return True


    def add_move(self, row_input, column_input):
        #if it's not yet occupied, add else, print a message
            row = row_input
            column = column_input
            self.x_moves.append([row, column])
            self.all_moves.append([row, column])



    def computer_move(self):
        self.current_possible_moves = [move for move in self.all_possible_moves if move not in self.all_moves]
        if self.current_possible_moves == []:
            print('No moves left. Draw')
            return True
        else:
            pick = random.choice(self.current_possible_moves)
            self.o_moves.append([pick[0], pick[1]])
            self.all_moves.append([pick[0], pick[1]])
            # print(f'current possible moves: {self.current_possible_moves}')
            # print(f'all moves {self.all_moves}')
            # print(pick)


    def player_wins(self, player_marker):
        print(f'Player {player_marker} wins')
        return True

    def win(self):
        for row in self.rows:
            #check each row
            row_pattern= ''.join(row)
            if row_pattern == 'XXX':
                return self.player_wins('X')
            elif row_pattern == 'OOO':
                return self.player_wins('O')

            col_pattern = ''
            for i in range(3):
                for row in self.rows:
                    col_pattern += row[i]
                    if col_pattern == 'OOO':
                        return self.player_wins('O')
                    elif col_pattern == 'XXX':
                        return self.player_wins('X')

                col_pattern = ''

        #check diagnonals
        diagonal_1 = self.rows[0][0] + self.rows[1][1] + self.rows[2][2]
        diagonal_2 = self.rows[2][0] + self.rows[1][1] + self.rows[0][2]

        if diagonal_1 == 'XXX' or diagonal_2 == 'XXX':
            return self.player_wins('X')

        if diagonal_1 == 'OOO' or diagonal_2 == '000':
            return self.player_wins('O')

        if self.current_possible_moves == []:
            print('No moves left. Draw')
            return True



    def render_board(self):
        self.formatted_rows = [['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]
        for move in self.x_moves:
            self.rows[move[0]-1][move[1] -1] ='X'
            self.formatted_rows[move[0]-1][move[1] -1] = ' ' + 'X' + ' '

        for move in self.o_moves:
            self.rows[move[0]-1][move[1] -1] ='O'
            self.formatted_rows[move[0]-1][move[1] -1] = ' ' + 'O' +' '

        for row in self.formatted_rows:
            row.insert(1, '|')
            row.insert(3,'|')
            formatted_row_output = ''.join(row)
            print(formatted_row_output)
            print('-----------')