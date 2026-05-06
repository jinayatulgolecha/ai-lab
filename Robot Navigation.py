# Robot Navigation - Best First Search

from queue import PriorityQueue

grid = [
 [0,0,0],
 [1,1,0],
 [0,0,0]
]

goal = (2,2)

def h(x,y):  # Manhattan distance
    return abs(x-goal[0]) + abs(y-goal[1])

def best_first():
    pq = PriorityQueue()
    pq.put((h(0,0), (0,0)))
    visited = set()

    while not pq.empty():
        _, (x,y) = pq.get()
        print((x,y))

        if (x,y) == goal:
            print("Reached goal!")
            return

        visited.add((x,y))

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<3 and 0<=ny<3 and grid[nx][ny]==0 and (nx,ny) not in visited:
                pq.put((h(nx,ny),(nx,ny)))

best_first()