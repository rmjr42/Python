# test_tic_tac_toe.py

import unittest
from TicTacToe import updateBoard, winnerHorizontal, winnerVertical, winnerDiagonal, validateMove, winner

class TestTicTacToe(unittest.TestCase):
    
    def setUp(self):
        self.board = [['']*3 for _ in range(3)]
    
    def test_updateBoard(self):
        updateBoard(self.board, '0', '0', 'X')
        self.assertEqual(self.board[0][0], 'X')
        updateBoard(self.board, '1', '1', 'O')
        self.assertEqual(self.board[1][1], 'O')
    
    def test_winnerHorizontal(self):
        self.board[0] = ['X', 'X', 'X']
        self.assertTrue(winnerHorizontal(self.board))
        self.board[0] = ['', '', '']
        self.assertFalse(winnerHorizontal(self.board))
    
    def test_winnerVertical(self):
        self.board[0][0] = 'X'
        self.board[1][0] = 'X'
        self.board[2][0] = 'X'
        self.assertTrue(winnerVertical(self.board))
        self.board[0][0] = ''
        self.board[1][0] = ''
        self.board[2][0] = ''
        self.assertFalse(winnerVertical(self.board))
    
    def test_winnerDiagonal(self):
        self.board[0][0] = 'X'
        self.board[1][1] = 'X'
        self.board[2][2] = 'X'
        self.assertTrue(winnerDiagonal(self.board))
        self.board[0][0] = ''
        self.board[1][1] = ''
        self.board[2][2] = ''
        self.assertFalse(winnerDiagonal(self.board))
        self.board[0][2] = 'O'
        self.board[1][1] = 'O'
        self.board[2][0] = 'O'
        self.assertTrue(winnerDiagonal(self.board))
        self.board[0][2] = ''
        self.board[1][1] = ''
        self.board[2][0] = ''
        self.assertFalse(winnerDiagonal(self.board))
    
    def test_validateMove(self):
        self.assertTrue(validateMove(self.board, '0', '0'))
        self.board[0][0] = 'X'
        self.assertFalse(validateMove(self.board, '0', '0'))
        self.assertFalse(validateMove(self.board, '3', '3'))
        self.assertFalse(validateMove(self.board, '-1', '0'))
        self.assertFalse(validateMove(self.board, '1', 'a'))
    
    def test_winner(self):
        self.board[0] = ['X', 'X', 'X']
        self.assertTrue(winner(self.board))
        self.board[0] = ['', '', '']
        self.board[0][0] = 'X'
        self.board[1][0] = 'X'
        self.board[2][0] = 'X'
        self.assertTrue(winner(self.board))
        self.board[0][0] = ''
        self.board[1][0] = ''
        self.board[2][0] = ''
        self.board[0][0] = 'X'
        self.board[1][1] = 'X'
        self.board[2][2] = 'X'
        self.assertTrue(winner(self.board))
        self.board[0][0] = ''
        self.board[1][1] = ''
        self.board[2][2] = ''
        self.assertFalse(winner(self.board))

if __name__ == '__main__':
    unittest.main()



