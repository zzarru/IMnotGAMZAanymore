'''
1) 학생 수(N)만큼 빈 리스트를 만들어준다. (줄 서는 순서)
2) 뽑은 자리의 인덱스를 구한다. (학생 번호 - 몇칸 앞으로 가는지 - 1)
3-1) 가야할 자리(idx)가 비어있다면 줄을 선다.
3-2) 가야할 자리에 다른 학생이 있다면, 그 뒤의 학생들을 한 칸씩 뒤로 밀고 줄을 선다.
'''
N = int(input())
lst = list(map(int, input().split()))

lunch = [0]*N

student = 1
for i in lst:
    idx = student - i - 1
    if lunch[idx] != 0:
        for j in range(idx+1, N):
            k = N - j + idx
            tmp = lunch[k-1]
            lunch[k] = tmp

        lunch[idx] = student

    else:
        lunch[idx] = student

    cnt += 1

print(*lunch, sep= ' ')