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
    # Wの最大値-> W=min{W_i}なので，Wを二分探索し，W以上となるように各W_iを設定することが可能か決める
    # それぞれWiを達成するために，必要な最小の値段を知りたい
    N,X = myin_sp_i()
    machine = []
    for i in range(N):
        machine.append(myin_sp_i())
    def f(m):
        # 各iでx以上を達成
        res = 0
        for i in range(N):
            a,p,b,q = machine[i]
            x = (m+a-1)//a
            y = (m+b-1)//b
            res2 = p*x
            for i in range(min(b,x)+1):
                yy = (max(m-a*(x-i),0)+b-1)//b
                res2 = min(p*(x-i)+q*yy,res2)
            for i in range(min(a,y)+1):
                xx = (max(m-b*(y-i),0)+a-1)//a
                res2 = min(p*xx+q*(y-i),res2)
            res+=res2
        return res<=X
    ok = 0
    ng = 10**15
    while ng-ok>1:
        m = ok+(ng-ok)//2
        if f(m):
            ok = m
        else:
            ng = m
    print(ok)

if __name__ == "__main__":
    main()