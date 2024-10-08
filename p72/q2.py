'''
실습일: 2024.09.24
실습자: 201910852 심기윤
실습내용: 리스트활용
'''

n, m = map(int, input().split())

mylist1 = []
mylist2 = []
mylist3 = [[0 for i in range(m)] for j in range(n)]

# # 2차원 배열 선언방법
# arr = []
# for i in range(n):
#     arr.append([])
#     for j in range(m):
#         arr[i].append(0)
# print(arr)

# # 2차원 배열 값 추출방법
# arr[0:2]
# arr[1][0:2]
# arr[0:2] = [[0, 0], [0, 1]]
# arr[3][0:2] = [99, 99]

for i in range(n):
    mylist1.append(list(map(int, input().split())))
    mylist2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        mylist3[i][j] = mylist2[i][j] + mylist1[i][j]

print(mylist3)

