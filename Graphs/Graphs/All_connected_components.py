'''
Code : All connected components

Given an undirected graph G(V,E), find and print all the connected components of the given graph G.

Note:
1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
2. E is the number of edges present in graph G.
3. You need to take input in main and create a function which should return all the connected components. And then print them in the main, not inside function.
Print different components in new line. And each component should be printed in increasing order (separated by space). Order of different components doesn't matter.

Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two space separated integers, that denote that there exists an edge between vertex a and b.

Output Format :
Print different components in new line. And each component should be printed in increasing order of vertices (separated by space). Order of different components doesn't matter.

Constraints :
0 <= V <= 1000
0 <= E <= (V * (V - 1)) / 2
0 <= a <= V - 1
0 <= b <= V - 1

Sample Input 1:
4 2
0 1
2 3

Sample Output 1:
0 1 
2 3 

Sample Input 2:
4 3
0 1
1 3 
0 3
Sample Output 2:
0 1 3 
2
'''

# Write your code here
from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

class Graph :
    def __init__ (self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[ 0 for i in range(nVertices)] for j in range(nVertices)]
    def addEdge (self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __allConnectedComponentsHelper(self, sv, visited, connected):
        connected.append(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                self.__allConnectedComponentsHelper(i, visited, connected)

    def allConnectedComponents(self):
        visited = [False for i in range(self.nVertices)]
        allConnected = []
        for i in range(self.nVertices):
            if not visited[i]:
                connected = []
                self.__allConnectedComponentsHelper(i, visited, connected)
                allConnected.append(connected)
        return allConnected

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
ans = g.allConnectedComponents()
for i in ans:
    i.sort()
    for j in i:
        print(j, end=' ')
    print()