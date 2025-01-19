T = int(input())

inputs = []

for _ in range(T):
    N = int(input())
    cities = []
    for _ in range(N):
        x, y = map(int, input().split())
        cities.append((x, y))
    inputs.append((N, cities))

for N, cities in inputs:
    z_values = [x + y for x, y in cities]
    max_z = max(z_values)
    min_z = min(z_values)
    total_time = 2 * (max_z - min_z)
    print(total_time)