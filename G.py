import time
import random
import math
q=True
g=''
count=0
game,sec,gamma,bro=True,3,'',1
playerhp,playerstock,pmhp,pmap,pGalliform=100,0,0,0,0
AIhp,AIstock,AImhp,AIap,AIGalliform=100,0,0,0,0
Palert=True
AIalert=True
sample_key=('1010')
t=1
bolo=0
AIchoc=('xplor','xtract')
menu=('~','!','@','#','$','%')
lmap=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
rmap=[]
loca=''
ry=''
list1=(0,5,10,20)
tup=('Search which location? (type "stop" to abort) :- ','Extract which location? (type "stop" to abort):- ')
start=True
slevel=(100,60,20)
alevel=(5,20,50)
A=list1[random.randrange(0,4)]
B=list1[random.randrange(0,4)]
C=list1[random.randrange(0,4)]
D=list1[random.randrange(0,4)]
E=list1[random.randrange(0,4)]
F=list1[random.randrange(0,4)]
G=list1[random.randrange(0,4)]
H=list1[random.randrange(0,4)]
I=list1[random.randrange(0,4)]
J=list1[random.randrange(0,4)]
K=list1[random.randrange(0,4)]
L=list1[random.randrange(0,4)]
M=list1[random.randrange(0,4)]
N=list1[random.randrange(0,4)]
O=list1[random.randrange(0,4)]
P=list1[random.randrange(0,4)]
Q=list1[random.randrange(0,4)]
R=list1[random.randrange(0,4)]
S=list1[random.randrange(0,4)]
T=list1[random.randrange(0,4)]
U=list1[random.randrange(0,4)]
V=list1[random.randrange(0,4)]
W=list1[random.randrange(0,4)]
X=list1[random.randrange(0,4)]
Y=list1[random.randrange(0,4)]
Z=list1[random.randrange(0,4)]

