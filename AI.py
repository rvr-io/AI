## Tic-Tac-Toe Approach 1


def fun(turn):
    print()
    print_board(board)
    print('\nGame Over\n')
    print('*** '+turn+' Won ***')


def print_board(board):
    print(board['1']+' | '+board['2']+' | '+board['3'])
    print('--------')
    print(board['4']+' | '+board['5']+' | '+board['6'])
    print('--------')
    print(board['7']+' | '+board['8']+' | '+board['9'])
    

def game():
    turn = 'X'
    count = 0
    while True:
        print()
        print_board(board)
        print('\nIts your chance '+turn+'. Where to place? ',end=' ')
        move = input()
        if(board[move]==''):
            board[move] = turn
            count += 1
        else:
            print('\nIt is already filled.Try Again\n')
            continue
        if(count>=5):
            if(board['1']==board['2']==board['3']!=''):
                fun(turn)
                return
            elif(board['4']==board['5']==board['6']!=''):
                fun(turn)
                return
            elif(board['7']==board['8']==board['9']!=''):
                fun(turn)
                return
            elif(board['1']==board['4']==board['7']!=''):
                fun(turn)
                return
            elif(board['2']==board['5']==board['8']!=''):
                fun(turn)
                return
            elif(board['3']==board['6']==board['9']!=''):
                fun(turn)
                return
            elif(board['1']==board['5']==board['9']!=''):
                fun(turn)
                return
            elif(board['3']==board['5']==board['7']!=''):
                fun(turn)
                return
        if(count==9):
            print()
            print_board(board)
            print('\nGame Over\n')
            print('Its a Tie')
            return
        if(turn=='X'):
            turn = 'O'
        else:
            turn = 'X'
                

board = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
board_keys = list(map(str,list(range(1,10))))
game()
 |  | 
--------
 |  | 
--------
 |  | 

Its your chance X. Where to place?  1

X |  | 
--------
 |  | 
--------
 |  | 

Its your chance O. Where to place?  5

X |  | 
--------
 | O | 
--------
 |  | 

Its your chance X. Where to place?  9

X |  | 
--------
 | O | 
--------
 |  | X

Its your chance O. Where to place?  7

X |  | 
--------
 | O | 
--------
O |  | X

Its your chance X. Where to place?  3

X |  | X
--------
 | O | 
--------
O |  | X

Its your chance O. Where to place?  2

X | O | X
--------
 | O | 
--------
O |  | X

Its your chance X. Where to place?  6

X | O | X
--------
 | O | X
--------
O |  | X

Game Over

*** X Won ***
## Tic-Tac-Toe Approach 2


def f(x):  #converts number to symbols X,O
    if x==2:
        return ''
    elif x==3:
        return 'X'
    else:return 'O'
    
def display_board():      #prints board
    print()
    print(f(d[1])+' | '+f(d[2])+' | '+f(d[3]))
    print('------')
    print(f(d[4])+' | '+f(d[5])+' | '+f(d[6]))
    print('------')
    print(f(d[7])+' | '+f(d[8])+' | '+f(d[9]))
    print()
    
def hinput():       #takes input from human
    x=int(input("Enter the place you want : "))
    if d[x]==2:
        d[x]=3
    else:
        print('It is already filled. Please enter again')
        hinput()

def cinput():     #keep input of computer
    x=check_win('c')  #checks chance for win of computer
    if x!=0:
        d[x]=5
        return 1
    y=check_win('h')   #checks chance for win of human
    if y!=0:
        d[y]=5
    else:
        for i in (5,1,3,7,9,6,4,2,8):
            if d[i]==2:
                d[i]=5
                break
    return 0

def check_win(st):  # if 'h' it checks for possibility for human win else for computer win
    if st=='h':
        tot=18
    else:
        tot=50
    for i in range(1,8,3):
            if d[i]*d[i+1]*d[i+2]==tot:
                if d[i]==d[i+1]!=d[i+2]:
                    return i+2
                elif d[i]==d[i+2]!=d[i+1]:
                    return i+1
                else:
                    return i
    for i in range(1,4):
            if d[i]*d[i+3]*d[i+6]==tot:
                if d[i]==d[i+3]!=d[i+6]:
                    return i+6
                elif d[i]==d[i+6]!=d[i+3]:
                    return i+3
                else:
                    return i
    if d[1]*d[5]*d[9]==tot:
        if d[1]==d[5]!=d[9]:
            return 9
        elif d[5]==d[9]!=d[1]:
            return 1
        else:
            return 5
    elif d[3]*d[5]*d[7]==50:
         if d[3]==d[5]!=d[7]:
            return 7
         elif d[5]==d[7]!=d[3]:
            return 3
         else:
            return 5
    else:
        return 0
    
d={1:2,2:2,3:2,4:2,5:2,6:2,7:2,8:2,9:2}
s=input("Who is going to play first ! human (H) or computer (C) ...")
c=1
while(c<=9):
    display_board()
    if s=='H'or s=='h':
        flag = 0
        hinput()
        for i in range(1,8,3):
            if d[i]*d[i+1]*d[i+2]==27:
                flag=1
        for i in range(1,4):
            if d[i]*d[i+3]*d[i+6]==27:
                flag=1
        if d[1]*d[5]*d[9]==27:
                flag=1
        if d[3]*d[5]*d[7]==27:
                flag=1
        if flag==1:
            display_board()
            print('\nGame over\n')
            print("\nHuman won\n")
            break
        s=s[0:0]+'C'
    else:
        if cinput():
            display_board()
            print('\nGame over\n')
            print('****Computer won****')
            break
        else:
            s=s[0:0]+'H'
    c+=1
if c==10:
    display_board()
    print('\nGame over\n')
    print("It's a Tie")
Who is going to play first ! human (H) or computer (C) ...h

 |  | 
------
 |  | 
------
 |  | 

Enter the place you want : 1

X |  | 
------
 |  | 
------
 |  | 


X |  | 
------
 | O | 
------
 |  | 

Enter the place you want : 9

X |  | 
------
 | O | 
------
 |  | X


X |  | O
------
 | O | 
------
 |  | X

Enter the place you want : 7

X |  | O
------
 | O | 
------
X |  | X


X |  | O
------
 | O | 
------
X | O | X

