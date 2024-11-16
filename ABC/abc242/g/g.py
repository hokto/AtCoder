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
    def add(i):
        nonlocal max_pairs
        if cloth[i]%2:
            max_pairs+=1
        cloth[i]+=1
    
    def rem(i):
        nonlocal max_pairs
        if not cloth[i]%2:
            max_pairs-=1
        cloth[i]-=1
    N = int(myin())
    AA = myin_sp_i()
    A = [a-1 for a in AA]
    Q = int(myin())
    block_size = int(N/Q**0.5)+1
    qs = [[] for i in range(N//block_size+1)]
    for q in range(Q):
        l,r = myin_sp_i()
        l-=1
        r-=1
        qs[l//block_size].append((l,r,q))
    max_pairs = 0
    cloth = [0]*N
    x = 0
    y=0
    ans = [0]*Q
    for i,qb in enumerate(qs):
        for l,r,q in sorted(qb,key=lambda x:x[1],reverse=i%2):
            while y<=r:
                add(A[y])
                y+=1
            while x>l:
                x-=1
                add(A[x])
            while y>r+1:
                y-=1
                rem(A[y])
            while x<l:
                rem(A[x])
                x+=1
            ans[q]=max_pairs
    print(*ans,sep="\n")

if __name__ == "__main__":
    main()