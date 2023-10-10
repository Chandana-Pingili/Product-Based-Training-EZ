def is_safe(board, row, col, N):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if solve_nqueens_util(board, 0, N) is False:
        print("Solution does not exist")
        return
    print_solution(board)

def solve_nqueens_util(board, row, N):
    if row == N:
        return True
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_nqueens_util(board, row + 1, N):
                return True
            board[row][col] = 0  # Backtrack
    return False

def print_solution(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# Example usage:
n = int(input()) # You can change N to the desired board size
solve_nqueens(n)
