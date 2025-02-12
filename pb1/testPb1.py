import unittest
from solverPb1 import solve_n_queens, display_board

class TestNQueens(unittest.TestCase):
    def test_no_solution(self):
        self.assertEqual(solve_n_queens(2), [])
        self.assertEqual(solve_n_queens(3), [])
    
    def test_one_solution(self):
        expected = [
            ['Q', '.', '.', '.'],
            ['.', '.', 'Q', '.'],
            ['.', '.', '.', 'Q'],
            ['.', 'Q', '.', '.']
        ]
        result = solve_n_queens(4)
        self.assertEqual(result, expected)

    def test_display_board(self):
        solution = [0, 2, 3, 1]
        expected = [
            ['Q', '.', '.', '.'],
            ['.', '.', 'Q', '.'],
            ['.', '.', '.', 'Q'],
            ['.', 'Q', '.', '.']
        ]
        self.assertEqual(display_board(solution), expected)
        
if __name__ == '__main__':
    unittest.main()