def solve_n_queens(n):
    pass

def display_board(solution):
    n = len(solution)
    board = [['.' for _ in range(n)] for _ in range(n)]
    for row, col in enumerate(solution):
        board[row][col] = 'Q'
    return board