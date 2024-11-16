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
    QR = []
    for i in range(N):
        QR.append(myin_sp_i())
    Q = int(myin())
    for q in range(Q):
        t,d = myin_sp_i()
        t-=1
        q,r = QR[t]
        print(d+(r-d%q)%q)

if __name__ == "__main__":
    main()