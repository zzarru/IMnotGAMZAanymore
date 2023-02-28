'''
1) 전치행렬로 바꿔주기
2) 2차원 리스트 만들어서 N극(1)과 S극(2) 순서대로 넣어주기
3) 2차원 리스트 순회하면서 1 -> 2 순서로 들어있는 경우(교착상태)의 수 세어주기
'''

T = 10
for test in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    #1 전치행렬 만들기
    lst_t = list(map(list, zip(*lst)))

    #2 magnetics에 N극, S극 놓인 순서대로 넣어주기
    magnetics = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lst_t[i][j] == 1 or lst_t[i][j] == 2:
                magnetics[i].append(lst_t[i][j])

    #3 교착상태의 개수 세어주기
    cnt = 0
    for magnetic in magnetics:
        for i in range(len(magnetic)-1):
            if magnetic[i] == 1 and magnetic[i+1] == 2:
                cnt += 1

    print(f'#{test} {cnt}')