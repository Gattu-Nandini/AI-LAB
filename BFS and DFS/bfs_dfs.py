from collections import deque

# Sample graph using dictionary (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    print("BFS Traversal:")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(neigh for neigh in graph[node] if neigh not in visited)
    print()

# DFS Function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        print("DFS Traversal:")

    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

# Run BFS and DFS
bfs(graph, 'A')
dfs(graph, 'A')
