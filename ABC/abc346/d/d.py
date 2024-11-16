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
    S = myin()
    C = myin_sp_i()
    zero_one_cost = [0]*N
    one_zero_cost = [0]*N
    for i in range(N):
        if i%2==0:
            if S[i]=="0":
                one_zero_cost[i]+=C[i]
            else:
                zero_one_cost[i]+=C[i]
        else:
            if S[i]=="0":
                zero_one_cost[i]+=C[i]
            else:
                one_zero_cost[i]+=C[i]
    zero_one_accum = [0]*(N+1)
    one_zero_accum = [0]*(N+1)
    for i in range(N):
        zero_one_accum[i+1]=zero_one_accum[i]+zero_one_cost[i]
        one_zero_accum[i+1]=one_zero_accum[i]+one_zero_cost[i]
    ans = sum(C)
    for i in range(N-1):
        one2 = 0
        if i>0:
            if (i-1)%2==0:
                one2+=zero_one_accum[i]
            else:
                one2+=one_zero_accum[i]
        if i<N-2:
            if (i+2)%2==0:
                one2+=zero_one_accum[N]-zero_one_accum[i+2]
            else:
                one2+=one_zero_accum[N]-one_zero_accum[i+2]
        if S[i]!="1":
            one2+=C[i]
        if S[i+1]!="1":
            one2+=C[i+1]
        zero2 = 0
        if i>0:
            if (i-1)%2==0:
                zero2+=one_zero_accum[i]
            else:
                zero2+=zero_one_accum[i]
        if i<N-2:
            if (i+2)%2==0:
                zero2+=one_zero_accum[N]-one_zero_accum[i+2]
            else:
                zero2+=zero_one_accum[N]-zero_one_accum[i+2]
        if S[i]!="0":
            zero2+=C[i]
        if S[i+1]!="0":
            zero2+=C[i+1]
        ans = min(ans,zero2,one2)
    print(ans)
if __name__ == "__main__":
    main()