import unittest
from DropToken import DropToken
"""
This test module tests if functions in DropToken class (except inputProcess)
works as documented.
"""
class DropTokenTestCase(unittest.TestCase):
    def setUp(self):
        self.dt = DropToken()

    def tearDown(self):
        self.dt = None
        
    def populateBoard(self):
        """
        populate a board till it is full and return
        the output of the last put() call
        """        
        dt = self.dt
        dt.put(1)
        dt.put(2)
        dt.put(3)
        dt.put(4)
        dt.put(4)
        dt.put(3)
        dt.put(2)
        dt.put(1)
        dt.put(1)
        dt.put(2)
        dt.put(3)
        dt.put(4)
        dt.put(1)
        dt.put(2)
        dt.put(3)
        return dt.put(4)

    def test_PUT_OK_when_column_is_not_full(self):
        """ test if put() will return OK when the given column is not full """
        dt = self.dt
        self.assertEqual(
            dt.put(1), 'OK',
            'put() should return OK when given column is not full')
        self.assertEqual(
            dt.put(1), 'OK',
            'put() should return OK when given column is not full')
        self.assertEqual(
            dt.put(1), 'OK',
            'put() should return OK when given column is not full')
        self.assertEqual(
            dt.put(1), 'OK',
            'put() should return OK when given column is not full')

    def test_PUT_ERROR_when_column_is_full(self):
        """ test if put() will return ERROR when the given column is full """
        dt = self.dt
        dt.put(1)
        dt.put(1)
        dt.put(1)
        dt.put(1)
        self.assertEqual(
            dt.put(1), 'ERROR',
            'put() should return ERROR when given column is full')

    def test_PUT_DRAW(self):
        """ test if put() will return DRAW when board is full and no one wins"""
        self.assertEqual(
            self.populateBoard(), 'DRAW',
            'put() should return DRAW when board is full')

    def test_PUT_player1_WIN_in_a_row(self):
        """ test if put() will return WIN when player 1 wins in a row"""
        dt = self.dt
        dt.put(1)
        dt.put(1)
        dt.put(2)
        dt.put(2)
        dt.put(3)
        dt.put(3)
        self.assertEqual(
            dt.put(4), 'WIN',
            'put() should return WIN when a player wins')

    def test_PUT_player2_WIN_in_a_row(self):
        """ test if put() will return WIN when player 2 wins in a row"""
        dt = self.dt
        dt.put(1)
        dt.put(1)
        dt.put(2)
        dt.put(2)
        dt.put(3)
        dt.put(3)
        dt.put(1)
        dt.put(4)
        dt.put(3)
        self.assertEqual(
            dt.put(4), 'WIN',
            'put() should return WIN when a player wins')

    def test_PUT_player1_WIN_in_a_column(self):
        """ test if put() will return WIN when player 1 wins in a column"""
        dt = self.dt
        dt.put(1)
        dt.put(2)
        dt.put(1)
        dt.put(2)
        dt.put(1)
        dt.put(2)
        self.assertEqual(
            dt.put(1), 'WIN',
            'put() should return WIN when a player wins')
        
    def test_PUT_player2_WIN_in_a_column(self):
        """ test if put() will return WIN when player 2 wins in a column"""
        dt = self.dt
        dt.put(1)
        dt.put(2)
        dt.put(1)
        dt.put(2)
        dt.put(1)
        dt.put(2)
        dt.put(3)
        self.assertEqual(
            dt.put(2), 'WIN',
            'put() should return WIN when a player wins')

    def test_PUT_player1_WIN_in_a_diagonal(self):
        """
        test if put() will return WIN
        when player 1 wins in a diagonal from top left to bottom right
        """
        dt = self.dt
        dt.put(2)
        dt.put(1)
        dt.put(4)
        dt.put(3)
        dt.put(3)
        dt.put(4)
        dt.put(1)
        dt.put(2)
        dt.put(2)
        dt.put(1)
        dt.put(4)
        dt.put(3)
        self.assertEqual(
            dt.put(1), 'WIN',
            'put() should return WIN when a player wins')

    def test_PUT_player2_WIN_in_a_diagonal(self):
        """
        test if put() will return WIN
        when player 2 wins in a diagonal from top left to bottom right
        """
        dt = self.dt
        dt.put(1)
        dt.put(2)
        dt.put(3)
        dt.put(4)
        dt.put(4)
        dt.put(3)
        dt.put(2)
        dt.put(1)
        dt.put(1)
        dt.put(2)
        dt.put(3)
        dt.put(4)
        dt.put(2)
        self.assertEqual(
            dt.put(1), 'WIN',
            'put() should return WIN when a player wins')

    def test_PUT_player1_WIN_in_an_antidiagonal(self):
        """
        test if put() will return WIN
        when player 1 wins in a diagonal from bottom left to top right
        """
        dt = self.dt
        dt.put(1)
        dt.put(2)
        dt.put(2)
        dt.put(3)
        dt.put(3)
        dt.put(4)
        dt.put(3)
        dt.put(4)
        dt.put(4)
        dt.put(3)
        self.assertEqual(
            dt.put(4), 'WIN',
            'put() should return WIN when a player wins')

    def test_PUT_player2_WIN_in_an_antidiagonal(self):
        """
        test if put() will return WIN
        when player 2 wins in a diagonal from bottom left to top right
        """
        dt = self.dt
        dt.put(2)
        dt.put(1)
        dt.put(3)
        dt.put(2)
        dt.put(4)
        dt.put(3)
        dt.put(4)
        dt.put(3)
        dt.put(3)
        dt.put(4)
        dt.put(1)
        self.assertEqual(
            dt.put(4), 'WIN',
            'put() should return WIN when a player wins')
        
    def test_PUT_WIN_when_board_is_full(self):
        """
        test if put() will return WIN
        when board is full and a player wins
        """
        dt = self.dt
        dt.put(1)
        dt.put(2)
        dt.put(3)
        dt.put(4)
        dt.put(4)
        dt.put(3)
        dt.put(2)
        dt.put(1)
        dt.put(1)
        dt.put(2)
        dt.put(3)
        dt.put(4)
        dt.put(2)
        dt.put(4)
        dt.put(3)
        self.assertEqual(
            dt.put(1), 'WIN',
            'put() should return WIN when a player wins')
        
    def test_PUT_ERROR_after_WIN(self):
        """ test if put() will return ERROR after a WIN"""
        dt = self.dt
        dt.put(1)
        dt.put(2)
        dt.put(1)
        dt.put(2)
        dt.put(1)
        dt.put(2)
        self.assertEqual(
            dt.put(1), 'WIN',
            'put() should return WIN when a player wins')
        self.assertEqual(
            dt.put(2), 'ERROR',
            'put() should return ERROR after a player has won already')
        
    def test_GET_empty_board(self):
        """test if get() returns empty string when board is empty """
        self.assertEqual(
            self.dt.get(), '',
            'get() should return an empty string when board is empty')
        
    def test_GET_non_empty_board(self):
        """
        test if get() returns past PUT histories as expected
        when board is not empty
        """
        self.dt.put(1)
        self.dt.put(2)
        self.assertEqual(
            self.dt.get(), '1\n2\n',
            'get() should return past PUT histories when board is not empty')

    def test_GET_full_board(self):
        """
        test if get() returns past PUT histories as expected
        when board is full
        """
        self.populateBoard()
        self.assertEqual(
            self.dt.get(), '1\n2\n3\n4\n4\n3\n2\n1\n1\n2\n3\n4\n1\n2\n3\n4\n',
            'get() should return past PUT histories when board is not empty')

    def test_BOARD_empty_board(self):
        """
        test if displayBoard() returns an initialized board
        when board is empty
        """
        emptyBoard = '| 0 0 0 0\n| 0 0 0 0\n| 0 0 0 0\n| 0 0 0 0\n'
        emptyBoard += '+--------\n  1 2 3 4'
        self.assertEqual(
            emptyBoard, self.dt.displayBoard(),
            'displayBoard() should return an intialized empty board')
        
    def test_BOARD_non_empty_board(self):
        """
        test if displayBoard() returns a valid board as expected
        based on past PUT histories when board is not empty
        """
        self.dt.put(1)
        self.dt.put(2)
        board = '| 0 0 0 0\n| 0 0 0 0\n| 0 0 0 0\n| 1 2 0 0\n'
        board += '+--------\n  1 2 3 4'
        self.assertEqual(
            board, self.dt.displayBoard(),
            'displayBoard() should return a board based on past PUT histories')
        
    def test_BOARD_full_board(self):
        """
        test if displayBoard() returns a valid board as expected
        based on past PUT histories when board is full
        """
        self.populateBoard()
        board = '| 1 2 1 2\n| 1 2 1 2\n| 2 1 2 1\n| 1 2 1 2\n'
        board += '+--------\n  1 2 3 4'
        self.assertEqual(
            board, self.dt.displayBoard(),
            'displayBoard() should return a board based on past PUT histories')
        
if __name__ == '__main__':
    unittest.main()
