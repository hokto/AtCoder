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
    N,M = myin_sp_i()
    deg = [0 for i in range(N)]
    find = [False for i in range(N)]
    check,*vs = myin_sp_s()
    if check=="OK":
        exit()
    find[0] = True
    from collections import deque
    st = deque()
    st2 = deque()
    st2.append(0)
    for v in vs:
        v = int(v)
        v-=1
        st.append((0,v))
        deg[v]+=1
    while len(st)>0:
        p,v = st.pop()
        if find[v]: 
            if p!=st[-1][0]:
                st2.pop()
                while st[-1][0]!=st2[-1]:
                    #print(st)
                    print(st2.pop()+1,flush=True) # 戻る
                    _=myin_sp_i()
                print(st2.pop()+1,flush=True)
                st2.append(st[-1][0])
                _ = myin_sp_i()
            continue
        st2.append(v)
        find[v]=True
        arr = []
        print(v+1,flush=True)
        check,*vs = myin_sp_s()
        if check=="OK" or check=="-1":
            exit()
        for vv in vs:
            vv = int(vv)
            vv-=1
            #if vv==p: continue
            if find[vv]: continue
            deg[vv]+=1
            arr.append((deg[vv],vv))
        if len(arr)==0:
            st2.pop()
            while st[-1][0]!=st2[-1]:
                #print(st)
                print(st2.pop()+1,flush=True) # 戻る
                _=myin_sp_i()
            print(st2.pop()+1,flush=True)
            st2.append(st[-1][0])
            _ = myin_sp_i()
        else:
            arr.sort(reverse=False)
            for _,vv in arr:
                st.append((v,vv))


if __name__ == "__main__":
    main()