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
    N,K = myin_sp_i()
    S = myin()
    k = 0
    ans = []
    is_one_bulk = False
    use_st = False
    st = []
    for i in range(N):
        if S[i]=="1" and not is_one_bulk:
            is_one_bulk = True
        elif S[i]=="0" and is_one_bulk:
            is_one_bulk = False
            k+=1
            if k==K-1:
                use_st = True
            elif k==K:
                use_st = False
                while st:
                    ans.append(st.pop())
        if use_st:
            st.append(S[i])
        else:
            ans.append(S[i])
    while st:
        ans.append(st.pop())
    print(*ans,sep="")

if __name__ == "__main__":
    main()