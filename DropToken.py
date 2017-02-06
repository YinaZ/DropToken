import sys
import logging

def main():
    """
    main function, creates a DropToken instance,
    read input from command line and call inputProcess(line)
    in DropToken class to process input line by line
    continue reading input till there is no next line,
    keyboard interrupts the program, or inputProcess(line) returns False
    """
    dt = DropToken()
    play = True
    while play:
        try:
            line = sys.stdin.readline()
        except KeyboardInterrupt:
            break
        if not line:
            break
        play = dt.inputProcess(line)

class DropToken:
    def __init__(self):
        # size of each side of the board
        self.size = 4
        # score for each column
        self.columnScore = [0] * self.size
        # score for each row
        self.rowScore = [0] * self.size
        # history for put commands
        self.history = []
        # spots left in given row
        self.occupied = [0] * self.size
        # score for diagonal from top left to bottom right
        self.diagonal = 0
        # score for diagonal from bottom left to top right
        self.antidiagonal = 0
        # size * size narray keeping track of board, initialized to all 0s
        self.board = [[0] * self.size for i in range(self.size)]
        # whether a player has won already
        self.won = False
        
    def inputProcess(self, line):
        """
        A function that takes into a string of commmand,
        call corresponding functions according to the command,
        and print messages if the input is not valid.
        
        Args:
            line: a string with command (PUT <column>, GET, BOARD and EXIT)
        Returns:
            False if EXIT is the command, otherse True
        """
        fields = line.split()
        # check if input argument size is not 1 or 2
        if len(fields) < 1 or len(fields) > 2:
            print 'Invalid input size!'
            return True
        # call corresponding functions based on input argument(s)
        if fields[0] == 'GET':
            res = self.get()
            if res != '':
                print res,
        elif fields[0] == 'EXIT':
            return False
        elif fields[0] == 'BOARD':
            print self.displayBoard()
        elif fields[0] == 'PUT':
            if len(fields) != 2:
                print 'PUT command needs one argument!'
                return True
            try:
                column = int(fields[1])
                if column < 1 or column > 4:
                    print 'Column number for PUT command needs to be from 1 to 4'
                else:
                    print self.put(column)
            except ValueError:
                print 'Invalid input, for column number please enter an integer from 1 to 4'
        else:
            print 'Invalid input, valid commands consists of GET BOARD EXIT PUT <column> only'
        return True

    def displayBoard(self):
        """
        A function that returns the string representation
        of the current board
        Returns:
            A string representing the board
        """
        res = ''
        for i in range(0, self.size):
            res += '|'
            for j in range(0, self.size):
                res += ' ' + str(self.board[i][j])
            res += '\n'
        res += '+'
        for i in range(0, self.size * 2):
            res += '-'
        res += '\n '
        for i in range(1, (self.size + 1)):
            res += (' ' + str(i))
        return res
    
    def get(self):
        """
        A function that returns the past columns of PUT commands
        Returns:
            A list of column numbers
        """
        res = ''
        for hist in self.history:
            res += (str(hist) + '\n')
        return res
    
    def put(self, column):
        """
        A function that returns "OK" if given column still has spot(s),
        "WIN" if one of the player wins, "DRAW" if board is full and
        nobody wins, and "ERR"R" if given column is full or someone
        has won already
        Returns:
            A string of result ("OK", "WIN", "DRAW" or "ERROR")
        """
        column -= 1
        if self.occupied[column] >= 4 or self.won:
            return 'ERROR'
        self.history.append(column + 1)
        row = self.occupied[column]
        # assign 1 to player 1, and -1 to player 2
        if len(self.history) % 2 == 1:
            player = 1
            self.board[3 - row][column] = 1
        else:
            player = -1
            self.board[3 - row][column] = 2
        # add player score to column, row and diagonal scores
        self.columnScore[column] += player
        self.rowScore[row] += player
        self.occupied[column] += 1;
        if column == row:
            self.diagonal += player
        if column + row == 3:
            self.antidiagonal += player
        # check column, row and diagonal scores
        # if absolute value of one of them is 4
        # which means the original value is either 4 or -4
        # and one of the player has occupied all 4 of them
        # which means the player has won in that row/column/diagonal
        # and thus return "WIN"
        if (abs(self.rowScore[row]) == 4 or abs(self.columnScore[column]) == 4
            or abs(self.diagonal) == 4 or abs(self.antidiagonal) == 4):
            self.won = True
            return 'WIN'
        # check if there is still non-full columns
        # in other words check if the board is full
        for i in range(0, self.size):
            # if board is not full return "OK"
            if self.occupied[i] < 4:
                return 'OK'
        # if the board is full, return "DRAW"
        return 'DRAW'

if __name__ == "__main__":
    main()
