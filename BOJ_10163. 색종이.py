N = int(input())
confetti = [[0] * 101 for _ in range(101)]

for _ in range(N):
    Si, Sj, w, h = map(int, input().split())

    for i in range(h):
        for j in range(w):
            Pi = Si + i
            Pj = Sj + j

            confetti[Pi][Pj] = 1

cnt = 0
for i in confetti:
    cnt += sum(i)

print(cnt)