Enter the place you want : 4

X |  | O
------
X | O | 
------
X | O | X


Human won

## Tic-Tac-Toe Approach 3
## WaterJug Problem - Traditional Approach


class Waterjug():
    def __init__(self,bjmax,sjmax,bj,sj,goal):
        self.bjmax = bjmax
        self.sjmax = sjmax
        self.bj = bj
        self.sj = sj
        self.goal = goal
        
    def fillbj(self):
        self.bj = self.bjmax
        print('(',self.bj,',',self.sj,')')
    
    def fillsj(self):
        self.sj = self.sjmax
        print('(',self.bj,',',self.sj,')')
        
    def emptybj(self):
        self.bj = 0
        print('(',self.bj,',',self.sj,')')
        
    def emptysj(self):
        self.sj = 0
        print('(',self.bj,',',self.sj,')')
    
    def transferbjtosj(self):
        while True:
            self.bj -= 1
            self.sj += 1
            if self.bj==0 or self.sj==self.sjmax:
                break
        print('(',self.bj,',',self.sj,')')
        
    def measure(self):
        print('(',self.bj,',',self.sj,')')
        while True:
            if self.bj==self.goal or self.sj==self.goal:
                print('\nSuccessful measuring')
                return
            if(self.bj==0):
                self.fillbj()
            elif(self.bj>0 and self.sj<self.sjmax):
                self.transferbjtosj()
            elif(self.bj>0 and self.sj==self.sjmax):
                self.emptysj()


big = int(input('enter big jug capacity : '))
small = int(input('enter small jug capacity : '))
goal = int(input('enter goal capacity : '))
waterjug = Waterjug(big,small,0,0,goal)
print()
waterjug.measure()
enter big jug capacity : 5
enter small jug capacity : 3
enter goal capacity : 1

( 0 , 0 )
( 5 , 0 )
( 2 , 3 )
( 2 , 0 )
( 0 , 2 )
( 5 , 2 )
( 4 , 3 )
( 4 , 0 )
( 1 , 3 )

Successful measuring
## WaterJug Problem - Using BFS


class Waterjug():
    def __init__(self,bjmax,sjmax,bj,sj,goal):
        self.bjmax = bjmax
        self.sjmax = sjmax
        self.bj = bj
        self.sj = sj
        self.goal = goal
        
    def bfs(self):
        open,closed = [],[]
        open.append((self.bj,self.sj))
        closed.append((self.bj,self.sj))
        while open:
            p = open.pop(0)
            print(p)
            self.bj = p[0]
            self.sj = p[1]
            
            ## goal case
            if(self.bj==self.goal or self.sj==self.goal):
                print('\nSuccessful measuring')
                return
            
            ## fill bj
            if self.bj==0 and (self.bjmax,self.sj) not in closed:
                open.append((self.bjmax,self.sj))
                closed.append((self.bjmax,self.sj))
                
            ## fill sj
            if self.sj==0 and (self.bj,self.sjmax) not in closed:
                open.append((self.bj,self.sjmax))
                closed.append((self.bj,self.sjmax))
                
            ## empty bj
            if self.bj>0 and (0,self.sj) not in closed:
                open.append((0,self.sj))
                closed.append((0,self.sj))
                
            ## empty sj
            if self.sj>0 and (self.bj,0) not in closed:
                open.append((self.bj,0))
                closed.append((self.bj,0))
                
            ## transfer from bj to sj
            if self.bj>0 and self.sj<self.sjmax:
                if self.bj>=(self.sjmax-self.sj):
                    t1 = self.bj - (self.sjmax-self.sj)
                    t2 = self.sjmax
                else:
                    t1 = 0
                    t2 = self.sj + self.bj
                if (t1,t2) not in closed:
                    open.append((t1,t2))
                    closed.append((t1,t2))
    

big = int(input('enter big jug capacity : '))
small = int(input('enter small jug capacity : '))
goal = int(input('enter goal capacity : '))
waterjug = Waterjug(big,small,0,0,goal)
print()
waterjug.bfs()
enter big jug capacity : 5
enter small jug capacity : 3
enter goal capacity : 4

(0, 0)
(5, 0)
(0, 3)
(5, 3)
(2, 3)
(2, 0)
(0, 2)
(5, 2)
(4, 3)

Successful measuring
## WaterJug Problem - Using DFS


class Waterjug():
    def __init__(self,bjmax,sjmax,bj,sj,goal):
        self.bjmax = bjmax
        self.sjmax = sjmax
        self.bj = bj
        self.sj = sj
        self.goal = goal
        
    def bfs(self):
        open,closed = [],[]
        open.append((self.bj,self.sj))
        closed.append((self.bj,self.sj))
        while open:
            p = open.pop()
            print(p)
            succ = []
            self.bj = p[0]
            self.sj = p[1]
            
            ## goal case
            if(self.bj==self.goal or self.sj==self.goal):
                print('\nSuccessful measuring')
                return
            
            ## fill bj
            if self.bj==0 and (self.bjmax,self.sj) not in closed:
                succ.append((self.bjmax,self.sj))
                
            ## fill sj
            if self.sj==0 and (self.bj,self.sjmax) not in closed:
                succ.append((self.bj,self.sjmax))
                
            ## empty bj
            if self.bj>0 and (0,self.sj) not in closed:
                succ.append((0,self.sj))
                
            ## empty sj
            if self.sj>0 and (self.bj,0) not in closed:
                succ.append((self.bj,0))
                
            ## transfer from bj to sj
            if self.bj>0 and self.sj<self.sjmax:
                if self.bj>=(self.sjmax-self.sj):
                    t1 = self.bj - (self.sjmax-self.sj)
                    t2 = self.sjmax
                else:
                    t1 = 0
                    t2 = self.sj + self.bj
                if (t1,t2) not in closed:
                    succ.append((t1,t2))
                    
            for i in succ[::-1]:
                open.append(i)
                closed.append(i)
    

big = int(input('enter big jug capacity : '))
small = int(input('enter small jug capacity : '))
goal = int(input('enter goal capacity : '))
waterjug = Waterjug(big,small,0,0,goal)
print()
waterjug.bfs()
enter big jug capacity : 5
enter small jug capacity : 4
enter goal capacity : 3

