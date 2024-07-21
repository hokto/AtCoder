from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

ans = 0
find = {}
def func(s,n,used,S,N,K):
    global find
    if n>=K:
        flag = True
        for i in range(K//2):
            if s[n-K+i]!=s[n-1-i]:
                flag =False
        if flag:
            return
    if n==N:
        find[s] = 1
        return
    visit = {}
    for i in range(N):
        if not used[i] and S[i] not in visit:
            used[i] = True
            func(s+S[i],n+1,used,S,N,K)
            used[i]=False
            visit[S[i]]=1
def main():
    N,K = myin_sp_i()
    S=myin()
    dic = {}
    for i in range(N):
        if S[i] not in dic:
            dic[S[i]]=1
        else:
            dic[S[i]]+=1
    cnt = 0
    for v in dic.values():
        cnt+=v//2
    if cnt>=K//2:
        func("",0,[False for i in range(N)],S,N,K)
        print(len(find))
    else:
        ans = 1
        for i in range(2,N+1):
            ans*=i
        for v in dic.values():
            for j in range(2,v):
                ans//=j
        print(ans)
if __name__ == "__main__":
    main()