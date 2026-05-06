# Cities Distance - Best First Search

from queue import PriorityQueue

graph = {
    'A': [('B',1),('C',4)],
    'B': [('D',2)],
    'C': [('D',1)],
    'D': []
}

heuristic = {'A':7,'B':6,'C':2,'D':0}

def best_first(start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], start))
    visited = set()

    while not pq.empty():
        _, node = pq.get()
        print(node)

        if node == goal:
            print("Reached goal!")
            return

        visited.add(node)

        for neigh, cost in graph[node]:
            if neigh not in visited:
                pq.put((heuristic[neigh], neigh))

best_first('A','D')