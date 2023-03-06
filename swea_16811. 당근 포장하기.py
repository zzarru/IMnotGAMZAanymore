'''
조건
1) 소, 중, 대로 구분해서 넣어야한다.
2) 같은 크기의 당근은 같은 상자에
3) 비어있는 상자는 없다.
4) 한 상자에 N/2개를 초과하는 당근을 담을 수 없다.
5) 각 상자의 든 당근의 개수가 최소가 되도록 포장한다.

풀이
1) 당근 크기에 따라 오름차순으로 정렬한다.
2)

'''

T = int(input())
for test in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))

    #1 오름차순 정렬
    carrots.sort()

    minV = 1000
    for i in range(N-2): # 소박스
         for j in range(i+1, N-1): # 중박스
             if carrots[i] != carrots[i+1] and carrots[j] != carrots[j+1]: #같은 크기의 당근이 다른 상자에 들어가지 않도록
                s = i + 1
                m = j - i
                l = N - 1- j

                # 빈 박스가 없고, 각 상자에 총 당근의 절반 초과하지 않도록 담기
                if s*m*l != 0 and s<= N//2 and m<= N//2 and l<= N//2:
                    if minV > max(s, m, l) - min(s, m, l):
                        minV = max(s, m, l) - min(s, m, l)

    # 포장이 불가한 경우
    if minV == 1000:
        minV = -1


    print(f'#{test} {minV}')




