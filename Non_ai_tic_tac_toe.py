# Tic Tac Toe - Simple Non-AI Version

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(p):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]] == p:
            return True
    return False

def play():
    player = "X"
    for turn in range(9):
        print_board()
        pos = int(input(f"Player {player}, enter position (1-9): ")) - 1
        
        if board[pos] != " ":
            print("Invalid move! Try again.")
            continue
        
        board[pos] = player
        
        if check_winner(player):
            print_board()
            print(f"Player {player} wins!")
            return
        
        player = "O" if player == "X" else "X"
    
    print_board()
    print("It's a draw!")

play()