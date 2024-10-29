'''
실습일: 2024.10.29
실습자: 201910852 심기윤
실습내용: 사용중인 pc의 ip주소 찾아 출력
'''
import socket

print(f'내 PC 이름: {socket.gethostname()}')
print(f'내 PC IP주소: {socket.gethostbyname(socket.gethostname())}')