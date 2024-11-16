from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
# 再帰用
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def main():
    from heapq import heapify,heappop,heappush
    from copy import deepcopy
    import math
    import random
    random.seed(20020401)
    N = int(myin())
    S = []
    for i in range(N):
        a,b = myin_sp_i()
        S.append((a,b))
    S.sort()
    
    # 初期解生成のアルゴリズム
    def init_solver(S,L):
        accum0 = [0]*(N+1)
        accum1 = [0]*(N+1)
        for i in range(N):
            accum0[i+1]=accum0[i]+S[i][0]
            accum1[i+1]=accum1[i]+S[i][1]
        ave = []
        for i in range((N+L-1)//L):
            if i*L+L-1>=N and i*L+1==N:
                break
            l = min(N,i*L+L)-i*L
            a = accum0[min(N,i*L+L)]-accum0[i*L]
            b = accum1[min(N,i*L+L)]-accum1[i*L]
            ave.append((a//l,b//l))
        return ave
    E = {}
    deg = {}
    def answer(S,add_S):
        nonlocal E,deg
        E = {}
        deg={}
        ret = []
        all_S = S+add_S
        cost = {}
        pq = [(0,(0,0),(-1,-1))]
        heapify(pq)
        while pq:
            c,v,p = heappop(pq)
            if v in cost:
                continue
            cost[v]=c
            if p!=(-1,-1):
                ret.append([p[0],p[1],v[0],v[1]])
                if p not in E:
                    E[p]=[]
                    deg[p]=0
                E[p].append(v)
                deg[p]+=1
            for vv in all_S:
                if v[0]<=vv[0] and v[1]<=vv[1]:
                    res = vv[0]-v[0]+vv[1]-v[1]
                    if vv not in cost:
                        heappush(pq,(res,vv,v))
        return ret
    #add_S=init_solver(S,L=int(math.sqrt(N)))
    ans1 = answer(S,[])
    add_S = []
    for loop in range(2):
        centroid_cnt = 0
        for p,_ in sorted(deg.items(),key=lambda x:-x[1]):
            center_x = 0
            center_y = 0
            if len(E[p])==1:
                center_x=(E[p][0][0]+p[0])//2
                center_y=(E[p][0][1]+p[1])//2
            else:
                div = 0
                for i in range(len(E[p])-1):
                    v1 = E[p][i]
                    v2 = E[p][i+1]
                    vv1 = (v1[0]-p[0],v1[1]-p[1])
                    vv2 = (v2[0]-p[0],v2[1]-p[1])
                    s = (vv1[0]*vv2[1]-vv2[0]*vv1[1])//2
                    gx = (v1[0]+v2[0]+p[0])//3
                    gy = (v1[1]+v2[1]+p[1])//3
                    center_x+=s*gx
                    center_y+=s*gy
                    div+=s
                center_x//=div
                center_y//=div
            add_S.append((center_x,center_y))
            centroid_cnt+=1
            if centroid_cnt==N//100*30:
                break
        ans = answer(S,add_S)
        ans1 = ans
    ans2 = []
    for res in ans1:
        if (res[2],res[3]) not in deg and (res[2],res[3]) in add_S:
            continue
        ans2.append(res)
    print(len(ans2))
    for res in ans2:
        print(*res)

if __name__ == "__main__":
    main()