(0, 0)
(5, 0)
(5, 4)
(1, 4)
(1, 0)
(0, 1)
(5, 1)
(2, 4)
(2, 0)
(0, 2)
(5, 2)
(3, 4)

Successful measuring
## Missionaries and Cannibals Problem -- Using BFS


class Graph():
    def __init__(self,start,goal):
        self.start = start
        self.goal = goal
        
    def valid(self,x):
        a,b = x
        if((a[0]>a[1] and a[1]!=0) or (b[0]>b[1] and b[1]!=0)):
            return False
        if(a[0]<0 or a[1]<0 or b[0]<0 or b[1]<0):
            return False
        return True
        
    def insert(self,t,closed,x):
        if(self.valid(x)):
            if x not in closed:
                t.append(x)
                closed.append(x)
        
    def rules(self,open,closed,p1,p2):
        t = []
        if(p1[2]==1):
            x = ((p1[0],p1[1]-2,0),(p2[0],p2[1]+2,1))  ## send 2 missionaries
            self.insert(t,closed,x)
            
            x = ((p1[0]-1,p1[1]-1,0),(p2[0]+1,p2[1]+1,1))  ## send 1 missionaries and 1 cannibal
            self.insert(t,closed,x)
            
            x = ((p1[0]-2,p1[1],0),(p2[0]+2,p2[1],1))  ## send 2 cannibals
            self.insert(t,closed,x)
            
            x = ((p1[0],p1[1]-1,0),(p2[0],p2[1]+1,1))  ## send 1 missionaries
            self.insert(t,closed,x)
            
            x = ((p1[0]-1,p1[1],0),(p2[0]+1,p2[1],1))  ## send 1 cannibal
            self.insert(t,closed,x)
            
        else:
            x = ((p1[0],p1[1]+2,1),(p2[0],p2[1]-2,0))  ## send 2 missionaries
            self.insert(t,closed,x)

            x = ((p1[0]+1,p1[1]+1,1),(p2[0]-1,p2[1]-1,0))  ## send 1 missionaries and 1 cannibal
            self.insert(t,closed,x)
            
            x = ((p1[0]+2,p1[1],1),(p2[0]-2,p2[1],0))  ## send 2 cannibals
            self.insert(t,closed,x)
            
            x = ((p1[0],p1[1]+1,1),(p2[0],p2[1]-1,0))  ## send 1 missionaries
            self.insert(t,closed,x)
            
            x = ((p1[0]+1,p1[1],1),(p2[0]-1,p2[1],0))  ## send 1 cannibal
            self.insert(t,closed,x)
        return t
        
    def bfs(self):
        open,closed = [],[]
        open.append(self.start)
        closed.append(self.start)
        p = self.start
        while p!=goal and open:
            p = open.pop(0)
            p1,p2 = p
            t = self.rules(open,closed,p1,p2)
            open.extend(t)
            print(p)
            print()
            if p==goal:
                print('\nSuccessfully completed.')
                return


c = int(input('enter number of cannibals : '))
m = int(input('enter number of missionaries : '))
if(c<=m):
    start = ((c,m,1),(0,0,0))
    goal = ((0,0,0),(c,m,1))
    g = Graph(start,goal)
    print()
    g.bfs()
enter number of cannibals : 3
enter number of missionaries : 3

((3, 3, 1), (0, 0, 0))

((2, 2, 0), (1, 1, 1))

((1, 3, 0), (2, 0, 1))

((2, 3, 0), (1, 0, 1))

((2, 3, 1), (1, 0, 0))

((0, 3, 0), (3, 0, 1))

((1, 3, 1), (2, 0, 0))

((1, 1, 0), (2, 2, 1))

((2, 2, 1), (1, 1, 0))

((2, 0, 0), (1, 3, 1))

((3, 0, 1), (0, 3, 0))

((1, 0, 0), (2, 3, 1))

((1, 1, 1), (2, 2, 0))

((2, 0, 1), (1, 3, 0))

((0, 0, 0), (3, 3, 1))


Successfully completed.
## Missionaries and Cannibals Problem -- Using DFS


class Graph():
    def __init__(self,start,goal):
        self.start = start
        self.goal = goal
        
    def valid(self,x):
        a,b = x
        if((a[0]>a[1] and a[1]!=0) or (b[0]>b[1] and b[1]!=0)):
            return False
        if(a[0]<0 or a[1]<0 or b[0]<0 or b[1]<0):
            return False
        return True
        
    def insert(self,t,closed,x):
        if(self.valid(x)):
            if x not in closed:
                t.append(x)
                closed.append(x)
        
    def rules(self,open,closed,p1,p2):
        t = []
        if(p1[2]==1): ## boat on lef side
            x = ((p1[0],p1[1]-2,0),(p2[0],p2[1]+2,1))  ## send 2 missionaries
            self.insert(t,closed,x)
            
            x = ((p1[0]-1,p1[1]-1,0),(p2[0]+1,p2[1]+1,1))  ## send 1 missionaries and 1 cannibal
            self.insert(t,closed,x)
            
            x = ((p1[0]-2,p1[1],0),(p2[0]+2,p2[1],1))  ## send 2 cannibals
            self.insert(t,closed,x)
            
            x = ((p1[0],p1[1]-1,0),(p2[0],p2[1]+1,1))  ## send 1 missionaries
            self.insert(t,closed,x)
            
            x = ((p1[0]-1,p1[1],0),(p2[0]+1,p2[1],1))  ## send 1 cannibal
            self.insert(t,closed,x)
            
        else:  ## boat on right side
            x = ((p1[0],p1[1]+2,1),(p2[0],p2[1]-2,0))  ## send 2 missionaries
            self.insert(t,closed,x)

            x = ((p1[0]+1,p1[1]+1,1),(p2[0]-1,p2[1]-1,0))  ## send 1 missionaries and 1 cannibal
            self.insert(t,closed,x)
            
            x = ((p1[0]+2,p1[1],1),(p2[0]-2,p2[1],0))  ## send 2 cannibals
            self.insert(t,closed,x)
            
            x = ((p1[0],p1[1]+1,1),(p2[0],p2[1]-1,0))  ## send 1 missionaries
            self.insert(t,closed,x)
            
            x = ((p1[0]+1,p1[1],1),(p2[0]-1,p2[1],0))  ## send 1 cannibal
            self.insert(t,closed,x)           
        return t
        
    def dfs(self):
        open,closed = [],[]
        open.append(self.start)
        closed.append(self.start)
        p = self.start
        while p!=goal and open:
            p = open.pop()
            p1,p2 = p
            t = self.rules(open,closed,p1,p2)
            open.extend(t[::-1])
            print(p)
            print()
            if p==goal:
                print('\nSuccessfully completed.')
                return


