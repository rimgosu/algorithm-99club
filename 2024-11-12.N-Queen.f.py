import sys
sys.setrecursionlimit(10**6)

n = int(input())
chess_board = [[True] * n for _ in range(n)]
directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

answer = [0]
def dfs(count, board):
    print(count, board)
    if count == 8:
        answer[0] += 1
        return
    
    for i in range(n):
        x,y = i,count
        board_copy = []
        for dy in range(n):
            temp = []
            for dx in range(n):
                temp.append(board[dy][dx])
            board_copy.append(temp)
        if board[y][x]: # y,x
            board_copy[y][x] = False
            for dx, dy in directions:
                nx, ny = x, y
                while True:
                    nx += dx
                    ny += dy
                    if not 0 <= nx < n or not 0 <= ny < n:
                        break

                    if board_copy[ny][nx]:
                        board_copy[ny][nx] = False
                    else:
                        return
                    
        
        dfs(count+1, board_copy)
        count -= 1

dfs(0,chess_board)
print(answer[0])