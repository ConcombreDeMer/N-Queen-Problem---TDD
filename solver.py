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