c = int(input('enter number of cannibals : '))
m = int(input('enter number of missionaries : '))
if(c<=m):
    start = ((c,m,1),(0,0,0))
    goal = ((0,0,0),(c,m,1))
    g = Graph(start,goal)
    print()
    g.dfs()
enter number of cannibals : 3
enter number of missionaries : 3

((3, 3, 1), (0, 0, 0))

((2, 2, 0), (1, 1, 1))

((2, 3, 1), (1, 0, 0))

((0, 3, 0), (3, 0, 1))

((1, 3, 1), (2, 0, 0))

((1, 1, 0), (2, 2, 1))

((2, 2, 1), (1, 1, 0))

((2, 0, 0), (1, 3, 1))

((3, 0, 1), (0, 3, 0))

((1, 0, 0), (2, 3, 1))

((1, 1, 1), (2, 2, 0))

((0, 0, 0), (3, 3, 1))


Successfully completed.
## BFS


from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self,start,goal):
        open,closed = [],[]
        open.append(start)
        while open:
            x = open.pop(0)
            closed.append(x)
            if x==goal:
                print('\nGoal node found')
                print(x,'\topen - ',open,'\tclosed - ',closed)
                return
            for i in self.graph[x]:
                if i not in closed and i not in open:
                    open.append(i)
            print(x,'\topen - ',open,'\tclosed - ',closed)
                    
g = Graph()
m = int(input('enter number of edges : '))
for i in range(m):
    u,v = map(int,input('enter edge : ').split())
    g.add_edge(u,v)
start = int(input('enter start node : '))
goal = int(input('enter goal node : '))
print()
g.bfs(start,goal)
enter number of edges : 10
enter edge : 1 2
enter edge : 1 3
enter edge : 3 4
enter edge : 4 5
enter edge : 4 6
enter edge : 6 8
enter edge : 8 9
enter edge : 4 7
enter edge : 7 9
enter edge : 3 9
enter start node : 1
enter goal node : 8

1 	open -  [2, 3] 	closed -  [1]
2 	open -  [3] 	closed -  [1, 2]
3 	open -  [4, 9] 	closed -  [1, 2, 3]
4 	open -  [9, 5, 6, 7] 	closed -  [1, 2, 3, 4]
9 	open -  [5, 6, 7, 8] 	closed -  [1, 2, 3, 4, 9]
5 	open -  [6, 7, 8] 	closed -  [1, 2, 3, 4, 9, 5]
6 	open -  [7, 8] 	closed -  [1, 2, 3, 4, 9, 5, 6]
7 	open -  [8] 	closed -  [1, 2, 3, 4, 9, 5, 6, 7]

Goal node found
8 	open -  [] 	closed -  [1, 2, 3, 4, 9, 5, 6, 7, 8]
## DFS


from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self,start,goal):
        open,closed = [],[]
        open.insert(0,start)
        while open:
            succ = []
            x = open.pop(0)
            closed.append(x)
            if x==goal:
                print('\nGoal node found')
                print(x,'\topen - ',open,'\tclosed - ',closed)
                return
            for i in self.graph[x]:
                if i not in closed and i not in open:
                    succ.append(i)
            open = succ + open
            print(x,'\topen - ',open,'\tclosed - ',closed)
                    
g = Graph()
m = int(input('enter number of edges : '))
for i in range(m):
    u,v = map(int,input('enter edge : ').split())
    g.add_edge(u,v)
start = int(input('enter start node : '))
goal = int(input('enter goal node : '))
print()
g.dfs(start,goal)
enter number of edges : 10
enter edge : 1 2
enter edge : 1 3
enter edge : 3 4
enter edge : 3 9
enter edge : 4 5
enter edge : 4 6
enter edge : 4 7
enter edge : 6 8
enter edge : 7 9
enter edge : 8 9
enter start node : 1
enter goal node : 8

1 	open -  [2, 3] 	closed -  [1]
2 	open -  [3] 	closed -  [1, 2]
3 	open -  [4, 9] 	closed -  [1, 2, 3]
4 	open -  [5, 6, 7, 9] 	closed -  [1, 2, 3, 4]
5 	open -  [6, 7, 9] 	closed -  [1, 2, 3, 4, 5]
6 	open -  [8, 7, 9] 	closed -  [1, 2, 3, 4, 5, 6]

Goal node found
8 	open -  [7, 9] 	closed -  [1, 2, 3, 4, 5, 6, 8]
## DFID


from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self,u,v):
        self.graph[u].append([v,0])
        self.graph[v].append([u,0])
        
    def dfs(self,start,goal,i):
        open,closed = [],[]
        open.insert(0,[start,0])
        while open:
            succ = []
            u,v = open.pop(0)
            closed.append(u)
            if(u==goal):
                print(u,'\topen - ',open,'\tclosed - ',closed)
                return 1
            if(v<i):
                for j in self.graph[u]:
                    j[1] = v+1
                    if j[0] not in closed and j[0] not in open:
                        succ.append(j)
                open = succ + open
            print(u,'\topen - ',open,'\tclosed - ',closed)
        return 0
        
    def dfid(self,start,goal):
        x = 0
        i = 0
        while(x!=1):
            print('\nDFID with depth - ',i)
            x = self.dfs(start,goal,i)
            i += 1
        if(x==1):
            print('\nGoal node found')
    
g = Graph()
m = int(input('enter number of edges : '))
for i in range(m):
    u,v = map(int,input('enter edge : ').split())
    g.add_edge(u,v)
start = int(input('enter start node : '))
goal = int(input('enter goal node : '))
g.dfid(start,goal)
enter number of edges : 6
enter edge : 0 1
enter edge : 0 2
enter edge : 1 3
enter edge : 1 4
enter edge : 2 5
enter edge : 2 6
enter start node : 0
enter goal node : 6

