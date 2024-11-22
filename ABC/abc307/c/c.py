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
    HA,WA = myin_sp_i()
    A = [[0]*WA for _ in range(HA)]
    for i in range(HA):
        for j,a in enumerate(myin()):
            if a=="#": A[i][j]=1
    HB,WB = myin_sp_i()
    B = [[0]*WB for _ in range(HB)]
    for i in range(HB):
        for j,b in enumerate(myin()):
            if b=="#": B[i][j]=1
    HX,WX = myin_sp_i()
    X = []
    for _ in range(HX):
        X.append(myin())
    Y = [[0]*WX for _ in range(HX)]
    for ai in range(-HX+1,HX):
        for aj in range(-WX+1,WX):
            flag1 = True
            for i in range(HA):
                for j in range(WA):
                    if A[i][j]:
                        if not (0<=ai+i<HX and 0<=aj+j<WX): flag1 = False
            if not flag1:
                continue
            for i in range(HA):
                for j in range(WA):
                    if A[i][j]:
                        Y[ai+i][aj+j]+=1
            for bi in range(-HX+1,HX):
                for bj in range(-WX+1,WX):
                    flag2 = True
                    for i in range(HB):
                        for j in range(WB):
                            if B[i][j]:
                                if not(0<=bi+i<HX and 0<=bj+j<WX): flag2 = False
                    if not flag2:
                        continue
                    for i in range(HB):
                        for j in range(WB):
                            if B[i][j]:
                                Y[bi+i][bj+j]+=1
                    isok = True
                    for i in range(HX):
                        for j in range(WX):
                            if X[i][j]=="#":
                                if not Y[i][j]:
                                    isok = False
                                    break
                            else:
                                if Y[i][j]:
                                    isok = False
                                    break
                        if not isok: break
                    if isok:
                        print("Yes")
                        return
                    for i in range(HB):
                        for j in range(WB):
                            if B[i][j]:
                                Y[bi+i][bj+j]-=1
            for i in range(HA):
                for j in range(WA):
                    if A[i][j]:
                        Y[ai+i][aj+j]-=1
    print("No")

if __name__ == "__main__":
    main()