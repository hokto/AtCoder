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
    # bit的な考えでN-1本のジュースを配分すればできそう？
    M = 1
    while 2**M<N:
        M+=1
    ans = [[] for i in range(M)]
    for i in range(1,N):
        for b in range(M):
            if i&(1<<b)>0:
                ans[b].append(i)
    print(M,flush=True)
    for a in ans:
        print(len(a),*a,flush=True)
    S = myin()
    X = int(S[::-1],2)
    if X==0:
        print(N,flush=True)
    else:
        print(X,flush=True)
    

if __name__ == "__main__":
    main()