DFID with depth -  0
0 	open -  [] 	closed -  [0]

DFID with depth -  1
0 	open -  [[1, 1], [2, 1]] 	closed -  [0]
1 	open -  [[2, 1]] 	closed -  [0, 1]
2 	open -  [] 	closed -  [0, 1, 2]

DFID with depth -  2
0 	open -  [[1, 1], [2, 1]] 	closed -  [0]
1 	open -  [[3, 2], [4, 2], [2, 1]] 	closed -  [0, 1]
3 	open -  [[4, 2], [2, 1]] 	closed -  [0, 1, 3]
4 	open -  [[2, 1]] 	closed -  [0, 1, 3, 4]
2 	open -  [[5, 2], [6, 2]] 	closed -  [0, 1, 3, 4, 2]
5 	open -  [[6, 2]] 	closed -  [0, 1, 3, 4, 2, 5]
6 	open -  [] 	closed -  [0, 1, 3, 4, 2, 5, 6]

Goal node found
## Bi-Directional Search


from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def bfs(self,node,turn):
        if turn=='f':
            for i in self.graph[node]:
                if i not in self.open1 and i not in self.closed1:
                    self.open1.append(i)
        else:
            for i in self.graph[node]:
                if i not in self.open2 and i not in self.closed2:
                    self.open2.append(i)

    def bidi(self,start,goal):
        self.start = start
        self.goal =  goal
        self.open1 = [start]
        self.closed1 = []
        self.open2 = [goal]
        self.closed2 = []
        turn = 'f'
        x = False
        while(self.open1 or x==False):
            for i in self.open1:
                if i in self.open2:
                    x = True
                    self.closed1.append(i)
                    res = self.closed1 + self.closed2[::-1]
                    print(res)
                    return
            else:
                if turn=='f':
                    k = self.open1.pop(0)
                    if k not in self.closed1:
                        self.closed1.append(k)
                        self.bfs(k,turn)
                    turn = turn[0:0] + 'b'
                else:
                    k = self.open2.pop(0)
                    if k not in self.closed2:
                        self.closed2.append(k)
                        self.bfs(k,turn)
                    turn = turn[0:0] + 'f'

g = Graph()
m = int(input('enter number of edges : '))
for i in range(m):
    u,v = map(int,input('enter edge : ').split())
    g.add_edge(u,v)
start = int(input('enter start node : '))
goal = int(input('enter goal node : '))
g.bidi(start,goal)
enter number of edges : 13
enter edge : 0 1
enter edge : 0 5
enter edge : 0 2
enter edge : 0 11
enter edge : 5 6
enter edge : 5 7
enter edge : 7 8
enter edge : 1 7
enter edge : 1 3
enter edge : 3 9
enter edge : 3 4
enter edge : 2 10
enter edge : 2 12
enter start node : 5
enter goal node : 4
[5, 0, 1, 3, 4]
## Best First Search


from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        self.graph2 = defaultdict(list)
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def best_first(self,start,goal,graph2):
        open,closed = [],[]
        for i in graph2:
            if i[0]==start:
                open.append([start,i[1]])
        u = start
        while open:
            open.sort(key=lambda i:i[1])
            u,v = open.pop(0)
            closed.append([u,v])
            if u==goal:
                print(u,'\topen - ',open,'\tclosed - ',closed)
                print('\nGoal node found')
                return
            for i in self.graph[u]:
                for k in graph2:
                    if k[0]==i:
                        if [i,k[1]] not in open and [i,k[1]] not in closed:
                            open.append([i,k[1]])
            print(u,'\topen - ',open,'\tclosed - ',closed)
            
    
g = Graph()
graph2 = []
m = int(input('enter number of nodes : '))
for i in range(m):
    node,h = map(int,input('enter node with heuristic value : ').split())
    graph2.append([node,h])
n = int(input('enter number of edges : '))
for i in range(n):
    u,v = map(int,input('enter edge :').split())
    g.add_edge(u,v)
start = int(input('enter start node : '))
goal = int(input('enter goal node : '))
print()
g.best_first(start,goal,graph2)
enter number of nodes : 13
enter node with heuristic value : 1 10
enter node with heuristic value : 2 4
enter node with heuristic value : 3 5
enter node with heuristic value : 4 6
enter node with heuristic value : 5 8
enter node with heuristic value : 6 7
enter node with heuristic value : 7 9
enter node with heuristic value : 8 5
enter node with heuristic value : 9 10
enter node with heuristic value : 10 11
enter node with heuristic value : 11 7
enter node with heuristic value : 12 4
enter node with heuristic value : 13 0
enter number of edges : 12
enter edge :1 2
enter edge :1 3
enter edge :1 4
enter edge :2 5
enter edge :2 6
enter edge :2 7
enter edge :3 8
enter edge :4 9
enter edge :4 10
enter edge :5 11
enter edge :6 12
enter edge :6 13
enter start node : 1
enter goal node : 13

1 	open -  [[2, 4], [3, 5], [4, 6]] 	closed -  [[1, 10]]
2 	open -  [[3, 5], [4, 6], [5, 8], [6, 7], [7, 9]] 	closed -  [[1, 10], [2, 4]]
3 	open -  [[4, 6], [6, 7], [5, 8], [7, 9], [8, 5]] 	closed -  [[1, 10], [2, 4], [3, 5]]
8 	open -  [[4, 6], [6, 7], [5, 8], [7, 9]] 	closed -  [[1, 10], [2, 4], [3, 5], [8, 5]]
4 	open -  [[6, 7], [5, 8], [7, 9], [9, 10], [10, 11]] 	closed -  [[1, 10], [2, 4], [3, 5], [8, 5], [4, 6]]
6 	open -  [[5, 8], [7, 9], [9, 10], [10, 11], [12, 4], [13, 0]] 	closed -  [[1, 10], [2, 4], [3, 5], [8, 5], [4, 6], [6, 7]]
13 	open -  [[12, 4], [5, 8], [7, 9], [9, 10], [10, 11]] 	closed -  [[1, 10], [2, 4], [3, 5], [8, 5], [4, 6], [6, 7], [13, 0]]

Goal node found
## Simple Hill Climbing


