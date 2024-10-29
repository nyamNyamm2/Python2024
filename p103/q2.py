'''
실습일: 2024.10.17
실습자: 201910852 심기윤
실습내용: 클래스 활용
'''

from q1 import nemo
class square(nemo):
    def __init__(self, m = 0):
        self.m = m

    def area(self):
        return self.m * self.m

    def perimeter(self):
        return  4 * self.m

n2 = square(5)
print(f'면적: {n2.area()}')
print(f'둘레: {n2.perimeter()}')