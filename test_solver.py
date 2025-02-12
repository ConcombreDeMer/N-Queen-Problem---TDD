import unittest
from solver import solve_n_queen_pairs, find_valid_configurations, is_valid_pair

class TestSolver(unittest.TestCase):
    def test_minimal_board(self):
        self.assertEqual(solve_n_queen_pairs(2), [], "Aucune solution possible pour un échiquier 2x2")

    def test_find_valid_configurations_4x4(self):
        configs = find_valid_configurations(4)
        self.assertIsInstance(configs, list, "Le résultat doit être une liste")
        if configs:
            for config in configs:
                self.assertIsInstance(config, list, "Chaque configuration doit être une liste")
                self.assertEqual(len(config), 4, "Chaque ligne doit avoir 4 caractères")
                self.assertTrue(all(len(row) == 4 for row in config), 
                              "Toutes les lignes doivent avoir la même longueur")

    def test_valid_configuration_pattern(self):
        configs = find_valid_configurations(4)
        if not configs:
            self.fail("Au moins une configuration valide devrait être trouvée")
        
        all_queen_counts = [sum(row.count('O') for row in config.split('\n')) for config in configs]
        # Vérifie que toutes les configurations ont le même nombre de reines (maximum)
        self.assertEqual(len(set(all_queen_counts)), 1, 
                        "Toutes les configurations doivent avoir le même nombre maximum de reines")
        
        for config in configs:
            # Extraction des positions des reines
            lines = config.split('\n')
            queens = [(i, j) for i, row in enumerate(lines) 
                     for j, cell in enumerate(row) if cell == 'O']
            
            # Vérification des paires
            pairs_found = []
            for i, q1 in enumerate(queens):
                pair_found = False
                for q2 in queens[i+1:]:
                    if is_valid_pair(q1, q2):
                        pairs_found.append((q1, q2))
                        pair_found = True
                self.assertTrue(pair_found, f"La reine en {q1} doit avoir une paire")
            
            # Vérification que chaque reine n'apparaît que dans une seule paire
            queens_in_pairs = [q for pair in pairs_found for q in pair]
            for queen in queens:
                self.assertEqual(queens_in_pairs.count(queen), 1, 
                               f"La reine en {queen} doit apparaître dans exactement une paire")

    def test_maximum_queens(self):
        """Test que les configurations trouvées ont le nombre maximum possible de reines"""
        configs = find_valid_configurations(4)
        if configs:
            queen_count = sum(configs[0].count('O'))
            # Pour n=4, on s'attend à avoir au moins 4 reines (2 paires)
            self.assertGreaterEqual(queen_count, 4, 
                                  "Il devrait y avoir au moins 4 reines pour un tableau 4x4")

    def test_solution_format(self):
        configs = find_valid_configurations(4)
        if configs:
            first_solution = configs[0]
            self.assertIn('\n', first_solution, "La solution doit contenir des retours à la ligne")
            lines = first_solution.split('\n')
            self.assertEqual(len(lines), 4, "Le tableau doit avoir 4 lignes")
            for line in lines:
                self.assertEqual(len(line), 4, "Chaque ligne doit avoir 4 caractères")

def test_validate_positions():
    solutions = solve_n_queen_pairs(4)
    assert solutions == [], "Aucune solution valide n'est attendue pour cette configuration"

def test_is_valid_pair_basic():
    from solver import is_valid_pair
    assert is_valid_pair((0, 0), (1, 1)) == True, "Les reines doivent s'attaquer (diagonale)"
    assert is_valid_pair((0, 0), (0, 1)) == True, "Les reines doivent s'attaquer (ligne)"
    assert is_valid_pair((0, 0), (1, 0)) == True, "Les reines doivent s'attaquer (colonne)"
    assert is_valid_pair((0, 0), (1, 2)) == False, "Les reines ne doivent pas s'attaquer"

if __name__ == '__main__':
    unittest.main()