from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        self.graph2 = defaultdict(list)
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def simple_hc(self,start,goal,graph2):
        open,closed = [],[]
        for i in graph2:
            if i[0]==start:
                open.append([start,i[1]])
        u = start
        while open:
            succ = []
            u,v = open.pop(0)
            closed.append([u,v])
            if u==goal:
                print(u,'\topen - ',open,'\tclosed - ',closed)
                print('\nGoal node found')
                return
            for i in self.graph[u]:
                for k in graph2:
                    if k[0]==i:
                        if [i,k[1]] not in open and [i,k[1]] not in closed:
                            succ.append([i,k[1]])
            succ.sort(key=lambda z:z[1])
            open = succ + open
            print(u,'\topen - ',open,'\tclosed - ',closed)
            
    
g = Graph()
graph2 = []
m = int(input('enter number of nodes : '))
for i in range(m):
    node,h = map(int,input('enter node with heuristic value : ').split())
    graph2.append([node,h])
n = int(input('enter number of edges : '))
for i in range(n):
    u,v = map(int,input('enter edge :').split())
    g.add_edge(u,v)
start = int(input('enter start node : '))
goal = int(input('enter goal node : '))
print()
g.simple_hc(start,goal,graph2)
enter number of nodes : 12
enter node with heuristic value : 1 10
enter node with heuristic value : 2 10
enter node with heuristic value : 4 4
enter node with heuristic value : 5 5
enter node with heuristic value : 6 7
enter node with heuristic value : 7 3
enter node with heuristic value : 8 0
enter node with heuristic value : 9 6
enter node with heuristic value : 10 8
enter node with heuristic value : 11 2
enter node with heuristic value : 12 0
enter node with heuristic value : 13 0
enter number of edges : 11
enter edge :1 2
enter edge :1 10
enter edge :1 6
enter edge :2 4
enter edge :2 11
enter edge :10 12
enter edge :6 5
enter edge :6 7
enter edge :11 8
enter edge :5 9
enter edge :9 13
enter start node : 1
enter goal node : 12

1 	open -  [[6, 7], [10, 8], [2, 10]] 	closed -  [[1, 10]]
6 	open -  [[7, 3], [5, 5], [10, 8], [2, 10]] 	closed -  [[1, 10], [6, 7]]
7 	open -  [[5, 5], [10, 8], [2, 10]] 	closed -  [[1, 10], [6, 7], [7, 3]]
5 	open -  [[9, 6], [10, 8], [2, 10]] 	closed -  [[1, 10], [6, 7], [7, 3], [5, 5]]
9 	open -  [[13, 0], [10, 8], [2, 10]] 	closed -  [[1, 10], [6, 7], [7, 3], [5, 5], [9, 6]]
13 	open -  [[10, 8], [2, 10]] 	closed -  [[1, 10], [6, 7], [7, 3], [5, 5], [9, 6], [13, 0]]
10 	open -  [[12, 0], [2, 10]] 	closed -  [[1, 10], [6, 7], [7, 3], [5, 5], [9, 6], [13, 0], [10, 8]]
12 	open -  [[2, 10]] 	closed -  [[1, 10], [6, 7], [7, 3], [5, 5], [9, 6], [13, 0], [10, 8], [12, 0]]

Goal node found
## Beam Search


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.graph2 = defaultdict(list)
           
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
       
    def generate_child(self,graph2,u,open,closed,w_open):
        for i in self.graph[u]:
            for k in graph2:
                if k[0]==i:
                    if [i,k[1]] not in closed and [i,k[1]] not in open:
                        open.append([i,k[1]])
        print(open,'\t',w_open,'\t',closed)
   
    def beam(self,start,goal,graph2,w):
        open,w_open,closed = [],[],[]
        u = start
        z = 0
        while(z<1):
            open.append([start,0])
            print(open,'\t',w_open,'\t',closed)
            open.pop(0)
            closed.append([start,0])
            self.generate_child(graph2,u,open,closed,w_open)
            z = 1
        while(open):
            open.sort(key = lambda x: x[1])
            if(w>len(open)):
                w = len(open)
            for i in range(w):
                w_open.append(open.pop(0))
            open.clear()
            if(w>len(w_open)):
                w = len(w_open)
            for i in range(w):
                print(open,'\t',w_open,'\t',closed)
                u,v = w_open.pop(0)
                closed.append([u,v])
                if u==goal:
                    print('\nGoal node found!!!\n')
                    return
                self.generate_child(graph2,u,open,closed,w_open)
               
g = Graph()
graph2 = []
m = int(input('enter number of nodes : '))
for i in range(m):
    node,h = map(int,input('enter node with heuristic value : ').split())
    graph2.append([node,h])
n = int(input('enter number of edges : '))
for i in range(n):
    u,v = map(int,input('enter edge : ').split())
    g.add_edge(u,v)
start = int(input('enter start node : '))
goal = int(input('enter goal node : '))
w = int(input('enter W value : '))
print()
g.beam(start,goal,graph2,w)
enter number of nodes : 18
enter node with heuristic value : 1 0
enter node with heuristic value : 2 10
enter node with heuristic value : 3 13
enter node with heuristic value : 4 9
enter node with heuristic value : 5 7
enter node with heuristic value : 6 11
enter node with heuristic value : 7 8
enter node with heuristic value : 8 9
enter node with heuristic value : 9 4
enter node with heuristic value : 10 12
enter node with heuristic value : 11 9
enter node with heuristic value : 12 5
enter node with heuristic value : 13 7
enter node with heuristic value : 14 10
enter node with heuristic value : 15 12
enter node with heuristic value : 16 4
enter node with heuristic value : 17 3
enter node with heuristic value : 18 9
enter number of edges : 17
enter edge : 1 2
enter edge : 1 3
enter edge : 1 4
enter edge : 2 5
enter edge : 2 6
enter edge : 3 7
enter edge : 4 8
enter edge : 4 9
enter edge : 4 10
enter edge : 5 11
enter edge : 5 12
enter edge : 6 13
enter edge : 7 14
enter edge : 8 15
enter edge : 9 16
enter edge : 9 17
enter edge : 10 18
enter start node : 1
enter goal node : 17
enter W value : 2

