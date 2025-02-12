import unittest
from solver import solve_n_queen_pairs

class TestSolver(unittest.TestCase):
    def test_minimal_board(self):
        self.assertEqual(solve_n_queen_pairs(2), [], "Aucune solution possible pour un échiquier 2x2")

def test_validate_positions():
    solutions = solve_n_queen_pairs(4)
    assert solutions == [], "Aucune solution valide n'est attendue pour cette configuration"

def test_is_valid_pair_basic():
    from solver import is_valid_pair
    assert is_valid_pair((0, 0), (1, 1)) == True, "Les reines doivent s'attaquer (diagonale)"




if __name__ == '__main__':
    unittest.main()