# 8 Puzzle - Hill Climbing (simple)

goal = [1,2,3,
        4,5,6,
        7,8,0]

def h(state):  # heuristic = misplaced tiles
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

def get_moves(state):
    i = state.index(0)
    moves = []
    r, c = i//3, i%3

    dirs = [(-1,0),(1,0),(0,-1),(0,1)]  # up,down,left,right
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            ni = nr*3 + nc
            new = state[:]
            new[i], new[ni] = new[ni], new[i]
            moves.append(new)
    return moves

def hill_climb(start):
    current = start

    while True:
        print(current, "h =", h(current))

        if current == goal:
            print("Goal reached!")
            return

        neighbors = get_moves(current)
        next_state = min(neighbors, key=h)

        if h(next_state) >= h(current):
            print("Stuck at local optimum!")
            return

        current = next_state

# Example
start = [1,2,3,
         4,0,6,
         7,5,8]

hill_climb(start)