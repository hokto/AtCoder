from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import random as rd
from collections import deque
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

        
N,M,T,LA,LB = myin_sp_i()
G = [[] for i in range(N)]
for _ in range(M):
    u,v = myin_sp_i()
    G[u].append(v)
    G[v].append(u)
Tour = [0]+myin_sp_i() # 0からスタート

class MyPrint:
    def __init__(self) -> None:
        self.len = 0
        self.print_str = ""
    def print_A(self,A):
        self.print_str+=" ".join(map(str,A))+"\n"
        self.len+=1
    def print_B(self,l,pa,pb):
        self.print_str+=f"s {l} {pa} {pb}\n"
        self.len += 1
    def print_move(self,to):
        self.print_str+=f"m {to}\n"
        self.len += 1
    
    def answer(self):
        print(self.print_str)
INF = 10**5
# Aが決まった時に最終の目的地まで動かすまでを1ゲームとする
# さらに，1ゲーム内であるスタート地点からゴール地点まで行く段階を1セクションとする(各Tセクション存在)
class Game:
    def __init__(self,_A) -> None:
        self.A = _A
        self.select_B_len = 0
        self.A_pos = -1
        self.B_pos = -1
        self.B = [-1]*LB
        self.dist = []
        self.log = []
        self.start = Tour[0]
        self.goal = Tour[1]
        self.cnt_section = 0
        self.turn = 0
        self.print = MyPrint()
        self.print.print_A(_A)
        # 何回目のBの変更かメモする
        self.B_change = [-1]*N
        # Bの変更内容をメモする
        self.B_log = []
        # Bの変更回数
        self.B_change_cnt = -1
    def init_section(self):
        self.start = Tour[self.cnt_section]
        self.goal = Tour[self.cnt_section+1]
        # スタートからゴールまでの最短の距離(正確にはターン数)をメモする
        self.dist = [INF]*N
        self.dist[self.start] = 0
        # どこから来たかメモしとく
        self.log = [-1]*N
    def solve_section(self):
        # 一旦無限にループさせる
        # 目的地に到着したら抜けるようには処理する
        for loop in range(INF):
            if self.select_B_len==0:
                #  一旦，乱数でBの範囲を決定する
                self.select_B_len = rd.randint(1,LB)
                self.A_pos = rd.randint(0,LA-self.select_B_len)
                self.B_pos = rd.randint(0,LB-self.select_B_len)
                self.B[self.B_pos:self.B_pos+self.select_B_len] = self.A[self.A_pos:self.A_pos+self.select_B_len]
                #self.print.print_B(self.select_B_len,self.A_pos,self.B_pos)
                self.B_log.append((self.select_B_len,self.A_pos,self.B_pos))
                self.B_change_cnt += 1
            deq = deque()
            for b in self.B:
                if self.dist[b]<INF:
                    deq.append((b,-1,self.dist[b]+1))
                    self.dist[b]=INF
                    self.B_change[b]=self.B_change_cnt
            find_goal = False
            while deq:
                v,p,cost = deq.popleft()
                if cost>=self.dist[v]: continue
                self.dist[v] = cost
                self.log[v] = p
                if v==self.goal:
                    find_goal = True
                    break
                for vv in G[v]:
                    if vv == p: continue
                    if vv not in self.B: continue
                    if cost>=self.dist[vv]: continue
                    deq.append((vv,v,cost+1))
            self.select_B_len = 0
            if find_goal:
                break
        self.turn += self.dist[self.goal]
    def fin_section(self):
        print(self.dist)
        stack = []
        now = self.goal
        while now!=-1:
            stack.append(("m",now))
            to = self.log[now]
            if to!=-1 and self.B_change[now]!=self.B_change[to]:
                stack.append(("s",*self.B_log[self.B_change[now]]))
            now = to
        stack.append(("s",*self.B_log[self.B_change[self.start]]))
        while stack:
            query = stack.pop()
            if query[0]=="m":
                self.print.print_move(query[1])
            else:
                self.print.print_B(query[1],query[2],query[3])
            
        self.cnt_section += 1
        
    def solve_game(self):
        for _ in range(T):
            self.init_section()
            self.solve_section()
            self.fin_section()
        
def main():
    # N=600,T=600で固定
    # N-1<=M<=3*N-6
    # N<=LA<=2*N
    # 4<=LB<=24
    init_A = [i for i in range(N)]
    # 足りない分をランダムに追加
    for _ in range(LA-N):
        init_A.append(rd.randint(0,N-1))
    rd.shuffle(init_A) # LAの長さにしてシャッフル
    print(f"{init_A=}") 
    game = Game(init_A)
    game.solve_game()
    game.print.answer()

if __name__ == "__main__":
    rd.seed(1421324)
    main()