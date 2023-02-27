'''
1) NxN (N은 항상 홀수)이므로 N//2 행이 중심이 된다.
2) N//2 행을 중심으로 1씩 멀어질수록 수확할 수 있는 농작물의 범위는 2씩 감소한다.
3) N//2행보다 작은 행의 경우, N//2행의 경우, N//2행보다 큰 경우를 나누어 수확범위를 설정한다.
4) 범위 내에 있는 수확물의 가격을 price에 더해주어 총 수익을 구한다.
'''
T = int(input())
for test in range(1,T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    price = 0
    for i in range(N):
        #2 N//2보다 작은 행의 경우 i가 증가할수록 수확범위가 +2
        if i < N//2:
            for j in range(N//2-i, N - N//2+i):
                price += farm[i][j]

        #3 N//2 행의 경우 수확범위는 N
        elif i == N//2:
            for j in range(N):
                price += farm[i][j]

        #4 N//2보다 큰 행의 경우 i가 증가할수록 수확범위가 -2
        else:
            for j in range(i-N//2, N - (i-N//2)):
                price += farm[i][j]

    print(f'#{test} {price}')