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
    N,T = myin_sp_s()
    TN = len(T)
    N = int(N)
    ans = []
    for i in range(N):
        S = myin()
        SN = len(S)
        if TN==SN:
            diff_cnt = 0
            for j in range(TN):
                if T[j]!=S[j]: diff_cnt+=1
            if diff_cnt<=1: ans.append(i+1)
        elif TN<SN:
            if TN+1!=SN: continue
            s_i = 0
            isok = True
            for t_i in range(TN):
                if S[s_i]!=T[t_i]:
                    if s_i-t_i ==1:
                        isok = False
                        break
                    else:
                        s_i += 1
                        if S[s_i]!=T[t_i]:
                            isok = False
                            break
                s_i+=1
            if isok: ans.append(i+1)
        else:
            if SN+1!=TN: continue
            t_i = 0
            isok = True
            for s_i in range(SN):
                if S[s_i]!=T[t_i]:
                    if t_i-s_i ==1:
                        isok = False
                        break
                    else:
                        t_i += 1
                        if S[s_i]!=T[t_i]:
                            isok = False
                            break
                t_i+=1
            if isok: ans.append(i+1)
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    main()