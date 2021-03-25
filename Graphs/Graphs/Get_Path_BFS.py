'''
Code : Get Path - BFS

Given an undirected graph G(V, E) and two vertices v1 and v2 (as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
Find the path using BFS and print the shortest path available.

Note:
1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
2. E is the number of edges present in graph G.
3. Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
4. Save the input graph in Adjacency Matrix.

Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two integers, that denote that there exists an edge between vertex a and b.
The following line contain two integers, that denote the value of v1 and v2.

Output Format :
Print the path from v1 to v2 in reverse order.

Constraints :
2 <= V <= 1000
1 <= E <= (V * (V - 1)) / 2
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
3 0 1

Sample Input 2 :
6 3
5 3
0 1
3 4
0 3

Sample Output 2 :
'''

# Write your code here
import queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

class Graph :
    def __init__ (self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[ 0 for i in range(nVertices+1)] for j in range(nVertices+1)]
    def addEdge (self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __getPathHelper(self, v1, v2, visited):
        if v1 == v2:
            visited[v1] = True
            output = []
            output.append(v1)
            return output
        
        q = queue.Queue()
        map = {}
        q.put(v1)
        visited[v1] = True
        map[v1] = -1
        done = False
        while q.empty() is False and not done:
            temp = q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[temp][i] == 1 and not visited[i] and temp != i:
                    map[i] = temp
                    q.put(i)
                    visited[i] = True
                    if i == v2:
                        done = True
                        break
        output = []
        if done:
            i = v2
            while i != -1:
                output.append(i)
                i = map[i]
            return output
        else:
            return None

    def getPath(self, v1, v2):
        visited = [False for i in range(self.nVertices+1)]
        return self.__getPathHelper(v1, v2, visited)

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
ans = g.getPath(v1, v2)
if ans is not None:
    for i in ans:
        print(i, end=' ')