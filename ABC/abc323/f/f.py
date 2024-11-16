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
    # (XB,YB)->(XC,YC)に運ぶために，(XB,YB)を押すための方向を決める
    # XC-XB>0ならXB-1,XC-XB<0ならXB+1, XC-XB==0なら近い方
    # Yについても同様
    # そこからは，|XC-XB|+|YC-YB|だが，方向を切り替える必要(つまり，XC-XB!=0 and YC-YB!=0)があるなら+2する
    XA,YA,XB,YB,XC,YC = myin_sp_i()
    # どちらか一方の軸が揃っている場合
    if YA==YB==YC:
        if (XB-XA)*(XC-XA)>0:
            print(XC-XA-1)
        else:
            print(abs(XB-XA)+4+abs(XC-XB)-1)
        return
    elif XA==XB==XC:
        if (YB-YA)*(YC-YA)>0:
            print(YC-YA-1)
        else:
            print(abs(YB-YA)+4+abs(YC-YB)-1)
        return
    ans = 0
    ans+=abs(XB-XA)+abs(YB-YA)
    ans+=abs(XC-XB)+abs(YC-YB)
    if (XB-XA)*(XC-XA)>0 or (YB-YA)*(YC-YA)>0:
        ans+=1
    else:
        ans+=3
    print(ans)

if __name__ == "__main__":
    main()