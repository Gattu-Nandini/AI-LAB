from queue import PriorityQueue

def heuristic(state, goal):
    return sum(abs(i - state.index(goal[i])) for i in range(len(goal)))

def get_neighbors(state):
    neighbors = []
    for i in range(len(state) - 1):
        s = list(state)
        s[i], s[i+1] = s[i+1], s[i]
        neighbors.append(''.join(s))
    return neighbors

def a_star(start, goal):
    pq = PriorityQueue()
    pq.put((heuristic(start, goal), 0, start, [start]))
    visited = set()

    while not pq.empty():
        _, cost, state, path = pq.get()
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                pq.put((cost + 1 + heuristic(neighbor, goal), cost + 1, neighbor, path + [neighbor]))
    return None

# Example usage
start = "hema"
goal = "mahe"
solution = a_star(start, goal)

if solution:
    for i, step in enumerate(solution):
        print(f"{i}) {step}")
else:
    print("No solution found.")
