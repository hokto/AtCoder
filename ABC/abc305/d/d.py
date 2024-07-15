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
    A = myin_sp_i()
    inter = []
    for i in range(N-1):
        inter.append([A[i],A[i+1]])
    accum = [0 for i in range(N)]
    for i in range(N-1):
        accum[i+1] = accum[i]
        if i%2==1:
            accum[i+1]+=inter[i][1]-inter[i][0]
    Q = int(myin())
    for q in range(Q):
        l,r = myin_sp_i()
        head1 = -1
        tail1 = len(inter)
        while tail1 - head1>1:
            m = head1+(tail1-head1) //2
            if inter[m][0]<=l:
                head1 = m
            else:
                tail1 = m
        head2 = -1
        tail2 = len(inter)
        while tail2-head2>1:
            m = head2+(tail2-head2)//2
            if r<=inter[m][1]:
                tail2 = m
            else:
                head2 = m
        ans = 0
        #print(head1,tail2)
        if head1%2==1:
            ans+=max(0,inter[head1][1]-l)
        if tail2%2==1:
            ans+=max(0,r-inter[tail2][0])
        ans+=accum[tail2]-accum[head1+1]
        print(ans)
if __name__ == "__main__":
    main()