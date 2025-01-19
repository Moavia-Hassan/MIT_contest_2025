from collections import defaultdict, deque

# Read input
input_data = input().split()
N = int(input_data[0])
K = int(input_data[1])

screenshots = []
idx = 2
for _ in range(N):
    scores = list(map(int, input_data[idx:idx + K]))
    screenshots.append(scores)
    idx += K

# Build graph
graph = defaultdict(list)
in_degree = [0] * N

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        valid = True
        for t in range(K):
            if screenshots[i][t] > screenshots[j][t]:
                valid = False
                break
        if valid:
            graph[i].append(j)
            in_degree[j] += 1

# Topological sort
queue = deque()
for i in range(N):
    if in_degree[i] == 0:
        queue.append(i)

order = []
while queue:
    u = queue.popleft()
    order.append(u + 1)  # Convert to 1-based index
    for v in graph[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

# Output result
if len(order) == N:
    print("YES")
    print(" ".join(map(str, order)))
else:
    print("NO")