def ETX(x,gamma,size,t):
    global playerstock,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
    if gamma == 'A':
        if x == 'xplor':
            print('\nYou have discovered',id(A),'\nResource available:-',A)
        else:
            if A == 0:
                print('\nLocation',gamma,'doesn\'t has any resource')
            else:
                print('Extraction has started')
                for i in range(0,A):
                    playerstock+=1
                    #time.sleep(t)
                A=0
                print('Stocks updated!!!','\nYour stock :-',playerstock)

    elif gamma == 'B':
        if x == 'xplor':
            print('\nYou have discovered',id(B),'\nResource available:-',B)
        else:
            if B == 0:
                print('\nLocation',gamma,'doesn\'t has any resource')
            else:
                print('Extraction has started')
                for i in range(0,B):
                    playerstock+=1
                    #time.sleep(t)
                B=0
                print('Stocks updated!!!','\nYour stock :-',playerstock)

    elif gamma == 'C':
        if x == 'xplor':
            print('\nYou have discovered',id(C),'\nResource available:-',C)
        else:
            if C == 0:
                print('\nLocation',gamma,'doesn\'t has any resource')
            else:
                print('Extraction has started')
                for i in range(0,C):
                    playerstock+=1
                    #time.sleep(t)
                C=0
                print('Stocks updated!!!','\nYour stock :-',playerstock)

    elif gamma == 'D':
        if x == 'xplor':
            print('\nYou have discovered',id(D),'\nResource available:-',D)
        else:
            if D == 0:
                print('\nLocation',gamma,'doesn\'t has any resource')
            else:
                print('Extraction has started')
                for i in range(0,D):
                    playerstock+=1
                    #time.sleep(t)
                D=0
                print('Stocks updated!!!','\nYour stock :-',playerstock)

    elif gamma == 'E':
        if x == 'xplor':
            print('\nYou have discovered',id(E),'\nResource available:-',E)
        else:
            if E == 0:
                print('\nLocation',gamma,'doesn\'t has any resource')
            else:
                print('Extraction has started')
                for i in range(0,E):
                    playerstock+=1
                    #time.sleep(t)
                E=0
                print('Stocks updated!!!','\nYour stock :-',playerstock)
    elif gamma == 'F':
        if x == 'xplor':
            print('\nYou have discovered',id(F),'\nResource available:-',F)
        else:
            if F == 0:
                print('\nLocation',gamma,'doesn\'t has any resource')
            else:
                print('Extraction has started')
                for i in range(0,F):
                    playerstock+=1
                    #time.sleep(t)
                F=0
                print('Stocks updated!!!','\nYour stock :-',playerstock)

    elif gamma == 'G':
        if x == 'xplor':
            print('\nYou have discovered',id(G),'\nResource available:-',G)
        else:
            if G == 0:
                print('\nLocation',gamma,'doesn\'t has any resource')
            else:
                print('Extraction has started')
                for i in range(0,G):
                    playerstock+=1
                    #time.sleep(t)
                G=0
                print('Stocks updated!!!','\nYour stock :-',playerstock)

    elif gamma == 'H':
        if x == 'xplor':
            print('\nYou have discovered',id(H),'\nResource available:-',H)
        else:
            if H == 0:
                print('\nLocation',gamma,'doesn\'t has any resource')
            else:
                print('Extraction has started')
                for i in range(0,H):
                    playerstock+=1
                    #time.sleep(t)
                H=0
                print('Stocks updated!!!','\nYour stock :-',playerstock)

    elif gamma == 'I':
        if x == 'xplor':
            print('\nYou have discovered',id(I),'\nResource available:-',I)
        else:
            if I == 0:
                print('\nLocation',gamma,'doesn\'t has any resource')
            else:
                print('Extraction has started')
                for i in range(0,I):
                    playerstock+=1
                    #time.sleep(t)
                I=0
                print('Stocks updated!!!','\nYour stock :-',playerstock)

    elif gamma == 'J':
        if size in (4,5):
            if x == 'xplor':
                print('\nYou have discovered',id(J),'\nResource available:-',J)
            else:
                if J == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,J):
                        playerstock+=1
                        #time.sleep(t)
                    J=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
            print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'K':
        if size in (4,5):
            if x == 'xplor':
                print('\nYou have discovered',id(K),'\nResource available:-',K)
            else:
                if K == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,K):
                        playerstock+=1
                        #time.sleep(t)
                    K=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)
        else:
            print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'L':
        if size in (4,5):
            if x == 'xplor':
                print('\nYou have discovered',id(L),'\nResource available:-',L)
            else:
                if L == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,L):
                        playerstock+=1
                        #time.sleep(t)
                    L=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
            print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'M':
        if size in (4,5):
            if x == 'xplor':
                print('\nYou have discovered',id(M),'\nResource available:-',M)
            else:
                if J == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,J):
                        playerstock+=1
                        #time.sleep(t)
                    M=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
            print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'N':
        if size in (4,5):
            if x == 'xplor':
                print('\nYou have discovered',id(N),'\nResource available:-',N)
            else:
                if N == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,N):
                        playerstock+=1
                        #time.sleep(t)
                    N=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
          print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'O':
        if size in (4,5):
            if x == 'xplor':
                print('\nYou have discovered',id(O),'\nResource available:-',O)
            else:
                if O == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,O):
                        playerstock+=1
                        #time.sleep(t)
                    O=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
          print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'P':
        if size in (4,5):
            if x == 'xplor':
                print('\nYou have discovered',id(P),'\nResource available:-',P)
            else:
                if P == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,P):
                        playerstock+=1
                        #time.sleep(t)
                        P=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
          print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'Q':
        if size in (5,):
            if x == 'xplor':
                print('\nYou have discovered',id(Q),'\nResource available:-',Q)
            else:
                if Q == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,Q):
                        playerstock+=1
                        #time.sleep(t)
                    Q=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
          print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'R':
        if size in (5,):
            if x == 'xplor':
                print('\nYou have discovered',id(R),'\nResource available:-',R)
            else:
                if R == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,R):
                        playerstock+=1
                        #time.sleep(t)
                    R=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
          print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'S':
        if size in (5,):
            if x == 'xplor':
                print('\nYou have discovered',id(S),'\nResource available:-',S)
            else:
                if S == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,S):
                        playerstock+=1
                        #time.sleep(t)
                    S=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
          print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'T':
        if size in (5,):
            if x == 'xplor':
                print('\nYou have discovered',id(T),'\nResource available:-',T)
            else:
                if T == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,T):
                        playerstock+=1
                        #time.sleep(t)
                    T=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
          print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'U':
        if size in (5,):
            if x == 'xplor':
                print('\nYou have discovered',id(U),'\nResource available:-',U)
            else:
                if U == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,U):
                        playerstock+=1
                        #time.sleep(t)
                    U=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)
        else:
          print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'V':
        if size in (5,):
            if x == 'xplor':
                print('\nYou have discovered',id(V),'\nResource available:-',V)
            else:
                if V == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,V):
                        playerstock+=1
                        #time.sleep(t)
                    V=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
          print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'W':
        if size in (5,):
            if x == 'xplor':
                print('\nYou have discovered',id(W),'\nResource available:-',W)
            else:
                if W == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,W):
                        playerstock+=1
                        #time.sleep(t)
                    W=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
          print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'X':
        if size in (5,):
            if x == 'xplor':
                print('\nYou have discovered',id(X),'\nResource available:-',X)
            else:
                if X == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,X):
                        playerstock+=1
                        #time.sleep(t)
                    X=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
          print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'Y':
        if size in (5,):
            if x == 'xplor':
                print('\nYou have discovered',id(Y),'\nResource available:-',Y)
            else:
                if Y == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                    for i in range(0,Y):
                        playerstock+=1
                        #time.sleep(t)
                    Y=0
                    print('Stocks updated!!!','\nYour stock :-',playerstock)

        else:
          print('\nLocation',gamma,'doesn\'t exist')
    elif gamma == 'Z':
        if size in (5,):
            if x == 'xplor':
                print('\nYou have discovered',id(Z),'\nResource available:-',Z)
            else:
                if Z == 0:
                    print('\nLocation',gamma,'doesn\'t has any resource')
                else:
                    print('Extraction has started')
                for i in range(0,Z):
                    playerstock+=1
                    #time.sleep(t)
                Z=0
                print('Stocks updated!!!','\nYour stock :-',playerstock)
        else:
          print('\nLocation',gamma,'doesn\'t exist')
    else:
        if gamma == 'stop':
            print('\nSearch Aborted')

        else:
            print('\nInvalid Input')



