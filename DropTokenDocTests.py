import os
from DropToken import DropToken
"""
This test module tests whether inputProcess function in DropToken class
works as documented.
Lines prefixed with >>> indicate input to input_test. If the input consists
of multiple commands, they are seperated by ','
The line(s) below a user input line until the next line prefixed with >>>
indicate(s) output from the program.

Examples:
>>> input_test("PUT 1")
OK

>>> input_test("PUT 1,PUT 2,GET")
OK
OK
1
2
>>>
"""
def input_test(input_str):
    """
    Check if input is handled correctly and corresponding output
    are printed correctly by input_Process() function in DropToken

    # Test when input argument size is larger than 2
    >>> input_test("PUT BOARD 1")
    Invalid input size!
    >>>

    # Test when input argument size is smaller
    # than 1 (0 in other words)
    >>> input_test("")
    Invalid input size!
    >>>

    # Test when input is not valid command
    # and argument size is 1
    >>> input_test("A")
    Invalid input, valid commands consists of GET BOARD EXIT PUT <column> only
    >>>

    # Test when input is not valid command
    # and argument size is 2
    >>> input_test("A B")
    Invalid input, valid commands consists of GET BOARD EXIT PUT <column> only
    >>>

    # Test when PUT is called but
    # no argument for column is passed in
    >>> input_test("PUT")
    PUT command needs one argument!
    >>>

    # Test when PUT is called but
    # column argument is not an integer
    >>> input_test("PUT A")
    Invalid input, for column number please enter an integer from 1 to 4
    >>>

    # Test when PUT is called but
    # column integer argument is larger than 4
    >>> input_test("PUT 5")
    Column number for PUT command needs to be from 1 to 4
    >>>

    # Test when PUT is called but
    # column integer argument is smaller than 1
    >>> input_test("PUT 0")
    Column number for PUT command needs to be from 1 to 4
    >>>

    # Test when PUT command is valid
    >>> input_test("PUT 1")
    OK
    >>>

    # Test when PUT command is called and a player wins
    >>> input_test("PUT 1,PUT 2,PUT 1,PUT 2,PUT 1,PUT 2,PUT 1")
    OK
    OK
    OK
    OK
    OK
    OK
    WIN
    >>>
    
    # Test when PUT command is called and players draw
    >>> input_test("PUT 1,PUT 2,PUT 1,PUT 2,PUT 1,PUT 2,PUT 2,PUT 1,PUT 3,PUT 4,PUT 3,PUT 4,PUT 3,PUT 4,PUT 4,PUT 3")
    OK
    OK
    OK
    OK
    OK
    OK
    OK
    OK
    OK
    OK
    OK
    OK
    OK
    OK
    OK
    DRAW
    >>>
    
    # Test when PUT command is called after a WIN
    # (and the column it tries to put is not full yet)
    >>> input_test("PUT 1,PUT 2,PUT 1,PUT 2,PUT 1,PUT 2,PUT 1,PUT 4")
    OK
    OK
    OK
    OK
    OK
    OK
    WIN
    ERROR
    >>>
    
    # Test when input consists of five PUT commands for the same column
    # in other words, test when PUT command tries to put to a column
    # that is full already
    >>> input_test("PUT 1,PUT 1,PUT 1,PUT 1,PUT 1")
    OK
    OK
    OK
    OK
    ERROR
    >>>
    
    # Test when BOARD command is called
    >>> input_test("BOARD")
    | 0 0 0 0
    | 0 0 0 0
    | 0 0 0 0
    | 0 0 0 0
    +--------
      1 2 3 4
    >>>
    
    # Test when GET command is called for an empty BOARD
    >>> input_test("GET")

    # Test when GET command is called for a non-empty BOARD
    >>> input_test("PUT 1,PUT 4,PUT 2,PUT 3,GET")
    OK
    OK
    OK
    OK
    1
    4
    2
    3

    # Test when EXIT is called
    >>> input_test("EXIT")

    # Test of a full game
    >>> input_test("GET,BOARD,PUT 1,PUT 4,PUT 2,PUT 3,BOARD,PUT 1,PUT 1,PUT 1,PUT 1,BOARD,PUT 3,PUT 2,PUT 3,PUT 2,PUT 3,BOARD,GET")
    | 0 0 0 0
    | 0 0 0 0
    | 0 0 0 0
    | 0 0 0 0
    +--------
      1 2 3 4
    OK
    OK
    OK
    OK
    | 0 0 0 0
    | 0 0 0 0
    | 0 0 0 0
    | 1 1 2 2
    +--------
      1 2 3 4
    OK
    OK
    OK
    ERROR
    | 1 0 0 0
    | 2 0 0 0
    | 1 0 0 0
    | 1 1 2 2
    +--------
      1 2 3 4
    OK
    OK
    OK
    OK
    WIN
    | 1 0 2 0
    | 2 1 2 0
    | 1 1 2 0
    | 1 1 2 2
    +--------
      1 2 3 4
    1
    4
    2
    3
    1
    1
    1
    3
    2
    3
    2
    3
    """
    dt = DropToken()
    for line in input_str.split(','):
        dt.inputProcess(line)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
