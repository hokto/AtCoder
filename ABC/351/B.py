N = int(input())
A = []
B = []
for _ in range(N):
    A.append(input())
for _ in range(N):
    B.append(input())

for i in range(N):
    for j in range(N):
        if A[i][j]!=B[i][j]:
            print(f"{i+1} {j+1}")