'''
1) 호석이 불면증 걸렷구나.. 언니 화이팅
'''
T = int(input())
for test in range(1, T+1):
    N = int(input())

    num_lst = [1]*10
    # while sum(num_lst) == 0:
    k = 1
    sheep = k*N

    # 자릿수 구하기
    for i in range(7):
        if 10 ** i <= sheep < 10 ** (i + 1):
            digit = i

            for j in range(digit):
                j = digit - j
                for l in range(j):
                    num = sheep//10**l
                    print(num)