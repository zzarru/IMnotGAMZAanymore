'''
1)
'''
T = int(input())
for test in range(1, T+1):
    N = int(input())

    #1 숫자 표시해줄 리스트 만들기 (0~9번의 idx)
    num_lst = [0] * 10
    k = 1
    while 0 in num_lst:
        sheep = k * N
        for i in range(7):
            if 10 ** i <= sheep < 10 ** (i + 1):
                digit = i

                for j in range(digit+1):
                    j = digit - j
                    num = sheep // 10**j
                    num_lst[num] = 1
                    sheep = sheep % 10**j

        k += 1

    print(f'#{test} {(k-1)*N}')