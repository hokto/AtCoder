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
    S = myin()
    T = myin()
    inv_T = []
    prev_T = 0
    for i in range(len(T)):
        if T[i]!=T[prev_T]:
            inv_T.append((prev_T,i))
            prev_T = i
    inv_T.append((prev_T,len(T)))
    inv_S = []
    prev_S = 0
    for i in range(len(S)):
        if S[i]!=S[prev_S]:
            inv_S.append((prev_S,i))
            prev_S = i
    inv_S.append((prev_S,len(S)))
    if len(inv_S)!=len(inv_T):
        print("No")
        return
    for i in range(len(inv_S)):
        l_S,r_S = inv_S[i]
        l_T,r_T = inv_T[i]
        if S[l_S]!=T[l_T]:
            print("No")
            return
        elif r_S-l_S==1:
            if r_T-l_T>1:
                print("No")
                return
        elif r_S-l_S>r_T-l_T:
            print("No")
            return
    print("Yes")
if __name__ == "__main__":
    main()