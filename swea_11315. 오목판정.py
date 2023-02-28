'''
1) 가로, 세로, 대각선을 탐색하며 돌이 연속하여 5개 놓여져 있으면 YES
2) 5개가 연속하여 놓이기 위한 최소 조건을 설정하여, 반복문 작동 횟수를 줄인다.
'''
T = int(input())
for test in range(1, T+1):
    N = int(input())
    omok = [list(map(str, input())) for _ in range(N)]


    ans = 0
    #1 가로줄 탐색 -> 적어도 첫번째 돌은 N-5의 위치에 놓여있어야한다.
    for i in range(N):
        for j in range(N-4):
            if omok[i][j] == 'o':
                cnt = 0
                for k in range(j, j+5):
                    if omok[i][k] == 'o':
                        cnt += 1
                    else:
                        break

                if cnt == 5:
                    ans += 1


    #2 세로줄 탐색 -> 적어도 첫번째 돌은 N-5의 위치에 놓여있어야한다.
    for i in range(N-4):
        for j in range(N):
            if omok[i][j] == 'o':
                cnt = 0
                for k in range(i, i+5):
                    if omok[k][j] == 'o':
                        cnt += 1
                    else:
                        break

                if cnt == 5:
                    ans +=1

    #3 우하향 대각선 탐색
    for i in range(N-4):
        for j in range(N-4):
            cnt = 0
            if omok[i][j] == 'o':
                for k in range(5):
                    if omok[i+k][j+k] == 'o':
                        cnt += 1
                    else:
                        break

            if cnt == 5:
                ans += 1

    #4 좌하향 대각선 탐색
    for i in range(N-4):
        for j in range(N-4):
            j = (N-1)- j
            cnt = 0
            if omok[i][j] == 'o':
                for k in range(5):
                    if omok[i+k][j-k] == 'o':
                        cnt +=1
                    else:
                        break

            if cnt == 5:
                ans += 1

    if ans:
        print(f'#{test} YES')
    else:
        print(f'#{test} NO')