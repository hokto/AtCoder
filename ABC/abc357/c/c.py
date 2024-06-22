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

ans = None
# 0:white 1:black
def out(d,ni,nj):
    global ans
    if d==1:
        ans[ni+1][nj+1]=0
        #print(ans)
        return
    for i in range(3):
        for j in range(3):
            if i==j==1:
                for ii in range(3**(d-1)):
                    for jj in range(3**(d-1)):
                        ans[ni+3**(d-1)+ii][nj+3**(d-1)+jj]=0
            else:
                out(d-1,ni+3**(d-1)*i,nj+3**(d-1)*j)
def main():
    global ans
    N = int(myin())
    if N==0:
        print("#")
        exit()
    ans = [[1 for _ in range(3**N)]for _ in range(3**N)] 
    out(N,0,0)
    for ans1 in ans:
        for v in ans1:
            if v==0:
                print(".",end="")
            elif v==1:
                print("#",end="")
        print("",end="\n")
if __name__ == "__main__":
    main()