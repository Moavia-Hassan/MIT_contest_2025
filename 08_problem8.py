import sys

def main():
    # Read all input at once
    input = sys.stdin.read
    data = input().split()

    idx = 0
    T = int(data[idx])  # Number of test cases
    idx += 1

    for _ in range(T):
        N = int(data[idx])  # Number of rows
        M = int(data[idx + 1])  # Number of columns
        idx += 2

        grid = []
        for _ in range(N):
            row = list(map(int, data[idx:idx + M]))  # Read a row of the grid
            grid.append(row)
            idx += M

        # Compute the XOR of all numbers in the grid
        xor_sum = 0
        for row in grid:
            for num in row:
                xor_sum ^= num

        # Determine the winner based on the XOR sum
        if xor_sum != 0:
            print("YES")  # Busy Beaver wins
        else:
            print("NO")  # Calico Bear wins

if __name__ == "__main__":
    main()