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
    Q = int(myin())
    pots = []
    t = 0
    l = -1
    for q in range(Q):
        query = myin_sp_i()
        if query[0]==1:
            pots.append(t)
        elif query[0]==2:
            t+=query[1]
        else:
            h = query[1]
            ok = l
            ng = len(pots)
            while ng-ok>1:
                m = ok+(ng-ok)//2
                if t-pots[m]>=h:
                    ok = m
                else:
                    ng = m
            print(ok-l)
            l = ok

if __name__ == "__main__":
    main()