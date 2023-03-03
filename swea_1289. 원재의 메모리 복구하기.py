T = int(input())
for test in range(1, T+1):
    memory= list(map(int, input()))

    cnt = 0
    num = 0
    for i in memory:
        if i != num:
            cnt += 1
            num = i

    print(f'#{test} {cnt}')