""" ABOpening: This gives the next White move for a Opening game using Alpha-Beta Pruning"""

import collections
import math
import copy
from sys import argv


def neighbors(x):
    neighbor = dict()
    neighbor[0] = [1,3,8]
    neighbor[1] = [0,2,4]
    neighbor[2] = [1, 5,13]
    neighbor[3] = [0,4,6,9]
    neighbor[4] = [1,3,5]
    neighbor[5] = [2,4,7,12]
    neighbor[6] = [3,7,10]
    neighbor[7] = [5,6,11]
    neighbor[8] = [0,9,20]
    neighbor[9] = [3,8,10,17]
    neighbor[10] = [6,9,14]
    neighbor[11] = [7,12,16]
    neighbor[12] = [5,11,13,19]
    neighbor[13] = [2,12,22]
    neighbor[14] = [10,15,17]
    neighbor[15] = [14,16,18]
    neighbor[16] = [11,15,19]
    neighbor[17] = [9,14,18,20]
    neighbor[18] = [15,17,19,21]
    neighbor[19] = [12,16,18,22]
    neighbor[20] = [8,17,21]
    neighbor[21] = [18,20,22]
    neighbor[22] = [13,19,21]
    return neighbor[x]


def closeMill(j:int, L:list):
    ch = L[j]
    if j==0:
        if (L[1]==ch and L[2]==ch) or (L[3]==ch and L[6]==ch or (L[8]==ch and L[20]==ch)):
            return True
        else: return False
    elif j==1:
        if (L[0]==ch and L[2]==ch):
            return True
        else: return False
    elif j==2:
        if(L[0]==ch and L[1]==ch) or (L[5]==ch and L[7]==ch) or (L[13]==ch and L[22]==ch):
            return True
        else: return False
    elif j==3:
        if(L[0]==ch and L[6]==ch) or (L[9]==ch and L[17]==ch) or (L[4]==ch and L[5]==ch):
            return True
        else: return False
    elif j==4:
        if(L[3]==ch and L[5]==ch):
            return True
        else: return False
    elif j==5:
        if(L[3]==ch and L[4]==ch) or (L[12]==ch and L[19]==ch) or (L[2]==ch and L[7]==ch):
            return True
        else: return False
    elif j==6:
        if(L[0]==ch and L[3]==ch) or (L[10]==ch and L[14]==ch):
            return True
        else: return False
    elif j==7:
        if(L[2]==ch and L[5]==ch) or (L[11]==ch and L[16]==ch):
            return True
        else: return False
    elif j==8:
        if(L[0]==ch and L[20]==ch) or (L[9]==ch and L[10]==ch):
            return True
        else: return False
    elif j==9:
        if(L[3]==ch and L[17]==ch) or (L[8]==ch and L[10]==ch):
            return True
        else: return False
    elif j==10:
        if(L[14]==ch and L[6]==ch) or (L[8]==ch and L[9]==ch):
            return True
        else: return False
    elif j==11:
        if(L[7]==ch and L[16]==ch) or (L[12]==ch and L[13]==ch):
            return True
        else: return False
    elif j==12:
        if(L[13]==ch and L[11]==ch) or (L[5]==ch and L[19]==ch):
            return True
        else: return False
    elif j==13:
        if(L[11]==ch and L[12]==ch) or (L[2]==ch and L[22]==ch):
            return True
        else: return False
    elif j==14:
        if(L[17]==ch and L[20]==ch) or (L[6]==ch and L[10]==ch) or (L[15]==ch and L[16]==ch):
            return True
        else: return False
    elif j==15:
        if(L[14]==ch and L[16]==ch) or (L[18]==ch and L[21]==ch):
            return True
        else: return False
    elif j==16:
        if(L[14]==ch and L[15]==ch) or (L[7]==ch and L[11]==ch) or (L[19]==ch and L[22]==ch):
            return True
        else: return False
    elif j==17:
        if(L[14]==ch and L[20]==ch) or (L[3]==ch and L[9]==ch) or (L[18]==ch and L[19]==ch):
            return True
        else: return False
    elif j==18:
        if(L[15]==ch and L[21]==ch) or (L[17]==ch and L[19]==ch):
            return True
        else: return False
    elif j==19:
        if(L[17]==ch and L[18]==ch) or (L[12]==ch and L[5]==ch) or (L[22]==ch and L[16]==ch):
            return True
        else: return False
    elif j==20:
        if(L[0]==ch and L[8]==ch) or (L[17]==ch and L[14]==ch) or (L[21]==ch and L[22]==ch):
            return True
        else: return False
    elif j==21:
        if(L[15]==ch and L[18]==ch) or (L[20]==ch and L[22]==ch):
            return True
        else: return False
    elif j==22:
        if(L[20]==ch and L[21]==ch) or (L[2]==ch and L[13]==ch) or (L[16]==ch and L[19]==ch):
            return True
        else: return False
    else: return False


