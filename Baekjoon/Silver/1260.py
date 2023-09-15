from collections import deque
import sys

n, m, v = map(int, sys.stdin.readline().split())
graph = [[False] * (n+1) for i in range(n+1)]
visitedDFS = [False] * (n+1)
visitedBFS = [False] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = True
    
def dfs(v):
    visitedDFS[v] = True
    print(v, end = " ")
    
    for i in range(1, n+1):
        if graph[v][i] == True and visitedDFS[i] == False:
            dfs(i)
            
def bfs(v):
    print() #줄바꿈
    queue=deque([v])
    visitedBFS[v] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        
        for i in range(1, n+1):
            if(graph[v][i] == True and visitedBFS[i] == False):
                queue.append(i)
                visitedBFS[i] = True
            
dfs(v)
bfs(v)
