# Water Jug using BFS (simple)

from collections import deque

def bfs(jug1, jug2, target):
    q = deque([(0, 0)])
    visited = set()

    while q:
        x, y = q.popleft()

        if (x, y) in visited:
            continue

        print((x, y))
        visited.add((x, y))

        if x == target or y == target:
            print("Reached target!")
            return

        q.append((jug1, y))   # fill jug1
        q.append((x, jug2))   # fill jug2
        q.append((0, y))      # empty jug1
        q.append((x, 0))      # empty jug2

        q.append((max(0, x-(jug2-y)), min(jug2, y+x)))  # pour 1→2
        q.append((min(jug1, x+y), max(0, y-(jug1-x))))  # pour 2→1

# Example
bfs(3, 5, 4)