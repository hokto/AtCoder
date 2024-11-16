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
    N,Q = myin_sp_i()
    M = max(N,Q)
    C = myin_sp_i()
    block_size = int(N/Q**0.5)+1
    qs = [[] for i in range(N//block_size+1)]
    for q in range(Q):
        l,r = myin_sp_i()
        l-=1
        r-=1
        qs[l//block_size].append(l*M*M+r*M+q)
    color = [0]*(N+1)
    x=0
    y=0
    cnt = 0
    ans = [0]*Q
    for i,qb in enumerate(qs):
        for a in sorted(qb,key=lambda x: (x//M)%M,reverse=i%2):
            l = a//(M*M)
            r = (a//M)%M
            q = a%M
            while y<=r:
                if color[C[y]]==0:
                    cnt+=1
                color[C[y]]+=1
                y+=1
            while x>l:
                x-=1
                if color[C[x]]==0:
                    cnt+=1
                color[C[x]]+=1
            while y>r+1:
                y-=1
                if color[C[y]]==1:
                    cnt-=1
                color[C[y]]-=1
            while x<l:
                if color[C[x]]==1:
                    cnt-=1
                color[C[x]]-=1
                x+=1
            ans[q] = cnt
    print(*ans,sep="\n")

if __name__ == "__main__":
    main()