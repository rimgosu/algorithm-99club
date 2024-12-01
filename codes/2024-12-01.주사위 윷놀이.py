from typing import Literal


dic = {
    0: ([1], 0),
    1: ([2], 2),
    2: ([3], 4),
    3: ([4], 6),
    4: ([5], 8),
    5: ([6, 22], 10),
    6: ([7], 12),
    7: ([8], 14),
    8: ([9], 16),
    9: ([10], 18),
    10: ([11, 28], 20),
    11: ([12], 22),
    12: ([13], 24),
    13: ([14], 26),
    14: ([15], 28),
    15: ([16, 30], 30),
    16: ([17], 32),
    17: ([18], 34),
    18: ([19], 36),
    19: ([20], 38),
    20: ([21], 40),
    21: ([], 0),
    22: ([23], 13),
    23: ([24], 16),
    24: ([25], 19),
    25: ([26], 25),
    26: ([27], 30),
    27: ([20], 35),
    28: ([29], 22),
    29: ([25], 24),
    30: ([31], 28),
    31: ([32], 27),
    32: ([25], 26)
}
abnormal = [5,10,15]
lst = list(map(int,input().split()))

def move(num, mode: Literal['normal'] | Literal['abnormal']):
    now = num
    _next_lst, _ = dic[now]

    if mode == 'normal':
        return _next_lst[0]
    else:
        return _next_lst[1]

answer_lst = []
def dfs(minions: list, cnt: int, answer: int):
    if cnt == 10:
        answer_lst.append(answer)
        return
    for idx, minion in enumerate(minions):
        minions_copy = [m for m in minions]
        now = minions_copy.pop(idx)
        if now == 21:
            continue
        elif now in abnormal:
            now = move(now, 'abnormal')
            for _ in range(lst[cnt]-1):
                now = move(now, 'normal')
                if now == 21:
                    break
        else:
            for _ in range(lst[cnt]):
                now = move(now, 'normal')
                if now == 21:
                    break

        minions_copy.append(now)
        dfs(minions_copy, cnt + 1, answer + dic[now][1])

dfs([0,0,0,0], 0, 0)
print(max(answer_lst))