N = int(input())
paper = [[0]*100 for _ in range(100)]
for _ in range(1, N+1):
    Cj, Ci = map(int, input().split())

    for i in range(Ci, Ci+10):
        for j in range(Cj, Cj+10):
            paper[i][j] = 1

total = 0
for conffetti in paper:
    total += sum(conffetti)


print(total)