def GenerateRemove(b, l1):
    k=False
    for i in range(len(b)):
        if b[i]=="B":
            if not closeMill(i,b):
                k=True
                b1 =copy.deepcopy(b)
                b1[i]="x"
                l1.append(b1)
    if k==False:
        l1.append(b)


def GenerateAdd(L:list):
    l1=[]
    for i in range(len(L)):
        if L[i]=="x":
            b = copy.deepcopy(L)
            b[i]="W"
            if(closeMill(i,b)):
                GenerateRemove(b,l1)
            else:
                l1.append(b)
    return l1


def GenerateMove(L):
    l1=[]
    for i in range(len(L)):
        if L[i]=="W":
            n= neighbors(i)
            for j in n:
                if L[j]=="x":
                    b=copy.deepcopy(L)
                    b[i]="x"
                    b[j]="W"
                    if closeMill(j,b):
                        GenerateRemove(b,l1)
                    else:
                        l1.append(b)
    return l1


def GenerateHopping(L):
    l1=[]
    for i in range(len(L)):
        if L[i]=="W":
            for j in range(len(L)):
                if L[j]=="x":
                    b=copy.deepcopy(L)
                    b[i]="x"
                    b[j]="W"
                    if closeMill(j,b):
                        GenerateRemove(b,l1)
                    else:
                        l1.append(b)
    return l1


def staticEstimate(L:list,ct):
    ct+=1
    c=collections.Counter(L)
    numWhite=c["W"]
    numBlack=c["B"]
    return (numWhite-numBlack,ct)



def GenerateMovesOpening(L: list):
    return GenerateAdd(L)


def ABOpening(L, depth:int, alpha, beta, MaximizingPlayer:bool, ct,n):

    if depth == 0:
        l,k = staticEstimate(L,ct)
        return (l,k,n)

    if MaximizingPlayer:
        maxEva = -math.inf
        l2 = GenerateMovesOpening(L)
        n = l2[0]
        for child in l2:
            eva,c,new_n = ABOpening(child, depth - 1, alpha, beta ,False,ct,n)
            ct=c
            if eva>maxEva:
                n=child
                maxEva=eva
            alpha=max(alpha,maxEva)
            if beta<=alpha: break
        return (maxEva,ct,n)

    else:
        minEva = +math.inf
        l1=copy.deepcopy(L)
        for i in range(len(l1)):
            if l1[i] =='W':
                l1[i]='M'
        for i in range(len(l1)):
            if l1[i] =='B':
                l1[i]='W'
        for i in range(len(l1)):
            if l1[i] =='M':
                l1[i]='B'
        l3 = GenerateMovesOpening(l1)
        for list in l3:
            for i in range(len(list)):
                if list[i] =="W":
                    list[i]="M"
            for i in range(len(list)):
                if list[i] =="B":
                    list[i]="W"
            for i in range(len(list)):
                if list[i] =="M":
                    list[i]="B"
        n = l3[0]
        for child in l3:
            eva,c ,q = ABOpening(child, depth - 1, alpha, beta, True,ct,n)
            ct=c
            if eva<minEva:
                minEva=eva
                n=child
            beta = min(beta,eva)
            if beta <= alpha:
                break
        return (minEva,ct,n)


if __name__ == "__main__":

    # file_location1 = "/Users/monik/PycharmProjects/AI_Project/input1.txt"
    # file_location2 = "/Users/monik/PycharmProjects/AI_Project/output3.txt"
    script, first, second, third = argv
    file_location1 = str(first)
    file_location2 = str(second)
    depth = int(third)
    file1 = open(file_location1, "r+")
    file2 = file1.readline()
    L = []
    for a in file2:
        L.append(a)
    print("Input Board:")
    print(L)
    # depth = 2
    alpha = -math.inf
    beta = math.inf
    print("AB Opening Game:")
    m,n,l = ABOpening(L, depth,alpha,beta, True, 0, [])

    print("MiniMax Estimate: %s \nPositions evaluated by static estimation:: %s \nBoard Position:: %s " % (m, n, l))
    sh="".join(l)
    print(sh)
    file1 = open(file_location2, "w+")
    file1.writelines([sh])