def Brain1():
    global AIstock,rmap,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
    if len(rmap) >= 1:
        ry=AIchoc[1]
        loca=rmap[-1]
    else:
        ry=AIchoc[0]
        loca=random.choice(lmap)
    if loca == 'A':
        if ry == 'xplor':
            if A != 0:
                rmap.append('A')
            else:
                loca=random.choice(lmap)
        else:
            if 'A' in rmap:
                AIstock+=A
                rmap.remove('A')
                A=0
    elif loca == 'B':
        if ry == 'xplor':
            if B != 0:
                rmap.append('B')
            else:
                loca=random.choice(lmap)
        else:
            if 'B' in rmap:
                AIstock+=B
                rmap.remove('B')
                B=0
    elif loca == 'C':
        if ry == 'xplor':
            if C != 0:
                rmap.append('C')
            else:
                loca=random.choice(lmap)
        else:
            if 'C' in rmap:
                AIstock+=C
                rmap.remove('C')
                C=0
    elif loca == 'D':
        if ry == 'xplor':
            if D != 0:
                rmap.append('D')
            else:
                loca=random.choice(lmap)
        else:
            if 'D' in rmap:
                AIstock+=D
                rmap.remove('D')
                D=0
    elif loca == 'E':
        if ry == 'xplor':
            if E != 0:
                rmap.append('E')
            else:
                loca=random.choice(lmap)
        else:
            if 'E' in rmap:
                AIstock+=E
                rmap.remove('E')
                E=0
    elif loca == 'F':
        if ry == 'xplor':
            if F != 0:
                rmap.append('F')
            else:
                loca=random.choice(lmap)
        else:
            if 'F' in rmap:
                AIstock+=F
                rmap.remove('F')
                F=0
    elif loca == 'G':
        if ry == 'xplor':
            if G != 0:
                rmap.append('G')
            else:
                loca=random.choice(lmap)
        else:
            if 'G' in rmap:
                AIstock+=G
                rmap.remove('G')
                G=0
    elif loca == 'H':
        if ry == 'xplor':
            if H != 0:
                rmap.append('H')
            else:
                loca=random.choice(lmap)
        else:
            if 'H' in rmap:
                AIstock+=H
                rmap.remove('H')
                H=0
    elif loca == 'I':
        if ry == 'xplor':
            if I != 0:
                rmap.append('I')
            else:
                loca=random.choice(lmap)
        else:
            if 'I' in rmap:
                AIstock+=B
                rmap.remove('I')
                I=0
    elif loca == 'J':
        if ry == 'xplor':
            if J != 0:
                rmap.append('J')
            else:
                loca=random.choice(lmap)
        else:
            if 'J' in rmap:
                AIstock+=C
                rmap.remove('J')
                J=0
    elif loca == 'K':
        if ry == 'xplor':
            if K != 0:
                rmap.append('K')
            else:
                loca=random.choice(lmap)
        else:
            if 'K' in rmap:
                AIstock+=K
                rmap.remove('K')
                K=0
    elif loca == 'L':
        if ry == 'xplor':
            if L != 0:
                rmap.append('L')
            else:
                loca=random.choice(lmap)
        else:
            if 'L' in rmap:
                AIstock+=L
                rmap.remove('L')
                L=0
    elif loca == 'M':
        if ry == 'xplor':
            if M != 0:
                rmap.append('M')
            else:
                loca=random.choice(lmap)
        else:
            if 'M' in rmap:
                AIstock+=M
                rmap.remove('M')
                M=0
    elif loca == 'N':
        if ry == 'xplor':
            if N != 0:
                rmap.append('N')
            else:
                loca=random.choice(lmap)
        else:
            if 'N' in rmap:
                AIstock+=N
                rmap.remove('N')
                N=0
    elif loca == 'O':
        if ry == 'xplor':
            if O != 0:
                rmap.append('O')
            else:
                loca=random.choice(lmap)
        else:
            if 'O' in rmap:
                AIstock+=H
                rmap.remove('O')
                O=0
    elif loca == 'P':
        if ry == 'xplor':
            if P != 0:
                rmap.append('P')
            else:
                loca=random.choice(lmap)
        else:
            if 'P' in rmap:
                AIstock+=P
                rmap.remove('P')
                P=0
    elif loca == 'Q':
        if ry == 'xplor':
            if Q != 0:
                rmap.append('Q')
            else:
                loca=random.choice(lmap)
        else:
            if 'Q' in rmap:
                AIstock+=Q
                rmap.remove('Q')
                Q=0
    elif loca == 'R':
        if ry == 'xplor':
            if R != 0:
                rmap.append('R')
            else:
                loca=random.choice(lmap)
        else:
            if 'R' in rmap:
                AIstock+=R
                rmap.remove('R')
                R=0
    elif loca == 'S':
        if ry == 'xplor':
            if S != 0:
                rmap.append('S')
            else:
                loca=random.choice(lmap)
        else:
            if 'S' in rmap:
                AIstock+=S
                rmap.remove('S')
                S=0
    elif loca == 'T':
        if ry == 'xplor':
            if T != 0:
                rmap.append('T')
            else:
                loca=random.choice(lmap)
        else:
            if 'T' in rmap:
                AIstock+=T
                rmap.remove('T')
                T=0
    elif loca == 'U':
        if ry == 'xplor':
            if U != 0:
                rmap.append('U')
            else:
                loca=random.choice(lmap)
        else:
            if 'U' in rmap:
                AIstock+=U
                rmap.remove('U')
                U=0
    elif loca == 'V':
        if ry == 'xplor':
            if V != 0:
                rmap.append('V')
            else:
                loca=random.choice(lmap)
        else:
            if 'V' in rmap:
                AIstock+=V
                rmap.remove('V')
                V=0
    elif loca == 'W':
        if ry == 'xplor':
            if W != 0:
                rmap.append('W')
            else:
                loca=random.choice(lmap)
        else:
            if 'W' in rmap:
                AIstock+=W
                rmap.remove('W')
                W=0
    elif loca == 'X':
        if ry == 'xplor':
            if X != 0:
                rmap.append('X')
            else:
                loca=random.choice(lmap)
        else:
            if 'X' in rmap:
                AIstock+=X
                rmap.remove('X')
                X=0
    elif loca == 'Y':
        if ry == 'xplor':
            if Y != 0:
                rmap.append('Y')
            else:
                loca=random.choice(lmap)
        else:
            if 'Y' in rmap:
                AIstock+=Y
                rmap.remove('Y')
                Y=0
    elif loca == 'Z':
        if ry == 'xplor':
            if Z != 0:
                rmap.append('Z')
            else:
                loca=random.choice(lmap)
        else:
            if 'Z' in rmap:
                AIstock+=Z
                rmap.remove('Z')
                Z=0

