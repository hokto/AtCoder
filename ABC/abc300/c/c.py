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
    H,W = myin_sp_i()
    N = min(H,W)
    used = [[False]*W for _ in range(H)]
    ans = [0]*(N+1)
    C = []
    for i in range(H):
        C.append(myin())
    for i in range(H):
        st = []
        for j in range(W):
            if used[i][j]: continue
            if C[i][j]==".": continue
            if j+1<W and C[i+1][j+1]=="#": 
                st.append(j)
            if j-1>=0 and C[i+1][j-1]=="#":
                prev = st.pop()
                now = j
                ans[(now-prev)//2]+=1
                for k in range(now-prev+1):
                    used[i+k][prev+k]=True
                    used[i+k][now-k]=True
                prev=-1
    print(*ans[1:])

if __name__ == "__main__":
    main()