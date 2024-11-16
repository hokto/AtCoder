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

def f1(Y,X,coor,D):
    res = 0
    for x,y in coor:
        res+=abs(Y-y)+X-x
    return res<=D
def f2(Y,X,coor,D):
    res = 0
    for x,y in coor:
        res+=abs(y-Y)+x-X
    return res<=D
def main():
    N,D = myin_sp_i()
    coor = []
    for i in range(N):
        x,y = myin_sp_i()
        coor.append((x,y))
    ans = 0
    MX_Y = max(coor,key=lambda x:x[1])[1]
    MN_Y = min(coor,key=lambda x:x[1])[1]
    MX_X = max(coor,key=lambda x:x[0])[0]
    MN_X = min(coor,key=lambda x:x[0])[0]
    for Y in range(MN_Y-D,MX_Y+D+1):
        ok1 = MN_X-D-1
        ng1 = MX_X+D+1
        while ng1-ok1>1:
            m = ok1+(ng1-ok1)//2
            if f1(Y,m,coor,D):
                ok1 = m
            else:
                ng1 = m
        mx_x = ok1
        ok2 = MX_X+D+1
        ng2 = MN_X-D-1
        while ok2-ng2>1:
            m = ng2+(ok2-ng2)//2
            if f2(Y,m,coor,D):
                ok2 = m
            else:
                ng2 = m
        mn_x = ok2
        if ok1!=MN_X-1 and ok2!=MX_X+D+1:
            ans+=mx_x-mn_x+1
        #print(mx_x,mn_x)
    print(ans)
if __name__ == "__main__":
    main()