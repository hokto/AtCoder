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
    H,W,X,Y = myin_sp_i()
    X-=1
    Y-=1
    S = []
    for _ in range(H):
        S.append(myin())
    T = myin()
    is_arrival = [[False]*W for _ in range(H)]
    for t in T:
        if t=="U":
            if X-1>=0 and S[X-1][Y]!="#":
                X-=1
        elif t=="D":
            if X+1<H and S[X+1][Y]!="#":
                X+=1
        elif t=="R":
            if Y+1<W and S[X][Y+1]!="#":
                Y+=1
        else:
            if Y-1>=0 and S[X][Y-1]!="#":
                Y-=1
        if S[X][Y]=="@":
            is_arrival[X][Y]=True
    ans = 0
    for i in range(H):
        for j in range(W):
            ans+=is_arrival[i][j]
    print(X+1,Y+1,ans)

if __name__ == "__main__":
    main()