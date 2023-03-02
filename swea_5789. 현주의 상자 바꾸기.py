T = int(input())
for test in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0] * N
    for i in range(Q):
        L, R = map(int, input().split())
        cnt = i + 1
        for j in range(L-1, R):
            boxes[j] = cnt


    print(f'#{test}', *boxes, sep=' ')