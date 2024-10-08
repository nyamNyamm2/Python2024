'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: 마일과 갤런을 입력받은 후 km, l로 변환
'''

mile = int(input("마일: "))
gallon = int(input("갤런: "))

print("%d마일은 %.3fkm, %d갤런은 %.3fl" %(mile, mile*1.6, gallon, gallon*3.7854))