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
    # (g-1)B+A/(\sqrt{g})=y
    # y'=B-0.5*(A/g\sqrt{g})=0
    # g**(3/2)B=0.5A
    # g**(3/2)=0.5A/B
    # g=(0.5A/B)**(2/3)
    A,B = myin_sp_i()
    g = max(1,int((0.5*A/B)**(2/3)))
    ans = (g-1)*B+A/(g**0.5)
    ans = min(ans,g*B+A/((g+1)**0.5))
    if g>1: ans = min(ans,(g-2)*B+A/((g-1)**0.5))
    print(round(ans,7))

if __name__ == "__main__":
    main()