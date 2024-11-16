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
    Q = int(myin())
    change = [chr(ord("a")+i) for i in range(26)]
    for q in range(Q):
        c,d = myin_sp_s()
        for i in range(26):
            if change[i]==c:
                change[i]=d
    ans = ""
    for i in range(N):
        ans+=change[ord(S[i])-ord("a")]
    print(ans)

if __name__ == "__main__":
    main()