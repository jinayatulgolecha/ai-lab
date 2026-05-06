# Water Jug using DFS (simple)

def dfs(x, y, jug1, jug2, target, visited):
    if (x, y) in visited:
        return False

    visited.add((x, y))
    print((x, y))

    if x == target or y == target:
        return True

    return (
        dfs(jug1, y, jug1, jug2, target, visited) or   # fill jug1
        dfs(x, jug2, jug1, jug2, target, visited) or   # fill jug2
        dfs(0, y, jug1, jug2, target, visited) or      # empty jug1
        dfs(x, 0, jug1, jug2, target, visited) or      # empty jug2
        dfs(max(0, x-(jug2-y)), min(jug2, y+x), jug1, jug2, target, visited) or  # pour 1→2
        dfs(min(jug1, x+y), max(0, y-(jug1-x)), jug1, jug2, target, visited)     # pour 2→1
    )

# Example
dfs(0, 0, 3, 5, 4, set())