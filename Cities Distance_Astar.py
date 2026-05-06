# A* for Cities (simple)

from queue import PriorityQueue

graph = {
    'A': [('B',1),('C',4)],
    'B': [('D',2)],
    'C': [('D',1)],
    'D': []
}

h = {'A':7,'B':6,'C':2,'D':0}

def astar(start, goal):
    pq = PriorityQueue()
    pq.put((h[start], 0, start))  # (f,g,node)
    visited = set()

    while not pq.empty():
        f, g, node = pq.get()
        print(node)

        if node == goal:
            print("Reached goal!")
            return

        visited.add(node)

        for neigh, cost in graph[node]:
            if neigh not in visited:
                pq.put((g+cost + h[neigh], g+cost, neigh))

astar('A','D')