def deldupele():
    global rmap
    dup=list()
    uni=list()
    for q in rmap:
        if q not in dup:
            uni.append(q)
            dup.append(q)
    rmap.clear()
    rmap=list(uni)
def AIbuy():
    global AIstock
    global AImhp
    global AIap
    if AIap>=AIap:
        m1=menu[random.randrange(0,3)]
        if AImhp<=0:
            mi=menu[5]
    if m1 == '~':
        if AIstock >= 3:
            AIstock-=3
            AImhp+=15
            AIap+=5
        else:
            m1=random.choice(menu)
    elif m1 == '!':
        if AIstock >= 5:
            AIstock-=5
            AImhp+=20
            AIap+=10
        else:
            m1=random.choice(menu)
    elif m1 == '@':
        if AIstock >= 10:
            AIstock-=10
            AImhp+=40
            AIap+=20
        else:
            m1=random.choice(menu)
    elif m1 == '#':
        if AIstock >= 1:
            AIstock-=1
            AIhp+=5
        else:
            m1=random.choice(menu)
    elif m1 == '$':
        if AIstock >= 15:
            AIstock-=15
            AIhp+=10
        else:
            m1=random.choice(menu)
    elif m1 == '%':
        if AIstock >= 18:
            AIstock-=18
            AImhp+=13
        else:
            m1=random.choice(menu)

