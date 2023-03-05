"""
1) 암호에서 하나씩 순회하면서 신호에 있는지 확인한다.
2) 암호 하나가 맞으면 인덱스를 조정해서 그 이후에 다음 암호가 신호에 들어있는지 확인한다.
3) 암호를 확인할 때마다 cnt를 1씩 증가시킨다.
4) 작업을 마무리하고 cnt의 길이와 암호의 길이가 일치하면 1을 출력 (아니면 0을 출력한다.)
"""

T = int(int(input()))
for test in range(1, T+1):
    N, K = map(int, input().split())
    signals = list(map(int, input().split()))
    pws = list(map(int, input().split()))

    cnt = 0
    Si = 0
    for pw in pws:
        for i in range(Si, len(signals)):
            if pw == signals[i]:
                Si = i + 1
                cnt += 1
                break

    if cnt == K:
        print(1)

    else:
        print(0)

