T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    flags = [list(input()) for _ in range(N)]

    for i in range(N-2):
        for j in range(i+1, N-1):