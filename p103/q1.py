'''
실습일: 2024.10.08
실습자: 201910852 심기윤
실습내용: 클래스 활용
'''

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
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

# import한 곳에선 실행되지 않고 이 파일을 실행할 때만 실행될 수 있게하는 코드
if __name__ == "__main__":
    n1 = nemo(5, 10)
    print(f'면적: {n1.area()}')
    print(f'둘레: {n1.perimeter()}')



