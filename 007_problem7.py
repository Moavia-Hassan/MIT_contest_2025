import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])  # Number of test cases
    idx += 1
    for _ in range(T):
        N = int(data[idx])  # Number of rows
        M = int(data[idx + 1])  # Number of columns
        idx += 2
        total_sum = 0  # To store the sum of all elements in the grid
        for _ in range(N):
            for _ in range(M):
                if idx < len(data):  # Ensure we don't go out of bounds
                    x = int(data[idx])
                    total_sum += x  # Accumulate the grid elements
                    idx += 1
                else:
                    break  # Exit if we run out of data
        # Check the parity of the total sum
        if total_sum % 2 == 1:
            print("YES")  # Busy Beaver wins
        else:
            print("NO")  # Calico Bear wins

if __name__ == "__main__":
    main()