def killpla(pGalliform):
    log=list(str(pGalliform))
    dbit={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100',
          '5':'0101','6':'0110','7':'0111','8':'1000','9':'1001'}
    wasd=dbit[log[0]]
    esdf=dbit[log[3]]
    rdfg=dbit[log[5]]
    tfgh=dbit[log[7]]
    para=None
    for i in range(4):
        if wasd[i]+esdf[i]+rdfg[i]+tfgh[i] == '1010':
            para=True
            break
    if para:
        print('Code matched')
    else:
        print('Code failed')
print('Pytext')
while start:
    art=input('''Press 'y' to start the game :- ''')
    if art == 'y':
        start=False
    else:
        print('''\nInvalid Input, Press 'y' ''')
while q:
    print('\nEasy','\nMedium','\nHard')
    z=input('\nGame Difficulty :- ')
    if z == 'E':
        u1=slevel[0]
        u2=alevel[0]
        q=False
    elif z == 'M':
        u1=slevel[1]
        u2=alevel[1]
        q=False
    elif z == 'H':
        u1=slevel[2]
        u2=alevel[2]
        q=False
    else:
        print('\nInvalid Input')
q=True
while q:
    size=int(input('\nMap Size :- '))
    if 3<=size<=5:
        for loop in range(0,3):
            print('|',end='')
            #time.sleep(1)
        print('\nGame has started')
        q=False
    else:
        print('''\nMap Size should be 3, 4 and 5''')
