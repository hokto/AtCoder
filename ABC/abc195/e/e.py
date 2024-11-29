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
    S = myin()
    X = myin()
    # i番目の手番かつmod7がxである時に，高橋くんが勝つならTrue,青木くんが勝つならFalseにする
    memo = [[None]*7 for _ in range(N)]
    def rec(i,x):
        if memo[i][x] is not None:
            return memo[i][x]
        x1 = (x*10+int(S[i]))%7
        x2 = (x*10)%7
        if i==N-1:
            if X[i]=="T":
                return ((x1==0) | (x2==0))
            else:
                return ((x1==0) & (x2==0))
        res1 = rec(i+1,x1)
        res2=rec(i+1,x2)
        if X[i]=="T":
            memo[i][x] = (res1 | res2)
        else:
            memo[i][x] = (res1 & res2)
        return memo[i][x]
    
    if rec(0,0):
        print("Takahashi")
    else:
        print("Aoki")
    #print(memo)
if __name__ == "__main__":
    main()