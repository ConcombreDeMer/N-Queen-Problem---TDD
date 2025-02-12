def solve_n_queen_pairs(n):
    if n < 4:
        return []
    positions = [(i, j) for i in range(n) for j in range(n)]
    threatening_pairs = []
    for i, queen1 in enumerate(positions):
        for queen2 in positions[i+1:]:
            if is_valid_pair(queen1, queen2):
                threatening_pairs.append((queen1, queen2))
    return threatening_pairs

def is_valid_pair(queen1, queen2):
    x1, y1 = queen1
    x2, y2 = queen2
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def find_valid_configurations(n):
    """Trouve les configurations maximales de reines qui s'attaquent par paires"""
    all_positions = [(i, j) for i in range(n) for j in range(n)]
    valid_configs = []
    max_queens = 0
    
    def is_valid_configuration(queens):
        if not queens:
            return False
        attack_count = {queen: 0 for queen in queens}
        pairs = []
        for i, q1 in enumerate(queens):
            for q2 in queens[i+1:]:
                if is_valid_pair(q1, q2):
                    attack_count[q1] += 1
                    attack_count[q2] += 1
                    pairs.append((q1, q2))
        # Vérifie que chaque reine n'attaque qu'une seule autre reine
        return all(count == 1 for count in attack_count.values())

    def format_solution(queens):
        """Convertit une solution en représentation ASCII avec retours à la ligne"""
        board = [['.' for _ in range(n)] for _ in range(n)]
        for x, y in queens:
            board[x][y] = 'O'
        return '\n'.join(''.join(row) for row in board)

    def backtrack(queens, remaining_positions):
        nonlocal max_queens
        
        if is_valid_configuration(queens):
            if len(queens) >= max_queens:
                if len(queens) > max_queens:
                    max_queens = len(queens)
                    valid_configs.clear()
                valid_configs.append(format_solution(queens))
            return

        if not remaining_positions or len(queens) > n:
            return

        current_pos = remaining_positions[0]
        new_remaining = remaining_positions[1:]

        # Essayer avec la reine courante
        backtrack(queens + [current_pos], new_remaining)
        # Essayer sans la reine courante
        backtrack(queens, new_remaining)

    backtrack([], all_positions)
    return valid_configs

def pretty_print_solutions(solutions):
    """Affiche les solutions de manière formatée"""
    for i, solution in enumerate(solutions):
        print(f"\nSolution {i + 1}:")
        print(solution)
        print()  # ligne vide entre les solutions

if __name__ == '__main__':
    n = 4
    solutions = find_valid_configurations(n)
    pretty_print_solutions(solutions)

