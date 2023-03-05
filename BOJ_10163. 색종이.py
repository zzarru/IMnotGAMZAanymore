N = int(input())
confetti = [[0] * 101 for _ in range(101)]

cnt = 1
for _ in range(N):
    Si, Sj, w, h = map(int, input().split())

    for i in range(h):
        for j in range(w):
            Pi = Si + i
            Pj = Sj + j

            confetti[Pi][Pj] = cnt

    cnt += 1

for k in range(1, N+1):
    paper = 0
    for i in range(101):
        for j in range(101):
            if k == confetti[i][j]:
                paper += 1

    print(paper)