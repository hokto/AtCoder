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
    N,M = myin_sp_i()
    can_cutter = []
    A = [] # 缶切りが必要ない缶
    B = [] # 缶切りが必要な缶
    for _ in range(N):
        t,x = myin_sp_i()
        if t==0:
            A.append(x)
        elif t==1:
            B.append(x)
        else:
            can_cutter.append(x)
    can_cutter.sort(reverse=True)
    A.sort(reverse=True)
    B.sort(reverse=True)
    A_accum = [0]*(len(A)+1)
    B_accum = [0]*(len(B)+1)
    #print(can_cutter)
    #print(A)
    #print(B)
    for i in range(len(A)):
        A_accum[i+1]=A_accum[i]+A[i]
    for i in range(len(B)):
        B_accum[i+1]=B_accum[i]+B[i]
    def f(x,k):
        # Bの方から缶をx個買う時の満足度．ただし，k個分缶切りを購入済み
        res = B_accum[x] # 缶切りが必要な方の満足度
        res += A_accum[min(max(0,M-k-x),len(A))] # 缶切りが不要な方の満足度．缶切りとBの缶を買ってもなお残っていたら買う
        return res
    ans = 0
    cutter_sum = 0
    for i in range(min(len(can_cutter)+1,M)):
        # Bの方から缶を買う適切な個数を求める
        l = 0
        r = min(cutter_sum,M-i,len(B))
        while r-l>2:
            m1 = l+(r-l)//3
            m2 = l+2*(r-l)//3
            f1 = f(m1,i)
            f2 = f(m2,i)
            if f1>f2:
                r = m1
            else:
                l = m2
        ans=max(ans,f(l,i),f(r,i))
        if i<len(can_cutter): cutter_sum+=can_cutter[i]
    print(ans)
if __name__ == "__main__":
    main()