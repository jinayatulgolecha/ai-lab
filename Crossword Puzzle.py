# Crossword CSP - simple (word fit)

grid = [
    ['_','_','_'],
    ['_','#','_'],
    ['_','_','_']
]

words = ["CAT","DOG"]

def can_place(word, row, col):
    if col + len(word) > 3:
        return False
    for i in range(len(word)):
        if grid[row][col+i] not in ['_', word[i]]:
            return False
    return True

def place(word, row, col):
    for i in range(len(word)):
        grid[row][col+i] = word[i]

def solve(i):
    if i == len(words):
        for r in grid: print(r)
        return True

    for r in range(3):
        for c in range(3):
            if can_place(words[i], r, c):
                temp = [row[:] for row in grid]
                place(words[i], r, c)
                if solve(i+1):
                    return True
                for x in range(3):
                    grid[x] = temp[x]
    return False

solve(0)