while game:
    Brain1()
    deldupele()
    gamma=''
    x=input('\nEnter your command (type "help"):- ')
    if x == 'xplor' or x == 'xtract':
        if x == 'xplor':
            j=0
        else:
            j=1
        while gamma != 'stop':
            gamma=str(input('\n'+tup[j]))
            if AIstock >= u1:
                while AIap == u2:
                    AIbuy()
            else:
                Brain1()
                deldupele()
            ETX(x,gamma,size,t)
    elif x == 'map':
        if AIstock >= u1:
            while AIap == u2:
                AIbuy()
        else:
            Brain1()
            deldupele()
        if size == 5:
            print('''.___________________.
|_A_|_B_|_C_|_D_|_E_|
|_F_|_G_|_H_|_I_|_J_|
|_K_|_L_|_M_|_N_|_O_|
|_P_|_Q_|_R_|_S_|_T_|
|_U_|_V_|_W_|_X_|_Y_|
|___|___|_Z_|___|___|''')
        elif size == 4:
            print('''._______________.
|_A_|_B_|_C_|_D_|
|_E_|_F_|_G_|_H_|
|_I_|_J_|_K_|_M_|
|_N_|_O_|_P_|_Q_|''')
        else:
            print('''.___________.
|_A_|_B_|_C_|
|_D_|_E_|_F_|
|_G_|_H_|_I_|''')
                     
    elif x == 'info':
        #time.sleep(1)
        if AIstock >= u1:
            while AIap == u2:
                AIbuy()
        else:
            Brain1()
            deldupele()
        print('\nYour Health Bar =',playerhp,'\nYour Stock =',playerstock,'\nYour Army Health Bar =',pmhp,'\nYour Army Attack Points =',pmap,'\nYour Galliformes =',pGalliform)
    elif x == 'buy':
        bro=1
        print('\nMenu list')
        #time.sleep(1)
        print('\n~ Small Army = 3','\n! Medium Army = 5','\n@ Large Army = 10','\n# Heal Point = 1','\n$ Heal Serum = 15','\n% Army Heal Serum = 18','\n& Extraction Speed = 14')
        #time.sleep(1)
        print('\nYour Stock =',playerstock)
        if AIstock >= u1:
            while AIap == u2:
                AIbuy()
        else:
            Brain1()
            deldupele()
        while bro == 1:
            buy=input('\nWhich one to buy? ')
            if buy == '~':
                if playerstock >= 3:
                    playerstock-=3
                    pmhp+=15
                    pmap+=5
                    print('\nYou have bought a Small Army')
                    print('Your Stock =',playerstock)
                else:
                    print('\nLow Balance')
            elif buy == '!':
                if playerstock >= 5:
                    playerstock-=5
                    pmhp+=20
                    pmap+=10
                    print('\nYou have bought a Medium Army')
                    print('Your Stock =',playerstock)
                else:
                    print('\nLow Balance')
            elif buy == '@':
                if playerstock >= 10:
                    playerstock-=10
                    pmhp+=40
                    pmap+=20
                    print('\nYou have bought a Large Army')
                    print('Your Stock =',playerstock)
                else:
                    print('\nLow Balance')
            elif buy == '#':
                if playerstock >= 1:
                    playerstock-=1
                    playerhp+=5
                    print('\nYou have bought a Heal point')
                    print('Your Stock =',playerstock)
                else:
                    print('\nLow Balance')
            elif buy == '$':
                if playerstock >= 15:
                    playerstock-=15
                    playerhp+=10
                    print('\nYou have bought a Heal Serum')
                    print('Your Stock =',playerstock)
                else:
                    print('\nLow Balance')
            elif buy == '%':
                if playerstock >= 18:
                    playerstock-=18
                    pmhp+=13
                    print('\nYou have bought Army Heal Serum')
                    print('Your Stock =',playerstock)
                else:
                    print('\nLow Balance')
            elif buy == '&':
                if playerstock >= 14:
                    playerstock-=14
                    t/=2
                    print('\nYou have bought an Extraction speed')
                    print('Your Stock =',playerstock)
                else:
                    print('\nLow Balance')
            elif buy == 'none':
                print('\nGame Continued')
                bro=0
            else:
                print('\nInvalid Input')
    elif x == 'quit':
        #time.sleep(2)
        print('\nGame Over ant')
        #time.sleep(2)
        game=False
    elif x == 'attack':
        bolo = 1
        while bolo == 1:
            print('\nYour Army Health Bar =',pmhp,'\nYour Army Attack Points =',pmap)
            con=input('\nPlease Confirm your COMMAND:- ')
            if con == '+':
                print('  Your Army Health   |  Enemy Army Health')    
                while not(AImhp <= 0 or pmhp <= 0):
                    AImhp,pmhp=AImhp-pmap,pmhp-AIap
                    g,j=AImhp,pmhp
                    if g<=pmap or j<=AImhp:
                        if g<=0:
                            g='Dead'
                        elif j<=0:
                            j='Dead'
                        else:
                            pass
                    else:
                        pass
                    print('        ',j,'        ','|','        ',g)
                    count+=1
                    #time.sleep(1)
                if g == 'Dead':
                    AImhp=0
                else:
                    pmhp=0
                if AImhp <= 0:
                    print('\nYou have Won the WAR')
                    pGalliform+=random.randint(0,10)*math.sin(count+math.pi/random.randrange(1,9))
                    print('You have earned',pGalliform,'Galliformes')
                else:
                    print('\nThe Emeny has Won the WAR')
                    AIGalliform+=random.randint(0,10)*math.sin(count+math.pi/random.randrange(1,9))
                bolo=0
            else:
                bolo=0
                print('\nAttack Aborted')
    elif x == 'kill':
        print('Still working')
        if input('Are u sure :- ') == 'y':
            if pGalliform > 0:
                killpla(pGalliform)
    elif x == 'help':
        print("""_Command_List_\n\n
xplor  = Explore the Sector\n
xtract = Extract Resources\n
map    = Map of the Playing World\n
info   = Player's Stats\n
buy    = Opens Store\n
attack = Attack the Enemy\n
kill   = Kill the Emeny to win\n
diplo  = Diplomacy (Work in Progress)\n
quit   = Exit the Game\n""")
    elif x == 'diplo':
        print('Watching diplomacy')
    else:
        print('\nInvalid Input')
        if AIstock >= u1:
            while AIap == u2:
                AIbuy()
        else:
            Brain1()
            deldupele()
    if AIstock >= u1 and AIap != u2:
        AIbuy()
#League of Legends Galliformes(Game birds)
