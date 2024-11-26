V, E, R = map(int, input().split())
정점 = []
for i in range(V):
    정점.append(i+1)
간선 = []
for i in range(E):
    간선.append(tuple(map(int, input().split())))

# 방문 처리, 간선 처리
visited = {}
line = {}
order = {}  # 방문 순서를 저장할 딕셔너리

# 모든 정점에 대해 초기화
for 정 in 정점:
    visited[정] = False
    line[정] = []
    order[정] = 0  # 방문하지 않은 정점은 0으로 초기화

# 간선 정보 추가
for 간 in 간선:
    x, y = 간
    line[x].append(y)
    line[y].append(x)

# 각 정점의 인접 리스트 정렬
for i in line.keys():
    line[i].sort()

# BFS 실행
visited[R] = True
queue = []
queue.append(R)
count = 1  # 방문 순서를 기록할 변수
order[R] = count  # 시작 정점의 방문 순서는 1

while queue:
    v = queue.pop(0)
    for i in line[v]:
        if not visited[i]:
            count += 1
            visited[i] = True
            order[i] = count
            queue.append(i)

# 각 정점의 방문 순서 출력
for i in range(1, V+1):
    print(order[i])