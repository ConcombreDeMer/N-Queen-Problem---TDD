import unittest
from solverPb1 import solve_n_queens, display_board

class TestNQueens(unittest.TestCase):
    
    def test_no_solution(self):
        """
        Teste les cas où il n'y a pas de solution (n=2 et n=3).
        """
        self.assertEqual(solve_n_queens(2), [])
        self.assertEqual(solve_n_queens(3), [])
    
    def test_multiple_solutions(self):
        """
        Teste les cas où il y a plusieurs solutions (n=4).
        """
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
    
    def test_solution_count(self):
        """
        Teste que la fonction retourne des solutions pour n = 5.
        """
        solution_5 = solve_n_queens(5)
        self.assertGreater(len(solution_5), 0)
    
    def test_solution_count_large(self):
        """
        Vérifie qu'il y a des solutions pour n = 6 et n = 7.
        """
        solution_6 = solve_n_queens(6)
        solution_7 = solve_n_queens(7)
        self.assertGreater(len(solution_6), 0)
        self.assertGreater(len(solution_7), 0)

    def test_display_board(self):
        """
        Teste l'affichage d'un échiquier pour une solution donnée.
        """
        solution = [0, 2, 3, 1]
        expected = [
            ['Q', '.', '.', '.'],
            ['.', '.', 'Q', '.'],
            ['.', '.', '.', 'Q'],
            ['.', 'Q', '.', '.']
        ]
        self.assertEqual(display_board(solution), expected)

    def test_display_multiple_solutions(self):
        """
        Teste l'affichage de plusieurs solutions pour n = 5.
        """
        solutions = solve_n_queens(5)
        self.assertGreater(len(solutions), 0)
        for solution in solutions:
            self.assertEqual(len(solution), 5)
            self.assertTrue(all(len(row) == 5 for row in solution)) 

    def test_display_board_6(self):
        """
        Teste l'affichage d'une solution pour n = 6.
        """
        solution = solve_n_queens(6)[0]
        self.assertEqual(len(solution), 6)
        self.assertTrue(all(len(row) == 6 for row in solution))
        
        self.assertTrue(all(row.count('Q') == 1 for row in solution))
        
        columns = [[row[i] for row in solution] for i in range(6)]
        self.assertTrue(all(col.count('Q') == 1 for col in columns))
        
        queens_pos = []
        for i in range(6):
            for j in range(6):
                if solution[i][j] == 'Q':
                    queens_pos.append((i, j))
        
        for i, (r1, c1) in enumerate(queens_pos):
            for r2, c2 in queens_pos[i+1:]:
                self.assertFalse(abs(r1 - r2) == abs(c1 - c2))

if __name__ == '__main__':
    unittest.main()
