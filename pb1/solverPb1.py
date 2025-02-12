def solve_n_queens(n):
    """
    Résout le problème des N reines pour une taille donnée de tableau n x n.
    Retourne toutes les solutions possibles sous forme de tableaux d'échiquiers.
    """
    if n < 4:
        return []
    
    solutions = backtrack([], n)
    solutions.sort()
    return [display_board(solution) for solution in solutions]

def backtrack(board, n):
    """
    Fonction récursive qui cherche toutes les solutions en utilisant un backtracking.
    """
    if len(board) == n:
        return [board[:]]
    
    solutions = []
    row = len(board)
    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solutions += backtrack(board, n)
            board.pop()
    return solutions

def is_safe(board, row, col):
    """
    Vérifie si une reine peut être placée à la position (row, col).
    """
    for r, c in enumerate(board):
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True

def display_board(solution):
    """
    Affiche un échiquier pour une solution donnée sous forme de tableau.
    """
    n = len(solution)
    board = [['.' for _ in range(n)] for _ in range(n)]
    for row, col in enumerate(solution):
        board[row][col] = 'Q'
    return board
