'''
Code : Has Path

Given an undirected graph G(V, E) and two vertices v1 and v2 (as integers), check if there exists any path between them or not. Print true if the path exists and false otherwise.

Note:
1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
2. E is the number of edges present in graph G.

Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two integers, that denote that there exists an edge between vertex 'a' and 'b'.
The following line contain two integers, that denote the value of v1 and v2.

Output Format :
The first and only line of output contains true, if there is a path between v1 and v2 and false otherwise.

Constraints :
0 <= V <= 1000
0 <= E <= 1000
0 <= a <= V - 1
0 <= b <= V - 1
0 <= v1 <= 2^31 - 1
0 <= v2 <= 2^31 - 1

Time Limit: 1 second

Sample Input 1 :
4 4
0 1
0 3
1 2
2 3
1 3

Sample Output 1 :
true

Sample Input 2 :
6 3
5 3
0 1
3 4
0 3

Sample Output 2 :
false
'''

import queue
from sys import stdin

class Graph :
    def __init__ (self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[ 0 for i in range(nVertices+1)] for j in range(nVertices+1)]
    def addEdge (self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def __hasPathHelper(self, v1, v2, visited):
        if self.adjMatrix[v1][v2] == 1:
            return True
        else:
            visited[v1] = True
            for i in range(self.nVertices):
                if self.adjMatrix[v1][i] > 0 and visited[i] is False:
                    flag = self.__hasPathHelper(i, v2, visited)
                    if flag:
                        return flag
        return False
    
    def hasPath(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        return self.__hasPathHelper(v1, v2, visited)

#main
v, e = input().strip().split(' ')
v = int(v)
e = int(e)
g = Graph(v)
for i in range(e):
    li = stdin.readline().rstrip().split(" ")
    x = int(li[0])
    y = int(li[1])
    g.addEdge(x, y)
v1, v2 = input().strip().split(' ')
v1 = int(v1)
v2 = int(v2)
ans = g.hasPath(v1, v2)
if ans:
    print('true')
else:
    print('false')