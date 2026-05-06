# Tic Tac Toe with Minimax (simple)

board = [" " for _ in range(9)]

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check(p):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in win)

def full():
    return " " not in board

def minimax(is_max):
    if check("O"): return 1     # AI
    if check("X"): return -1    # Player
    if full(): return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(True))
                board[i] = " "
        return best

def best_move():
    best_val = -100
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            val = minimax(False)
            board[i] = " "
            if val > best_val:
                best_val = val
                move = i
    return move

def play():
    while True:
        print_board()
        pos = int(input("Enter your move (1-9): ")) - 1

        if board[pos] != " ":
            print("Invalid!")
            continue

        board[pos] = "X"

        if check("X"):
            print_board()
            print("You win!")
            break

        if full():
            print_board()
            print("Draw!")
            break

        ai = best_move()
        board[ai] = "O"

        if check("O"):
            print_board()
            print("AI wins!")
            break

        if full():
            print_board()
            print("Draw!")
            break

play()