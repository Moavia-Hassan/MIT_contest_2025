import sys

def inp():
    return map(int, sys.stdin.readline().strip().split())

N, Q = inp()
a = [0] + list(inp())

CHUNK_SIZE = 64
chunks = (N + CHUNK_SIZE - 1) // CHUNK_SIZE
size = 1
while size < N:
    size <<= 1
tree = [[0] * chunks for _ in range(2 * size)]

for i in range(1, N + 1):
    if 1 <= a[i] <= N:
        chunk_idx = (a[i] - 1) // CHUNK_SIZE
        bit_pos = (a[i] - 1) % CHUNK_SIZE
        tree[size + i - 1][chunk_idx] |= (1 << bit_pos)

for i in range(size - 1, 0, -1):
    for c in range(chunks):
        tree[i][c] = tree[2 * i][c] | tree[2 * i + 1][c]

output = []

for _ in range(Q):
    type_q, x, y = inp()
    
    if type_q == 1:
        old_val = a[x]
        pos = size + x - 1
        if 1 <= old_val <= N:
            chunk_idx = (old_val - 1) // CHUNK_SIZE
            bit_pos = (old_val - 1) % CHUNK_SIZE
            tree[pos][chunk_idx] &= ~(1 << bit_pos)
        if 1 <= y <= N:
            chunk_idx = (y - 1) // CHUNK_SIZE
            bit_pos = (y - 1) % CHUNK_SIZE
            tree[pos][chunk_idx] |= (1 << bit_pos)
        a[x] = y
        pos //= 2
        while pos >= 1:
            for c in range(chunks):
                tree[pos][c] = tree[2 * pos][c] | tree[2 * pos + 1][c]
            pos //= 2
    else:
        mask = [0] * chunks
        left = size + x - 1
        right = size + y - 1
        while left <= right:
            if left % 2 == 1:
                for c in range(chunks):
                    mask[c] |= tree[left][c]
                left += 1
            if right % 2 == 0:
                for c in range(chunks):
                    mask[c] |= tree[right][c]
                right -= 1
            left //= 2
            right //= 2
        
        for c in range(chunks):
            if mask[c] != (1 << CHUNK_SIZE) - 1:
                for b in range(CHUNK_SIZE):
                    if not (mask[c] & (1 << b)):
                        output.append(c * CHUNK_SIZE + b + 1)
                        break
                break

print('\n'.join(map(str, output)))