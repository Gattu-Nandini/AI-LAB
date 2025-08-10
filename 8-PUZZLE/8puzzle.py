from collections import deque

def bfs(start):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    q = deque([(start, [])])
    seen = {tuple(start)}

    while q:
        state, path = q.popleft()
        if state == goal:
            return path + [state]

        i = state.index(0)
        for d in (-3, 3, -1, 1):
            ni = i + d
            if 0 <= ni < 9 and (i // 3 == ni // 3 if abs(d) == 1 else True):
                new = state[:]
                new[i], new[ni] = new[ni], new[i]
                t = tuple(new)
                if t not in seen:
                    seen.add(t)
                    q.append((new, path + [state]))

def show(path):
    for s in path:
        print('\n'.join(' '.join(str(x) if x != 0 else '_' for x in s[i:i+3]) for i in range(0, 9, 3)))
        print("-----")

# Example
start = [1, 2, 3, 4, 5, 6, 0, 7, 8]
sol = bfs(start)
if sol:
    show(sol)
    print(f"Solved in {len(sol) - 1} moves.")
else:
    print("No solution.")
