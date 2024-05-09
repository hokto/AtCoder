import math
T=int(input())
d = [2,4,8,6]
D = {2:0,4:1,8:2,6:3}
for t in range(T):
    N,M,K = list(map(int,input().split()))
    n_d = d[(N-1)%4]
    m_d = d[(M-1)%4]
    k_d = d[(K-1)%4]
    mk_d = (m_d - k_d)
    if mk_d<0: mk_d*=-1
    if mk_d==0:
        print(n_d)
    else:
        p_d = math.pow(2,N,10)*math.pow()
        q_d=n_d-p_d*mk_d
        if q_d<0: q_d*=-1
        print(q_d)
    