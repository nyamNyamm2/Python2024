'''
실습일: 2024.10.08
실습자: 201910852 심기윤
실습내용: 클래스 활용
'''

# q1
class nemo:
    def __init__(self, w = 0, h = 0):
        self.w = w
        self.h = h

    def getW(self):
        return self.w

    def getH(self):
        return self.h

    def setW(self, w):
        self.w = w

    def setH(self, h):
        self.h = h

    def area(self):
        print('면적: ', self.w * self.h)

    def perimeter(self):
        print('둘레: ', 2 * (self.w + self.h))

n1 = nemo(5, 10)
n1.area()
n1.perimeter()


# q2
class square(nemo):
    def __init__(self, m = 0):
        self.m = m

    def area(self):
        print('면적: ', self.m * self.m)

    def perimeter(self):
        print('둘레: ', 4 * self.m)

n2 = square(5)
n2.area()
n2.perimeter()
