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
    N,M,H,K = myin_sp_i()
    S = myin()
    P = {}
    for i in range(M):
        P[tuple(myin_sp_i())] = True
    x = 0
    y = 0
    h = H
    for i in range(N):
        if S[i]=="R":
            x+=1
        elif S[i]=="L":
            x-=1
        elif S[i]=="U":
            y+=1
        else:
            y-=1
        h-=1
        if h<0:
            print("No")
            return
        if (x,y) in P and P[(x,y)] and h<K:
            h = K
            P[(x,y)]=False
    print("Yes")
    

if __name__ == "__main__":
    main()