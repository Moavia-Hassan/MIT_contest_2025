import sys

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 2 ** (self.n - 1).bit_length()
        self.tree = [set() for _ in range(2 * self.size)]
        for i in range(self.n):
            self.tree[self.size + i] = {data[i]} if 1 <= data[i] <= self.n else set()
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] | self.tree[2 * i + 1]

    def update(self, idx, value):
        pos = self.size + idx
        self.tree[pos] = {value} if 1 <= value <= self.n else set()
        pos //= 2
        while pos >= 1:
            self.tree[pos] = self.tree[2 * pos] | self.tree[2 * pos + 1]
            pos //= 2

    def query(self, l, r):
        l += self.size
        r += self.size + 1
        res = set()
        while l < r:
            if l % 2 == 1:
                res |= self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                res |= self.tree[r]
            l //= 2
            r //= 2
        return res

def main():
    N, Q = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a = [0] + a  

    st = SegmentTree(a)
    output = []

    for _ in range(Q):
        type_op, x, y = map(int, sys.stdin.readline().split())
        
        if type_op == 1:
            st.update(x, y)
            a[x] = y
        else:
            present = st.query(x, y)
            missing = 1
            while missing <= N and missing in present:
                missing += 1
            output.append(missing)

    for result in output:
        print(result)

if __name__ == "__main__":
    main()