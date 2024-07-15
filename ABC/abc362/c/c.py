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

def main():
    N = int(myin())
    X = [0 for i in range(N)]
    P_lr = []
    M_lr = []
    LR = []
    sum=0
    for i in range(N):
        l,r = myin_sp_i()
        LR.append((l,r))
        if 0<l:
            P_lr.append((l,r,i))
            sum+=l
            X[i]=l
        if r<0:
            M_lr.append((l,r,i))
            sum+=r
            X[i]=r
    for i in range(N):
        if sum>0 and LR[i][0]<X[i]:
            x=max(LR[i][0],X[i]-sum)
            if LR[i][1]<x:
                x = LR[i][1]
            sum+=x-X[i]
            X[i]=x
        if sum<0 and X[i]<LR[i][1]:
            x = min(LR[i][1],X[i]-sum)
            if LR[i][0]>x:
                x = LR[i][0]
            sum+=x-X[i]
            X[i]=x
    if sum==0:
        print("Yes")
        print(*X)
    else:
        print("No")
if __name__ == "__main__":
    main()