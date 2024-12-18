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
    T = int(myin())
    for t in range(T):
        N,M = myin_sp_i()
        B = [(0,0)] # (i,j):=座標iで値がjとなる
        A = [(0,0)] # (i,j):=座標iで値がjとなる
        ans = 0
        init = True
        for _ in range(N):
            x,y = myin_sp_i()
            if init:
                ans = x
                init = False
            pib,pjb = B[-1]
            pia,pja = A[-1]
            B.append((pib+y,pjb+x*y))
            if pjb>0 and B[-1][1]<=0:
                # pj+x*i>=0なる最大のiを探す
                # pj>=-x*i
                # -pj/x>=i
                i = -pjb//x
                ans = max(ans,pja+x*i*(i+1)//2+pjb*i)
            A.append((pia+y,pja+x*y*(y+1)//2+pjb*y))
        ans = max(ans,A[-1][1])
        #print(B)
        #print(A)
        print(ans)

if __name__ == "__main__":
    main()