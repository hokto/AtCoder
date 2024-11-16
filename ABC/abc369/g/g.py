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
    # K=1の時は1から最も遠い点を選ぶ
    # K=2の時は1からK=1で選んだ点の間のパスから最も離れている点を選ぶ
    # K=3の時はK=1,2で選んだ点のパスから最も離れている点を選ぶ
    #...
    # K=1から2,2から3に移るときに1から各点までのパスで使用していたらその分引くことができると嬉しい
    # ->パス上にある内点でかつ葉に辺が貼られている点が列挙できていればいい？
    pass

if __name__ == "__main__":
    main()