[[1, 0]] 	 [] 	 []
[[2, 10], [3, 13], [4, 9]] 	 [] 	 [[1, 0]]
[] 	 [[4, 9], [2, 10]] 	 [[1, 0]]
[[8, 9], [9, 4], [10, 12]] 	 [[2, 10]] 	 [[1, 0], [4, 9]]
[[8, 9], [9, 4], [10, 12]] 	 [[2, 10]] 	 [[1, 0], [4, 9]]
[[8, 9], [9, 4], [10, 12], [5, 7], [6, 11]] 	 [] 	 [[1, 0], [4, 9], [2, 10]]
[] 	 [[9, 4], [5, 7]] 	 [[1, 0], [4, 9], [2, 10]]
[[16, 4], [17, 3]] 	 [[5, 7]] 	 [[1, 0], [4, 9], [2, 10], [9, 4]]
[[16, 4], [17, 3]] 	 [[5, 7]] 	 [[1, 0], [4, 9], [2, 10], [9, 4]]
[[16, 4], [17, 3], [11, 9], [12, 5]] 	 [] 	 [[1, 0], [4, 9], [2, 10], [9, 4], [5, 7]]
[] 	 [[17, 3], [16, 4]] 	 [[1, 0], [4, 9], [2, 10], [9, 4], [5, 7]]

Goal node found!!!

## Branch and Bound 


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        
    def add_edge(self,u,v,w):
        self.graph[u].append([v,w])
        self.graph[v].append([u,w])
       
    def branch(self,start,goal):
        self.open=[]
        self.closed=[]
        self.open.append([start,0])
        while(self.open):
            self.open=sorted(self.open,key=lambda i:i[1])
            u,v=self.open.pop(0)
            if u==goal:
                self.closed.append(u)
                print(u,'\topen - ',self.open,'\tclosed - ',self.closed)
                print("\nGoal node found\n")
                return
            self.closed.append(u)
            for i in self.graph[u]:
                i[1]=v+i[1]
                self.open.append(i)
            print(u,'\topen - ',self.open,'\tclosed - ',self.closed)
                           
g=Graph()
n=int(input("enter no.of edges : "))
for i in range(n):
    u,v,w=map(int,input("enter edge and edge weight : ").split())
    g.add_edge(u,v,w)
start = int(input('enter start node : '))
goal = int(input('enter goal node : '))
print()
g.branch(start,goal)
print()
enter no.of edges : 9
enter edge and edge weight : 1 2 5
enter edge and edge weight : 1 3 7
enter edge and edge weight : 1 6 9
enter edge and edge weight : 2 4 4
enter edge and edge weight : 2 5 6
enter edge and edge weight : 3 4 8
enter edge and edge weight : 3 5 5
enter edge and edge weight : 4 6 3
enter edge and edge weight : 5 6 2
enter start node : 1
enter goal node : 6

1 	open -  [[2, 5], [3, 7], [6, 9]] 	closed -  [1]
2 	open -  [[3, 7], [6, 9], [1, 10], [4, 9], [5, 11]] 	closed -  [1, 2]
3 	open -  [[6, 9], [4, 9], [1, 10], [5, 11], [1, 14], [4, 15], [5, 12]] 	closed -  [1, 2, 3]
6 	open -  [[4, 9], [1, 10], [5, 11], [5, 12], [1, 14], [4, 15]] 	closed -  [1, 2, 3, 6]

Goal node found


## 8 Puzzle


from collections import defaultdict

class Graph:
    def __init__(self):
        self.start=defaultdict(list)
        self.goal=defaultdict(list)
        self.x = defaultdict(list)
        self.d = {
            0: [1,3],
            1: [0,2,4],
            2: [1,5],
            3: [0,4,6],
            4: [1,3,5,7],
            5: [2,4,8],
            6: [3,7],
            7: [4,6,8],
            8: [5,7]
        }
       
    def addS(self,start):
        self.start = start;
       
    def addG(self,goal):
        self.goal = goal;       
       
    def h(self,x,gl):
        count = 0
        for i in range(9):
            if x[i]!=gl[i]:
                count = count + 1
        if(count==0):
            return 0
        return count-1
       
    def find(self,x):
        i = x.index('0')
        return i
           
    def form(self,x):
        z = ''
        for i in range(len(x)):
            z = z + str(x[i])
        return z
   
    def convertS(self,x):
        list1 = []
        list1[:0] = x
        return list1
   
    def genC(self,x,ind,pos):
        list2 = x.copy()
        list2[ind],list2[pos] = list2[pos],list2[ind]
        return list2
       
    def best_first(self):
        st = self.form(self.start)
        gl = self.form(self.goal)
        ch = st[:]
        self.open=[[ch,self.h(ch,gl)]]
        self.closed=[]
        while(self.open):
            self.open=sorted(self.open,key=lambda i:i[1])
            ##print('open - ',self.open,'\tclosed - ',self.closed)
            u,v=self.open.pop(0)
            self.closed.append(u)
            if u==gl:
                print("\nGoal node found")
                print('closed - ',self.closed)
