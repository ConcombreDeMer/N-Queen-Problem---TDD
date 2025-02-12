import unittest
from solver import solve_n_queen_pairs

class TestSolver(unittest.TestCase):
    def test_minimal_board(self):
        self.assertEqual(solve_n_queen_pairs(2), [], "Aucune solution possible pour un échiquier 2x2")

def test_validate_positions():
    solutions = solve_n_queen_pairs(4)
    assert solutions == [], "Aucune solution valide n'est attendue pour cette configuration"


if __name__ == '__main__':
    unittest.main()