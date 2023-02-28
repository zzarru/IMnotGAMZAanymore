'''
전치행렬을 만들어 차례로 리스트의 값을 읽어오면 된다.
*전제 : 전치행렬을 만들기 위해서는 NxN의 구조여야 한다.

1) 리스트를 순회하며 가장 긴 리스트의 길이(len_max)를 구한다.
2) 가장 리스트의 길이와 같도록, 리스트에 공백을 추가한다.
3) 리스트를 전치하여 차례로 값을 불러온다.

'''
T = int(input())
for test in range(1, T+1):
    lst = [list(map(str, input())) for _ in range(5)]

    #1 가장 긴 리스트의 길이 구하기
    len_max = 0
    for i in lst:
        if len(i) > len_max:
            len_max = len(i)

    #2 가장 긴 리스트의 길이만큼 공백 추가하기
    for i in lst:
        while len(i) != len_max:
            i.append(' ')

    #3 zip함수 이용하여 전치행렬 만들기
    lst_t = list(map(list, zip(*lst)))

    # 공백을 제외하고 문자열 출력하기
    letters = []
    for i in lst_t:
        for j in i:
            if j != ' ':
                letters.append(j)

    print(f'#{test}', ''.join(letters))