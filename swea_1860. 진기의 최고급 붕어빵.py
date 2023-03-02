T = int(input())
for test in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    customers = sorted(customers)

    result = "Possible"
    for i in range(N):
        fish_bread = (customers[i] // M)* K - (i+1)
        if fish_bread < 0:
            result = "Impossible"
            break

    print(f'#{test} {result}')