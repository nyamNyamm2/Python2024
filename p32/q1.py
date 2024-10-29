'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: 마일과 갤런을 입력받은 후 km, l로 변환
'''

mile = int(input("마일: "))
gallon = int(input("갤런: "))

print("%d마일은 %.3fkm, %d갤런은 %.3fl" %(mile, mile*1.6, gallon, gallon*3.7854))




# 24.10.18 중간대비 복습
m, g = map(int, input("마일과 갤런을 차례대로 입력: ").split())
print(f'미국식 표현인 {m}마일은 한국식 표현으로 {m*1.6:.2f}km이고 {g}갤런은 {g*3.7854:.2f}리터 입니다.')
