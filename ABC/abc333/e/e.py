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
    N = int(myin())
    por = [[] for i in range(N)]
    que = []
    s = [0]*N
    used = [0]*N
    for i in range(N):
        t,x = myin_sp_i()
        x-=1
        if t==1:
            por[x].append(i)
            que.append(i)
        else:
            if not por[x]:
                print(-1)
                return
            idx = por[x].pop()
            used[idx]=1
            s[idx]+=1
            s[i]-=1
    ans = []
    for idx in que:
        ans.append(used[idx])
    K = 0
    k=0
    for i in range(N):
        k+=s[i]
        K = max(k,K)
    print(K)
    print(*ans)

if __name__ == "__main__":
    main()