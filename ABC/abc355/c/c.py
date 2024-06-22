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
    A = myin_sp_i()
    row_sum = [0 for i in range(N)]
    col_sum = [0 for i in range(N)]
    naname1_sum = 0
    naname2_sum = 0
    ans = -1 
    for turn in range(T):
        a = A[turn]-1
        i = a//N
        j = a%N
        row_sum[i]+=1
        if row_sum[i]==N:
            ans = turn+1
            break
        col_sum[j]+=1
        if col_sum[j]==N:
            ans = turn+1
            break
        if i==j:
            naname1_sum+=1
            if naname1_sum==N:
                ans = turn+1
                break
        if i==N-1-j:
            naname2_sum+=1
            if naname2_sum==N:
                ans = turn+1
                break
        
    print(ans)

if __name__ == "__main__":
    main()