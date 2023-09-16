import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
count = -1

graph = [[False] * (n+1) for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = True
    
def dfs(v):
    visited[v] = True
    global count
    count+=1
    
    for i in range(1, n+1):
        if graph[v][i] == True and visited[i] == False:
            dfs(i)
            
dfs(1)
print(count)
