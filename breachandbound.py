from icecream import ic
import numpy as np


class Node:
    def __init__(self, tree, weight, free, jail):
        self.tree =  tree
        self.weight = weight
        self.free = free
        self.jail = jail



def startDicts(n):
    dict = {}
    for i in range(n):
        dict[i+1] = []
    return dict


def verifyDegrees(dicts):
    flag = True
    hNode = 0
    for i in range(N):
        if(len(dicts[i]) > len(dicts[hNode])):
            hNode = i
        if(len(dicts[i]) != 2 and (flag)):
            flag = False
    return flag, hNode


def MSTprim(graph,nvertices):
    selected_node = [0]*nvertices

    no_edge = 0

    selected_node[0] = True

    dicts = startDicts(nvertices)

    weight=0

    # printing for edge and weight
    print("Edge : Weight\n")
    while (no_edge < nvertices - 1):
        minimum = INF
        a = 0
        b = 0
        for i in range(nvertices):
            if selected_node[i]:
                for j in range(nvertices):
                    if ((not selected_node[j]) and graph[i][j]):  
                        # not in selected and there is an edge
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            a = i
                            b = j
        print(str(a) + "-" + str(b) + ":" + str(graph[a][b]))

        weight += graph[a][b]
        dicts[a+1].append(b+1)
        dicts[b+1].append(a+1)

        selected_node[b] = True
        no_edge += 1
    return dicts, weight


def build1tree(G, N):
    
    redG = G[1:,1:]
    ic(G)

    dicts, weight = MSTprim(redG, N-1)

    minimum = INF
    a=0
    b=0
    dicts[0]=[]
    selected_node = [0]*N


    for i in range(N):
        if(G[0][i]):
            if (minimum > G[0][i]):
                minimum = G[0][i]
                a = 0
                b = i
    selected_node[b] = True

    dicts[a].append(b)
    dicts[b].append(a)
    weight += G[a][b]

    minimum = INF

    for i in range(N):
        if(G[0][i] and (not selected_node[i])):
            if(minimum > G[0][i]):
                minimum = G[0][i]
                a = 0
                b = i
    
    dicts[a].append(b)
    dicts[b].append(a)
    weight += G[a][b]
    ic(weight)
    return dicts, weight




INF = 9999999
# number of vertices in graph
N = 5
G = np.array([[0, 2, 0, 6, 3],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [3, 5, 7, 9, 0]])


onetree, weight = build1tree(G, N)
ic(onetree)

flag, hNode = ic(verifyDegrees(onetree))

# A dictionary referencing graphs edges and it's weights
free = {}
# A dictionary with the key referencing a graph edge 
#and it's value indicating it's weight and if it is
#to be forced or not
jail = {}

# Initializing free dict
for i in range(N):
    for j in onetree[i]:
        free[(i,j)] = G[i][j]
ic(free)

# Initializing jail dict
minWei = (INF,0)
minWei2 = (INF,0)
for i in onetree[hNode]:
    if(minWei[0] > G[hNode][i]):
        minWei = ic((G[hNode][i],i))
jail[(hNode,minWei[1])] = [minWei[0], 1]
ic(jail)
ic(minWei[0])

for i in onetree[hNode]:
    if(i != minWei[1] and minWei2[0] > G[hNode][i]):
        minWei = (G[hNode][i],i)

#arr = [Node(onetree, weight, free, jail)]
#jail[(hNode,maxWei[1])] = [maxWei[0], 0]
#arr.append([Node(onetree, weight, free, jail)])



while(not flag):
    break