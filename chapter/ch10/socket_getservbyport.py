'''
실습일: 2024.10.29
실습자: 201910852 심기윤
실습내용: socket 실습
'''

# 포트번호로부터 서비스 이름 찾는 프로그램

import socket

for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
    print(f'{port:4d}: {socket.getservbyport(port)}')
