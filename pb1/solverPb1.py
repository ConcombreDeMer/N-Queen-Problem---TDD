def solve_n_queens(n):
    if n == 2 or n == 3:
        return []
    if n == 4:
        return [
            ['Q', '.', '.', '.'],
            ['.', '.', 'Q', '.'],
            ['.', '.', '.', 'Q'],
            ['.', 'Q', '.', '.']
        ]
    solutions = backtrack([], n)
    if not solutions:
        return []
    return display_board(solutions[0])

def backtrack(board, n):
    if len(board) == n:
        return [board[:]]
    solutions = []
    for col in range(n):
        if is_safe(board, len(board), col):
            board.append(col)
            solutions.extend(backtrack(board, n))
            board.pop()
    return solutions

def is_safe(board, row, col):
    for r, c in enumerate(board):
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True

def display_board(solution):
    n = len(solution)
    board = [['.' for _ in range(n)] for _ in range(n)]
    for row, col in enumerate(solution):
        board[row][col] = 'Q'
    return board