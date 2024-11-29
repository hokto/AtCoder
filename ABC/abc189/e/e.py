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

# (x,y) = O(a,b)+(a',b')
# 回転: (x',y') = O_r(x',y')
# 対称移動: (x',y') = (2p-x,y) = (-x,y) + (2p,0)
#          (x',y') = (x,2p-y) = (x,-y) + (0,2p)
class Matrix22:
    def __init__(self,a,b,c,d) -> None:
        self.val = ((a,b),
                    (c,d))
    def __mul__(self,other):
        a = self.val[0][0]*other.val[0][0]+self.val[0][1]*other.val[1][0]
        b = self.val[0][0]*other.val[0][1]+self.val[0][1]*other.val[1][1]
        c = self.val[1][0]*other.val[0][0]+self.val[1][1]*other.val[1][0]
        d = self.val[1][0]*other.val[0][1]+self.val[1][1]*other.val[1][1]
        return self.__class__(a,b,c,d)
    
    def mult_vec(self,vec):
        nx = self.val[0][0]*vec[0] + self.val[0][1]*vec[1]
        ny = self.val[1][0]*vec[0] + self.val[1][1]*vec[1]
        return (nx,ny)
            
E = Matrix22(1,0,0,1)
RotPos = Matrix22(0,-1,1,0)
RotNeg = Matrix22(0,1,-1,0)
MovX = Matrix22(-1,0,0,1)
MovY = Matrix22(1,0,0,-1)
def main():
    N = int(myin())
    coor = []
    for i in range(N):
        x,y = myin_sp_i()
        coor.append((x,y))
    M = int(myin())
    op = [(E,(0,0))] # (変換行列,差分の座標)
    for i in range(M):
        query = myin_sp_s()
        mat,vec = op[-1]
        if query[0]=="1":
            mat = RotNeg*mat
            op.append((mat,RotNeg.mult_vec(vec)))
        elif query[0]=="2":
            mat = RotPos*mat
            op.append((mat,RotPos.mult_vec(vec)))
        elif query[0]=="3":
            p = int(query[1])
            mat = MovX*mat
            new_vec = (-vec[0]+2*p,vec[1])
            op.append((mat,new_vec))
        else:
            p = int(query[1])
            mat = MovY*mat
            new_vec = (vec[0],-vec[1]+2*p)
            op.append((mat,new_vec))
    Q = int(myin())
    for q in range(Q):
        a,b = myin_sp_i()
        x,y = coor[b-1]
        mat,vec = op[a]
        nx,ny = mat.mult_vec((x,y))
        nx += vec[0]
        ny += vec[1]
        print(*[nx,ny])

if __name__ == "__main__":
    main()