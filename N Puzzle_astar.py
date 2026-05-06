# A* for 8 Puzzle (simple)

from queue import PriorityQueue

goal = [1,2,3,4,5,6,7,8,0]

def h(s):  # misplaced tiles
    return sum(1 for i in range(9) if s[i] != 0 and s[i] != goal[i])

def moves(s):
    i = s.index(0)
    r, c = i//3, i%3
    res = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            ni = nr*3 + nc
            new = s[:]
            new[i], new[ni] = new[ni], new[i]
            res.append(new)
    return res

def astar(start):
    pq = PriorityQueue()
    pq.put((h(start), 0, start))  # (f=g+h, g, state)
    visited = set()

    while not pq.empty():
        f, g, cur = pq.get()
        print(cur)

        if cur == goal:
            print("Goal reached!")
            return

        visited.add(tuple(cur))

        for m in moves(cur):
            if tuple(m) not in visited:
                pq.put((g+1 + h(m), g+1, m))

start = [1,2,3,4,0,6,7,5,8]
astar(start)