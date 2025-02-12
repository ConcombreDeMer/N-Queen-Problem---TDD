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
    all_positions = [(i, j) for i in range(n) for j in range(n)]
    valid_configs = []
    
    def is_valid_configuration(queens):
        if not queens:
            return False
        attack_count = {queen: 0 for queen in queens}
        for i, q1 in enumerate(queens):
            for q2 in queens[i+1:]:
                if is_valid_pair(q1, q2):
                    attack_count[q1] += 1
                    attack_count[q2] += 1
        return all(count == 1 for count in attack_count.values())

    def format_solution(queens):
        board = [['.' for _ in range(n)] for _ in range(n)]
        for x, y in queens:
            board[x][y] = 'O'
        return [''.join(row) for row in board]

    return []

