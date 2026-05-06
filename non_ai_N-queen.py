# N-Queens - Simple Version

n = int(input("Enter N: "))
board = [[0]*n for _ in range(n)]

def safe(row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(col):
    if col == n:
        return True

    for i in range(n):
        if safe(i, col):
            board[i][col] = 1
            if solve(col + 1):
                return True
            board[i][col] = 0
    return False

solve(0)

for row in board:
    print(row)