T = int(input())
for test in range(1, T+1):
    claps = list(map(int, input()))

    audience = 0
    hired = 0
    for i in range(len(claps)):
        total_clap = audience + hired
        if i <= total_clap:
            audience += claps[i]

        else:
            hired += i - total_clap
            audience += claps[i]


    print(f'#{test} {hired}')