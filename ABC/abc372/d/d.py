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
    H = myin_sp_i()
    ans = []
    st = []
    for h in H[::-1]:
        ans.append(len(st))
        if len(st)==0 or st[-1]>=h:
            st.append(h)
        else:
            while len(st)>0 and st[-1]<h:
                st.pop()
            st.append(h)
    print(*reversed(ans))

if __name__ == "__main__":
    main()