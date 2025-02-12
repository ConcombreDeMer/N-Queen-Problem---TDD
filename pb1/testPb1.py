import unittest
from solverPb1 import solve_n_queens

class TestNQueens(unittest.TestCase):
    def test_no_solution(self):
        self.assertEqual(solve_n_queens(2), [])
        self.assertEqual(solve_n_queens(3), [])
    
    def test_one_solution(self):
        self.assertEqual(solve_n_queens(4), [[0, 2, 3, 1]])
        
if __name__ == '__main__':
    unittest.main()