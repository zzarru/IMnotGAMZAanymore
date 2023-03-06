'''
1) 델타탐색 (상좌우하) 범위 설정
2) 가운데 풍선의 숫자만큼 거리 증가
3) 터진 꽃가루의 개수가 가장 큰 값을 구한다.
'''

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]

    #1 델타탐색 (상, 좌, 우, 하)
    di = [-1, 0, 0, 1]
    dj = [0, -1, 1, 0]

    max_pang = 0
    for i in range(N):
        for j in range(M):
            pang = balloons[i][j] # 가운데 풍선의 값을 미리 넣어준다. (중복 터짐 방지)
            l = balloons[i][j] # 가운데 풍선의 값 == 거리만큼 터진다.
            for k in range(4):
                for h in range(1, 1+l):
                    ni = i + di[k]*h
                    nj = j + dj[k]*h

                    if 0 <= ni < N and 0 <= nj < M:
                        pang += balloons[ni][nj]

            if pang > max_pang:
                max_pang = pang

    print(f'#{test} {max_pang}')
