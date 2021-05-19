#graph = {1:[2], 2:[3,4], 3:[7], 4:[5,6], 5:[], 6:[], 7:[]}

graph = {}
n = int(input('no. of nodes: '))

for i in range(n):
    key = int(input('Enter root node: '))
    print('enter its children L-R: ')
    child = [int(i) for i in input().split()]
    graph[key] = child

# Depth First Search
visit = [0 for i in range(n)]
def dfs(key):
    print(key)
    visit[key-1] = 1
    child = graph[key]
    for key in child:
        if(visit[key-1]!=1):
            dfs(key)

dfs(1)