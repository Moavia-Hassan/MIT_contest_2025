T = int(input())

inputs = []

for _ in range(T):
    length = int(input())
    S = input()
    inputs.append((length, S))

for length, S in inputs:
    valid = True
    i = 0
    
    while i < length:
        if S[i] != 'M':
            valid = False
            break
        i += 1
        
        count = 0
        while i + 1 < length and S[i] == 'I' and S[i + 1] == 'T':
            count += 1
            i += 2
        
        if count == 0:
            valid = False
            break
    
    if valid:
        print("YES")
    else:
        print("NO")