T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    flags = [list(input()) for _ in range(N)]


    total = 0
    for i in range(N-2):
        for j in range(i + 1, N - 1):
            cnt = 0
            for k in range(i+1):
                cnt += flags[k].count('W')
            for k in range(i+1, j+1):
                cnt += flags[k].count('B')
            for k in range(j+1, N):
                cnt += flags[k].count('R')

            total = max(total, cnt)

    print(f'#{test}', N*M-total)