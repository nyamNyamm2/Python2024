'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: cm 입력받기
'''

cm = float(input("cm 입력: "))

if cm < 0:
    print("잘못 입력하였습니다")
elif cm > 0:
    print("%.0f인치" %(cm / 2.54))




# 24.10.18 중간대비 복습
user = float(input("cm 입력: "))
if user < 0:
    print("잘못 입력하셨습니다.")
else:
    print(f'{user / 2.54:.2f}인치')