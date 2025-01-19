
T = int(input())
for _ in range(T):
    num = int(input())

for N in num:
    k = 1
    while 5**k < N:
        k += 1
    if k == 1:
        print("MIT time")
    else:
        print(f"MIT^{k} time")


