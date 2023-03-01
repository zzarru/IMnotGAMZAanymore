'''
1) 2차원 리스트 만들기 (파리 영역)
2) 리스트 순회하며 파리채의 영역(MxM)의 합 구하기
3) 그 합의 max값 구하기
'''
T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for i in range(N-M+1): # 파리채가 NxN의 영역을 벗어나지 않도록 범위 설정
        for j in range(N-M+1):
            kill = 0
            for k in range(M): # 파리채의 영역만큼의 파리 수 구하기
                for l in range(M):
                    kill += flies[i+k][j+l]
                    
            if kill > max_kill:
                max_kill = kill

    print(f'#{test} {max_kill}')