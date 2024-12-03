from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
# 再帰用
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
    from itertools import permutations
    X,Y,A,B,C = myin_sp_i()
    N = 3
    def solve(x,y,i,R):
        if i==N:
            if x<0 or y<0:
                return False
            return True
        if x<=0 or y<=0:
            return False
        # 横いっぱいに配置する
        xx = x
        yy = y-(R[i]+xx-1)//xx
        f1 = solve(xx,yy,i+1,R)
        # 縦いっぱいに配置する
        yy = y
        xx = x-(R[i]+yy-1)//yy
        f2 = solve(xx,yy,i+1,R)
        return (f1|f2)
    for R in permutations([A,B,C]):
        f = solve(X,Y,0,R)
        if f:
            print("Yes")
            return
    print("No")

if __name__ == "__main__":
    main()