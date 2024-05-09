N,M = list(map(int,input().split()))
G = [[] for i in range(N)]
for i in range(M):
    A,B,C = list(map(int,input().split()))
    A-=1
    B-=1
    G[B].append((A,C))
    G[A].append((B,-C))

for i in range(N):
    is_decision = False
    dec_num = -1
    for r in range(N):
        que = [i]
        rank = [-1 for i in range(N)]
        rank[i] = r
        is_mujun = False
        while len(que)>0:
            p = que.pop(0)
            for v,c in G[p]:
                if rank[v]==-1:
                    rank[v]=rank[p]+c
                    que.append(v)
                elif rank[v]!=rank[p]+c:
                    is_mujun = True
                    break
            if is_mujun:
                break
        if i==0: print(rank)
        if not is_mujun:
            if not is_decision:
                is_decision=True
                dec_num = r+1
            else:
                is_decision = False
                dec_num=-1
                break
    print(dec_num)