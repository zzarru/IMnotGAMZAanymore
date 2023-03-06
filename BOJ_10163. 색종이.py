"""
문어박사님 풀이1
"""

N = int(input())
confetti = [[0] * 1001 for _ in range(1001)]

for n in range(1, N+1):
    Sj, Si, w, h = map(int, input().split())

    for i in range(Si, Si+h):
        for j in range(Sj, Sj+w):
            confetti[i][j] = n

for n in range(1, N+1):
    cnt = 0
    for paper in confetti:
        cnt += paper.count(n)
    print(cnt)