# Map Coloring - simple CSP

graph = {
    'A': ['B','C'],
    'B': ['A','C','D'],
    'C': ['A','B','D'],
    'D': ['B','C']
}

colors = ['Red','Green','Blue']
result = {}

def safe(node, c):
    for n in graph[node]:
        if n in result and result[n] == c:
            return False
    return True

def solve(nodes):
    if not nodes:
        print(result)
        return True

    node = nodes[0]
    for c in colors:
        if safe(node, c):
            result[node] = c
            if solve(nodes[1:]):
                return True
            del result[node]
    return False

solve(list(graph.keys()))