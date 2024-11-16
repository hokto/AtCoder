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
    if N==1:
        print(0)
        exit()
    N-=1
    d_max = 9
    d = 1
    while N>d_max:
        N-=d_max
        if d%2==0:
            d_max=d_max*10
        d+=1
    N+=10**((d-1)//2)-1
    #if N>d_max:
        #N-=d_max
    #print(d_max,N)
    ans = ["0"]*d
    S_N = str(N)
    for i in range(len(S_N)):
        ans[i]=ans[d-1-i]=S_N[i]
    print("".join(ans))
if __name__ == "__main__":
    main()