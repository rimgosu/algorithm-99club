total_input = int(input())
total = []
visited = {}
for i in range(total_input):
    total.append(i+1)
    visited[i+1] = False
start, end = map(int, input().split())
number = int(input())
dict = {}
for i in range(number):
    rel1, rel2 = map(int, input().split())
    if not rel1 in dict:
        dict[rel1] = []
    if not rel2 in dict:
        dict[rel2] = []
    dict[rel1].append(rel2)
    dict[rel2].append(rel1)

can_visit = [False]
visited[start] = True
def bfs(count, visit, where):
    if where == end:
        print(count)
        can_visit[0] = True
    
    for next in dict[where]:
        if not visit[next]:
            visit[next] = True
            bfs(count+1, visit, next)

bfs(0,visited,start)
if not can_visit[0]:
    print(-1)