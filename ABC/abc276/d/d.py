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
    A = myin_sp_i()
    B = [0]*N
    two_div_cnt = [0]*N
    three_div_cnt = [0]*N
    for i in range(N):
        x = A[i]
        while x%2==0:
            two_div_cnt[i]+=1
            x//=2
        while x%3==0:
            three_div_cnt[i]+=1
            x//=3
        B[i] = x
    if B.count(B[0])!=N:
        print(-1)
        return
    two_div_cnt_min = min(two_div_cnt)
    three_div_cnt_min = min(three_div_cnt)
    print(sum(two_div_cnt)-N*two_div_cnt_min+sum(three_div_cnt)-N*three_div_cnt_min)
if __name__ == "__main__":
    main()