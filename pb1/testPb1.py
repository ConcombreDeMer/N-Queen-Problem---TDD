import unittest
from solverPb1 import solve_n_queens, display_board

class TestNQueens(unittest.TestCase):
    def test_no_solution(self):
        self.assertEqual(solve_n_queens(2), [])
        self.assertEqual(solve_n_queens(3), [])
    
    def test_multiple_solutions(self):
        expected = [
            [
                ['Q', '.', '.', '.'],
                ['.', '.', 'Q', '.'],
                ['.', '.', '.', 'Q'],
                ['.', 'Q', '.', '.']
            ],
            [
                ['.', 'Q', '.', '.'],
                ['Q', '.', '.', '.'],
                ['.', '.', 'Q', '.'],
                ['.', '.', '.', 'Q']
            ]
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

    def test_solution_count(self):
        solution_5 = solve_n_queens(5)
        self.assertGreater(len(solution_5), 0)  

    def test_solution_count_large(self):
        solution_6 = solve_n_queens(6)
        solution_7 = solve_n_queens(7)
        self.assertGreater(len(solution_6), 0)
        self.assertGreater(len(solution_7), 0)
        
if __name__ == '__main__':
    unittest.main()