# A* Robot Navigation (simple)

from queue import PriorityQueue

grid = [
 [0,0,0],
 [1,1,0],
 [0,0,0]
]

goal = (2,2)

def h(x,y):
    return abs(x-goal[0]) + abs(y-goal[1])  # Manhattan

def astar():
    pq = PriorityQueue()
    pq.put((h(0,0), 0, (0,0)))  # (f,g,(x,y))
    visited = set()

    while not pq.empty():
        f, g, (x,y) = pq.get()
        print((x,y))

        if (x,y) == goal:
            print("Reached goal!")
            return

        visited.add((x,y))

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<3 and 0<=ny<3 and grid[nx][ny]==0 and (nx,ny) not in visited:
                pq.put((g+1 + h(nx,ny), g+1, (nx,ny)))

astar()