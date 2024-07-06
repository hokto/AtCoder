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
    N,T = myin_sp_i()
    S = list(myin())
    X = myin_sp_i()
    XX = [[x,i] for i,x in enumerate(X)]
    XX.sort()
    A = [] # 正方向だけ
    B = [] # 負方向だけ
    for i in range(N):
        if S[XX[i][1]]=="0":
            B.append(XX[i][0])
        else:
            A.append(XX[i][0])
    NA = len(A)
    NB = len(B)
    ans = 0
    for i in range(NA):
        head = -1
        tail = NB
        while tail-head>1:
            m = head+(tail-head)//2
            if B[m]<=A[i]+2*T:
                head = m
            else:
                tail = m
        r1 = head
        head = -1
        tail = NB
        while tail-head>1:
            m = head+(tail-head)//2
            if B[m]<A[i]:
                head = m
            else:
                tail = m
        l1 = head
        ans+=r1-l1
        #print([l1,r1])
    print(ans)

if __name__ == "__main__":
    main()