from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
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
    # ジャンプできる条件:(x1,y1),(x2,y2)に対して，|x1-x2|+|y1-y2|が偶数
    # そのため，x1,y1の偶奇によって3つのグループに分割して独立で考える
    # 1. どちらも偶数 2.どちらも奇数 3.それ以外(片方偶数，片方奇数)
    # ->元々45度回転することでより簡単に考えられる
    # X=x+y,Y=x-yとすると，1.どちらも偶数 2.どちらも奇数の場合のみジャンプ可能(X,Y軸がどちらも2だけ増える移動になるため)
    # また，その移動数は1/2|X1-X2|+1/2|Y1-Y2|=1/2(|X1-X2|+|Y1-Y2|)になる
    # 各グループの移動数の総和はソート済みのX,Yに対して1/2\sum_{i}\sum_{i<j}x_j-x_i+y_j-y_i=1/2\sum_{i}((2i-n_g+1)x_i+(2i-ng+1)y_i)
    
    N = int(myin())
    G1_x = []
    G1_y = []
    G2_x = []
    G2_y = []
    for i in range(N):
        x,y = myin_sp_i()
        X = x+y
        Y = x-y
        if X%2==Y%2:
            if X%2==0:
                G1_x.append(X)
                G1_y.append(Y)
            else:
                G2_x.append(X)
                G2_y.append(Y)
    G1_x.sort()
    G1_y.sort()
    G2_x.sort()
    G2_y.sort()
    ans = 0
    for g in [G1_x,G2_x,G1_y,G2_y]:
        n = len(g)
        for i,v in enumerate(g):
            ans+=(2*i-n+1)*v
    print(ans//2)
if __name__ == "__main__":
    main()