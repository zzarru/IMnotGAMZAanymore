'''
1) 아홉 난쟁이의 키를 리스트로 받아주고 총 합을 구한다.
2) 가짜 난쟁이 2명의 키의 합을 구한다.(over_heights) : 아홉 난쟁이 키 합 - 100
3) 리스트를 순회하며 난쟁이 두명의 키 합이 over_heights가 되는 경우를 찾는다.
4) 가짜 난쟁이 2명을 제외한, 진짜 난쟁이의 리스트를 만들고 오름차순으로 정렬한 뒤 출력한다.
'''

#1 아홉 난쟁이의 키 input받기
heights = []
for i in range(9):
    height = int(input())
    heights.append(height)

#2 가짜 난쟁이의 키 합 구하기
over_heights = sum(heights) - 100

#3 가짜 난쟁이의 인덱스를 튜플 형식으로 넣어준다.
fakers = []
for i in range(len(heights)-1):
    for j in range(i+1, len(heights)):
        if heights[i] + heights[j] == over_heights:
            fakers.append((i,j))

#4-1 중복된 값이 있는 경우, 아무 거나 출력하면 되므로 가짜 난쟁이의 경우의 수 중 하나만 따져서 일곱 난쟁이를 찾는다.
dwarfs = []
for i in range(9):
    if i not in fakers[0]:
        dwarfs.append(heights[i])

#4-2 오름차순 정렬
dwarfs.sort()

for dwarf in dwarfs:
    print(dwarf)