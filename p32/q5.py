'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: 학점 출력하기
'''

exam, report = map(int, input("시험, 과제 점수 입력: ").split())
print('A') if exam >= 90 or report >= 90 else print()