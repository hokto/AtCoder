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
    H,W,K = myin_sp_i()
    S = []
    for i in range(H):
        S.append(myin())
    ans = K+1
    for i in range(H):
        pena= 0
        dot = 0
        if K<=W:
            for k in range(K):
                if S[i][k]==".":
                    dot+=1
                elif S[i][k]=="x":
                    pena+=1
            if pena==0:
                ans=min(ans,dot)
            for k in range(K,W):
                if S[i][k-K]==".":
                    dot-=1
                elif S[i][k-K]=="x":
                    pena-=1
                if S[i][k]==".":
                    dot+=1
                elif S[i][k]=="x":
                    pena+=1
                if pena==0:
                    ans=min(ans,dot)
    for j in range(W):
        pena= 0
        dot = 0
        if K<=H:
            for k in range(K):
                if S[k][j]==".":
                    dot+=1
                elif S[k][j]=="x":
                    pena+=1
            if pena==0:
                ans=min(ans,dot)
            for k in range(K,H):
                if S[k-K][j]==".":
                    dot-=1
                elif S[k-K][j]=="x":
                    pena-=1
                if S[k][j]==".":
                    dot+=1
                elif S[k][j]=="x":
                    pena+=1
                if pena==0:
                    ans=min(ans,dot)
    if ans>K:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()