#                 print('open - ',self.open,'\tclosed - ',self.closed)
                return
            index = self.find(u)
            le = len(self.d[index])
            l1 = self.convertS(u)
            for i in range(le):
                l2 = self.genC(l1,index,self.d[index][i])
                q = self.form(l2)
                if q not in self.closed:
                    self.open.append([q,self.h(q,gl)])
            ##print('open - ',self.open,'\tclosed - ',self.closed)
            ##print()
            
    def do(self,u,gl):
        index = self.find(u)
        le = len(self.d[index])
        l1 = self.convertS(u)
        for i in range(le):
            l2 = self.genC(l1,index,self.d[index][i])
            q = self.form(l2)
            if q not in self.closed:
                self.open.append([q,self.h(q,gl)])
            
    def beam(self,w):
        st = self.form(self.start)
        gl = self.form(self.goal)
        ch = st[:]
        self.open=[]
        self.closed=[]
        self.w_open = []
        u = ch
        z = 0
        while(z<1):
            self.open.append([ch,self.h(ch,gl)])
            ##print('open - ',self.open,'\tw_open - ',self.w_open,'\tclosed - ',self.closed)
            self.open.pop(0)
            self.closed.append(u)
            self.do(u,gl)
            z = 1
        print('open - ',self.open,'\tw_open - ',self.w_open,'\tclosed - ',self.closed)
        print()
        while(u!=gl):
            self.open=sorted(self.open,key=lambda i:i[1])
            ##print('\nopen - ',self.open,'\tw_open - ',self.w_open,'\tclosed - ',self.closed)
            if(w>len(self.open)):
                w = len(self.open)
            for i in range(w):
                self.w_open.append(self.open.pop(0))
            self.open.clear()
            if(w>len(self.w_open)):
                w = len(self.w_open)
            for i in range(w):
                ##print('\nopen - ',self.open,'\tw_open - ',self.w_open,'\tclosed - ',self.closed)
                u,v = self.w_open.pop(0)
                self.closed.append(u)
                if u==gl:
                    print('\nGoal node found!!!\n')
                    print('closed - ',self.closed)
                    return
                self.do(u,gl)
                ##print('open - ',self.open,'\tw_open - ',self.w_open,'\tclosed - ',self.closed)
                
    def simple_hc(self):
        st = self.form(self.start)
        gl = self.form(self.goal)
        ch = st[:]
        self.open=[[ch,self.h(ch,gl)]]
        self.closed=[]
        while(self.open):
            self.succ=[]
            ##print('open - ',self.open,'\tclosed - ',self.closed)
            u,v=self.open.pop(0)
            self.closed.append(u)
            if u==gl:
                print("\nGoal node found")
                print('closed - ',self.closed)
                ##print('open - ',self.open,'\tclosed - ',self.closed)
                return
            index = self.find(u)
            le = len(self.d[index])
            l1 = self.convertS(u)
            for i in range(le):
                l2 = self.genC(l1,index,self.d[index][i])
                q = self.form(l2)
                if q not in self.closed:
                    self.succ.append([q,self.h(q,gl)])
            self.succ=sorted(self.succ,key=lambda i:i[1])
            self.open = self.succ + self.open
            ##print()
            
    def branch(self):
        st = self.form(self.start)
        gl = self.form(self.goal)
        ch = st[:]
        self.open=[[ch,0]]
        self.closed=[]
        while(self.open):
            self.open=sorted(self.open,key=lambda i:i[1])
            ##print('open - ',self.open,'\tclosed - ',self.closed)
            u,v=self.open.pop(0)
            self.closed.append(u)
            if u==gl:
                print("\nGoal node found")
                print('closed - ',self.closed)
                ##print('open - ',self.open,'\tclosed - ',self.closed)
                return
            index = self.find(u)
            le = len(self.d[index])
            l1 = self.convertS(u)
            for i in range(le):
                l2 = self.genC(l1,index,self.d[index][i])
                q = self.form(l2)
                if q not in self.closed:
                    self.open.append([q,v+1])
            ##print('open - ',self.open,'\tclosed - ',self.closed)
            ##print()
                               
   
g = Graph()
start = input('enter start state : ')
g.addS(g.convertS(start))
goal = input('enter goal state : ')
g.addG(g.convertS(goal))
print()
choice = input('Best-First-Search(b/B) or Beam-Search(bs) or Simple-Hill-Climbing(s/S) or Branch-and-Bound(bb)?? - ')
print()
if(choice=='b' or choice=='B'):
    print('Best First Search\n')
    g.best_first()
elif(choice=='bs'):
    w = int(input('enter W value : '))
    print('\nBeam Search\n')
    g.beam(w)
elif(choice=='s' or choice=='S'):
    print('Simple Hill Climbing\n')
    g.simple_hc()
elif(choice=='bb'):
    print('Branch and Bound\n')
    g.branch()
enter start state : 123046758
enter goal state : 123456780

Best-First-Search(b/B) or Beam-Search(bs) or Simple-Hill-Climbing(s/S) or Branch-and-Bound(bb)?? - b

Best First Search


Goal node found
closed -  ['123046758', '123406758', '123456708', '123456780']
## 8 puzzle using A*


from collections import defaultdict

class Graph:
    def __init__(self):
        self.start=defaultdict(list)
        self.goal=defaultdict(list)
        self.x = defaultdict(list)
        self.d = {
            0: [1,3],
            1: [0,2,4],
            2: [1,5],
            3: [0,4,6],
            4: [1,3,5,7],
            5: [2,4,8],
            6: [3,7],
            7: [4,6,8],
            8: [5,7]
        }
       
    def addS(self,start):
        self.start = start;
       
    def addG(self,goal):
        self.goal = goal;            
       
    def h(self,x,gl):
        count = 0
        for i in range(9):
            if x[i]!=gl[i]:
                count = count + 1
        if(count==0):
            return 0
        return count-1
       
    def find(self,x):
        i = x.index('0')
        return i
           
    def form(self,x):
        z = ''
        for i in range(len(x)):
            z = z + str(x[i])
        return z
   
    def convertS(self,x):
        list1 = []
        list1[:0] = x
        return list1
   
    def genC(self,x,ind,pos):
        list2 = x.copy()
        list2[ind],list2[pos] = list2[pos],list2[ind]
        return list2
       
    def A_Star_8(self):
        st = self.form(self.start)
        gl = self.form(self.goal)
        ch = st[:]
        self.open=[[ch,0,self.h(ch,gl)]]
        self.closed=[]
        while(self.open):
            self.open=sorted(self.open,key=lambda i:i[1]+i[2])
            ##print('open - ',self.open,'\tclosed - ',self.closed)
            u,v,w=self.open.pop(0)
            self.closed.append(u)
            if u==gl:
                print("\nGoal node found")
                print('closed - ',self.closed)
                return
            index = self.find(u)
            le = len(self.d[index])
            l1 = self.convertS(u)
            for i in range(le):
                l2 = self.genC(l1,index,self.d[index][i])
                q = self.form(l2)
                if q not in self.closed:
                    self.open.append([q,v+1,self.h(q,gl)])
            ##print('open - ',self.open,'\tclosed - ',self.closed)
            ##print()
                               
   
g = Graph()
start = input('enter start state : ')
g.addS(g.convertS(start))
goal = input('enter goal state : ')
g.addG(g.convertS(goal))
print()
g.A_Star_8()
enter start state : 123046758
enter goal state : 123456780


Goal node found
closed -  ['123046758', '123406758', '123456708', '123456780']
## A* Search
