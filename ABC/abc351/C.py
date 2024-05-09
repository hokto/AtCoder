N = int(input())
A = list(map(int,input().split()))

stack = []
for i in range(N):
    now = A[i]
    while len(stack)!=0 and stack[-1]==now:
        prev = stack.pop(-1)
        now += 1
    stack.append(now)

print(len(stack))