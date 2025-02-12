import unittest
from solver import solve_n_queen_pairs

class TestSolver(unittest.TestCase):
    def test_minimal_board(self):
        self.assertEqual(solve_n_queen_pairs(2), [], "Aucune solution possible pour un échiquier 2x2")

if __name__ == '__main__':
    unittest.main()