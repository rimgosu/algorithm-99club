case_number = int(input())

cases = {}
for i in range(case_number):
    cases[i] = []
    cases[i].append(int(input()))
    cases[i].append(tuple(map(int, input().split())))
    cases[i].append(tuple(map(int, input().split())))

for case in cases.values():
    length, start, end = case[0], case[1], case[2]

    directions = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
    visited = []
    for i in range(length):
        temp = []
        for j in range(length):
            temp.append(False)
        visited.append(temp)

    queue = []
    queue.append((start, 0))
    visited[start[1]][start[0]] = True

    while queue:
        where, count = queue.pop(0)
        x,y = where
        if where == end:
            print(count)
            break
        for dx,dy in directions:
            if 0<= dx+x < length and 0<= dy+y < length and not visited[y+dy][x+dx]:
                queue.append(((x+dx,y+dy), count+1))
                visited[y+dy][x+dx] = True
    